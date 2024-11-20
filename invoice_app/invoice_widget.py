import sqlite3
import datetime as dt

from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem, QMessageBox

from interfaces.ui_create_invoice import Ui_Invoice
from nomenclature.nomenclature_dialog import NomenclatureDialog
from accept_app.accept_dialog import AcceptDialog
from vender_app.vender_dialog import VenderDialog
from contracts_app.contracts_dialog import ContractDialog
from files_app.file_dialog import FileDialog


class InvoiceWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.id = None
        self.contract_id = None
        self.ui = Ui_Invoice()
        self.ui.setupUi(self)
        self.ui.delete_btn.hide()
        self.ui.send_btn.hide()
        self.ui.accept_viewer_btn.hide()
        self.ui.date_lbl.setText("--.--.----")
        self.ui.status_lbl.setText("---------")
        self.ui.tableWidget.hideColumn(0)

        self.ui.add_nomenclature_btn.clicked.connect(self.open_nomenclature_dialog)
        self.ui.delete_nomenclature_btn.clicked.connect(self.delete_nomenclature_row)
        self.ui.save_btn.clicked.connect(self.save_invoice)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)
        self.ui.delete_btn.clicked.connect(self.delete_invoice)
        self.ui.send_btn.clicked.connect(self.open_accept_dialog)
        self.ui.vendor_btn.clicked.connect(self.open_vender_dialog)
        self.ui.contract_btn.clicked.connect(self.open_contract_dialog)
        self.ui.file_btn.clicked.connect(self.open_file_dialog)
        self.ui.accept_viewer_btn.clicked.connect(lambda: parent.open_accept_invoice_viewer(self.id))
        self.ui.tableWidget.itemChanged.connect(self.calculate_and_display_sum)

    def open_vender_dialog(self):
        dialog = VenderDialog(self.parent)
        if dialog.exec() == QDialog.Accepted and dialog.vender:
            self.ui.vendor_lbl.setText(dialog.vender)
            self.contract_id = None
            self.ui.contract_lbl.clear()

    def open_contract_dialog(self):
        vender_name = self.ui.vendor_lbl.text()
        if not vender_name:
            QMessageBox.warning(self, "Предупреждение", "Вы не добавили контрагента")
            return
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        vender_id = cur.execute("SELECT id FROM Vendor WHERE name = ?;", (vender_name,)).fetchone()[0]
        dialog = ContractDialog(self.parent, vender_id)
        if dialog.exec() == QDialog.Accepted:
            self.contract_id = dialog.contract_id
            self.ui.contract_lbl.setText(dialog.contract_name)

    def open_nomenclature_dialog(self):
        dialog = NomenclatureDialog(self.parent)
        if dialog.exec() == QDialog.Accepted:
            con = sqlite3.connect(self.parent.database_file)
            cur = con.cursor()
            nomenclature = cur.execute("SELECT * FROM Nomenclature WHERE id=?", (dialog.nomenclature_id,)).fetchone()
            con.close()

            rows = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(rows + 1)
            self.ui.tableWidget.setItem(rows, 0, QTableWidgetItem(str(nomenclature[0])))
            self.ui.tableWidget.setItem(rows, 1, QTableWidgetItem(nomenclature[1]))
            self.ui.tableWidget.setItem(rows, 2, QTableWidgetItem(nomenclature[2]))

    def delete_nomenclature_row(self):
        self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())
        self.calculate_and_display_sum()

    def set_is_created(self, id):
        self.ui.save_btn.clicked.disconnect()
        self.ui.save_btn.clicked.connect(self.update_invoice)
        self.id = id
        self.ui.delete_btn.show()
        self.ui.send_btn.show()
        self.ui.accept_viewer_btn.show()

    def set_uneditable_fields(self, date, status):
        self.ui.date_lbl.setText(date.split(".")[0])
        self.ui.status_lbl.setText(status)

    def check_and_return_editable_fields(self):
        vender_name = self.ui.vendor_lbl.text()
        name = self.ui.name_edit.text()
        description = self.ui.description_text.toPlainText()
        rows = self.ui.tableWidget.rowCount()

        # Извлечение значений из столбца 'Количество'
        amounts = []
        prices = []
        for row in range(rows):
            item = self.ui.tableWidget.item(row, 3)
            if item and item.text().strip():
                try:
                    amounts.append(float(item.text().strip()))
                except ValueError:
                    QMessageBox.warning(self, "Ошибка", f"Некорректное значение в строке {row + 1}, столбец 'Количество'")
                    return None, None, None, None, None, None, None
            else:
                QMessageBox.warning(self, "Ошибка", f"Отсутствует значение в строке {row + 1}, столбец 'Количество'")
                return None, None, None, None, None, None, None
            price = self.ui.tableWidget.item(row, 4)
            if price and price.text().strip():
                try:
                    prices.append(float(price.text().strip()))
                except ValueError:
                    QMessageBox.warning(self, "Ошибка", f"Некорректное значение в строке {row + 1}, столбец 'Цена'")
                    return None, None, None, None, None, None, None
            else:
                QMessageBox.warning(self, "Ошибка", f"Отсутствует значение в строке {row + 1}, столбец 'Цена'")
                return None, None, None, None, None, None, None

        item_ids = [self.ui.tableWidget.item(row, 0).text() for row in range(rows)]


        if not name:
            QMessageBox.warning(self, "Предупреждение", "Вы не заполнили номер счета")
        elif not vender_name:
            QMessageBox.warning(self, "Предупреждение", "Вы не добавили контрагента")
        elif not description:
            QMessageBox.warning(self, "Предупреждение", "Вы не заполнили описание")
        elif not rows:
            QMessageBox.warning(self, "Предупреждение", "Вы не добавили номенклатуру")
        elif not self.contract_id:
            QMessageBox.warning(self, "Предупреждение", "Вы не добавили договор")
        else:
            return name, description, rows, amounts, item_ids, prices

        return None, None, None, None, None, None, None


    def save_invoice(self):
        name, description, rows, amounts, item_ids, prices = self.check_and_return_editable_fields()
        if not (name and description and rows and amounts and prices):
            return
        amounts = list(amounts)
        
        created_at = dt.datetime.now()
        status = "Не согласовано"
        user_id = self.parent.user_id

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        try:
            cur.execute("""
                        INSERT INTO Invoice(invoice_name, description, created_at, status, purchaser_id, contract_id) 
                        VALUES (?, ?, ?, ?, ?, ?);
                        """, 
                        (name, description, created_at, status, user_id, self.contract_id))
        except sqlite3.Error as err:
            QMessageBox.critical(self, "Неизвестная ошибка", str(err))
        
        invoice_id = cur.lastrowid
        invoice_ids = [str(invoice_id)] * rows

        cur.executemany("INSERT INTO Invoice_items(amount, invoice_id, item_id, price) VALUES (?, ?, ?, ?);", 
                        zip(amounts, invoice_ids, item_ids, prices))
        con.commit()
        con.close()

        self.parent.tab_widget.setTabText(self.parent.tab_widget.currentIndex(), f"Счет {invoice_id}")
        self.set_is_created(invoice_id)
        self.set_uneditable_fields(str(created_at), status)
        self.parent.status_bar.showMessage("Счет успешно сохранен", 3000)

    def update_invoice(self):
        name, description, rows, amounts, item_ids, prices = self.check_and_return_editable_fields()
        amounts = list(amounts)
        if not (name and description and rows and amounts, prices):
            return
        
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        try:
            cur.execute("""
                        UPDATE Invoice 
                        SET invoice_name=?, description=?, contract_id=? 
                        WHERE id=?;
                        """, (name, description, self.contract_id, self.id))
        except sqlite3.OperationalError as err:
            QMessageBox.critical(self, "Неизвестная ошибка", str(err))
        
        invoice_ids = [str(self.id)] * rows

        cur.execute("DELETE FROM Invoice_items WHERE invoice_id=?", (self.id,))
        cur.executemany("INSERT INTO Invoice_items(amount, invoice_id, item_id, price) VALUES (?, ?, ?, ?);", 
                        zip(amounts, invoice_ids, item_ids, prices))
        con.commit()
        con.close()
        self.parent.status_bar.showMessage("Счет успешно сохранен", 3000)


    def load_invoice_data(self, invoice_id):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        
        # Получаем основную информацию о счете
        invoice = cur.execute("""
                            SELECT
                                Invoice.invoice_name,
                                Invoice.description, 
                                Invoice.created_at, 
                                Invoice.status, 
                                Contracts.id,
                                Contracts.number, 
                                Contracts.date, 
                                Vendor.name,
                                Invoice.items_sum
                            FROM Invoice 
                            LEFT JOIN Contracts ON Invoice.contract_id = Contracts.id
                            LEFT JOIN Vendor ON Contracts.vender_id = Vendor.id
                            WHERE Invoice.id = ?;
                            """, (invoice_id,)).fetchone()
        if invoice:
            self.ui.name_edit.setText(invoice[0])
            self.ui.description_text.setPlainText(invoice[1])
            self.ui.vendor_lbl.setText(invoice[7])
            self.set_uneditable_fields(str(invoice[2]), invoice[3])
            self.contract_id = invoice[4]
            self.ui.contract_lbl.setText(invoice[5] + " от " + str(invoice[6]))
            self.ui.sum_lcd.display(invoice[8])  # Заполняем итоговую сумму

        # Очищаем таблицу и добавляем связанные позиции заявки
        self.ui.tableWidget.setRowCount(0)
        items = cur.execute("""
                            SELECT item_id, amount, price 
                            FROM Invoice_items 
                            WHERE invoice_id = ?;
                            """, (invoice_id,)).fetchall()
        for item_id, amount, price in items:
            nomenclature = cur.execute("SELECT name, unit FROM Nomenclature WHERE id = ?", (item_id,)).fetchone()
            if nomenclature:
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.setRowCount(row + 1)
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item_id)))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(nomenclature[0]))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(nomenclature[1]))
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(amount)))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(price)))

        con.close()
        self.set_is_created(invoice_id)
        
        con.close()
        self.set_is_created(invoice_id)

    def delete_invoice(self):
        res = QMessageBox.warning(self, "Предупреждение", "Вы уверены, что хотите удалить объект?", QMessageBox.Yes, QMessageBox.No)
        if res == QMessageBox.No:
            return

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        cur.execute("DELETE FROM Invoice_items WHERE invoice_id=?", (self.id,))
        cur.execute("DELETE FROM Invoice WHERE id=?", (self.id,))
        con.commit()
        con.close()

        self.parent.close_current_tab()
        self.parent.status_bar.showMessage("Счет успешно удален", 3000)

    def open_accept_dialog(self):
        if not self.id:
            ans = QMessageBox.warning(self, "Предупреждение", "Для продолжения необходимо сохранить объект")
            if ans == QMessageBox.Ok:
                self.save_invoice()
            else:
                return
        dialog = AcceptDialog(self.parent)
        if dialog.exec() == QDialog.Accepted:
            approval_status = "Не согласовано"
            con = sqlite3.connect(self.parent.database_file)
            cur = con.cursor()

            max_stage = cur.execute("SELECT MAX(stage_order) FROM Invoice_approvals_stages WHERE invoice_id=?;", (self.id,)).fetchone()[0]
            if not max_stage:
                max_stage = 0
            else:
                max_stage = int(max_stage) + 1

            for stage_order, acceptor_id in enumerate(dialog.accepted_users):
                cur.execute("""
                            INSERT INTO Invoice_approvals_stages(approval_status, stage_order, invoice_id, acceptor_id) 
                            VALUES (?, ?, ?, ?)
                            """, (approval_status, max_stage + stage_order if dialog.is_step_by_step else 1, self.id, acceptor_id))

            con.commit()
            con.close()
        if not dialog.accepted_users:
            self.parent.status_bar.showMessage("Не выбраны согласованты", 3000)
        else:
            self.parent.status_bar.showMessage("Заявка успешно отправлена на согласование", 3000)

    def open_file_dialog(self):
        if not self.id:
            QMessageBox.warning(
                self, 
                "Предупреждение", 
                "Для продолжения необходимо сохранить счет"
            )
            return
        dialog = FileDialog(self.parent, self.id)
        dialog.exec()

    def calculate_and_display_sum(self):
        total_sum = 0
        rows = self.ui.tableWidget.rowCount()
        for row in range(rows):
            price_item = self.ui.tableWidget.item(row, 4)  # Колонка цены
            amount_item = self.ui.tableWidget.item(row, 3)  # Колонка количества
            if price_item and amount_item:
                try:
                    price = float(price_item.text())
                    amount = float(amount_item.text())
                    total_sum += price * amount
                except ValueError:
                    continue
        self.ui.sum_lcd.display(total_sum)
    