import sqlite3
import datetime as dt

from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem, QMessageBox

from interfaces.ui_create_invoice_widget import Ui_Create_invoice
from nomenclature.nomenclature_dialog import NomenclatureDialog


class InvoiceWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.id = None
        self.ui = Ui_Create_invoice()
        self.ui.setupUi(self)
        self.ui.delete_btn.hide()
        self.ui.date_lbl.setText("--.--.----")
        self.ui.status_lbl.setText("---------")

        self.ui.tableWidget.hideColumn(0)

        self.ui.add_nomenclature_btn.clicked.connect(self.open_nomenclature_dialog)
        self.ui.save_btn.clicked.connect(self.save)
        self.ui.menu_btn.clicked.connect(parent.open_menu)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)
        self.ui.delete_btn.clicked.connect(self.delete)

    def load_request_items(self, request_item_ids):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        items = cur.execute(
            f"""
            SELECT 
                Request_items.id, 
                Request_items.amount, 
                Nomenclature.name, 
                Nomenclature.unit
            FROM Request_items
            LEFT JOIN Nomenclature ON Request_items.item_id = Nomenclature.id
            WHERE Request_items.id IN ({", ".join(["?"] * len(request_item_ids))})
            """, 
            *request_item_ids
        ).fetchall()
        for request, item_id in request_item_ids:
            nomenclature = cur.execute("SELECT name, unit FROM Nomenclature WHERE id = ?", (item_id,)).fetchone()
            if nomenclature:
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.setRowCount(row + 1)
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item_id)))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(nomenclature[0]))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(nomenclature[1]))
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem("0"))
        con.close()


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

    def set_is_created(self, id):
        self.ui.save_btn.clicked.disconnect()
        self.ui.save_btn.clicked.connect(self.update)
        self.id = id
        self.ui.delete_btn.show()

    def set_uneditable_fields(self, date, status):
        self.ui.date_lbl.setText(date.split(".")[0])
        self.ui.status_lbl.setText(status)

    def check_and_return_editable_fields(self):
        num = self.ui.num_edit.text()
        description = self.ui.description_text.toPlainText()
        rows = self.ui.tableWidget.rowCount()
        amounts = [self.ui.tableWidget.item(row, 3) for row in range(rows)]
        item_ids = None

        if not num:
            QMessageBox.warning(self, "Предупреждение", "Вы не заполнили номер")
        elif not description:
            QMessageBox.warning(self, "Предупреждение", "Вы не заполнили описание")
        elif not rows:
            QMessageBox.warning(self, "Предупреждение", "Вы не добавили номенклатуру")
        elif not all(amounts):
            QMessageBox.warning(self, "Предупреждение", "Вы не указали `Количество` у некоторых позиций")
        else:
            amounts = map(lambda item: item.text(), amounts)
            item_ids = [self.ui.tableWidget.item(row, 0).text() for row in range(rows)]

        return num, description, rows, amounts, item_ids

    def save(self):
        num, description, rows, amounts, item_ids = self.check_and_return_editable_fields()
        if not (num and description and rows and amounts):
            return
        
        created_at = dt.datetime.now()
        status = "Не согласовано"

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO (invoice_name, description, created_at, status, vender_manager_id, purchaser_id) VALUES (?, ?, ?, ?, ?, ?);", 
                        (num, description, created_at, status, 1, 1))
        except sqlite3.OperationalError as err:
            QMessageBox.critical(self, "Неизвестная ошибка", str(err))
        
        invoice_id = cur.lastrowid
        invoice_ids = [str(invoice_id)] * rows

        cur.executemany("INSERT INTO Request_items(amount, request_id, item_id) VALUES (?, ?, ?);", 
                        zip(amounts, request_ids, item_ids))
        con.commit()
        con.close()

        self.parent.tab_widget.setTabText(self.parent.tab_widget.currentIndex(), f"Заявка {request_id}")
        self.set_is_created(request_id)
        self.set_uneditable_fields(str(created_at), status)

    def update(self):
        description, rows, amounts, item_ids = self.check_and_return_editable_fields()
        if not (description and rows and amounts):
            return
        
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        try:
            cur.execute("UPDATE Requests SET description=? WHERE id=?;", (description, self.id))
        except sqlite3.OperationalError as err:
            QMessageBox.critical(self, "Неизвестная ошибка", str(err))
        
        request_ids = [str(self.id)] * rows

        cur.execute("DELETE FROM Request_items WHERE request_id=?", (self.id,))
        cur.executemany("INSERT INTO Request_items(amount, request_id, item_id) VALUES (?, ?, ?);", 
                        zip(amounts, request_ids, item_ids))
        con.commit()
        con.close()


    def load_request_data(self, request_id):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        
        # Получаем основную информацию о заявке
        request = cur.execute("SELECT description, created_at, status FROM Requests WHERE id = ?", (request_id,)).fetchone()
        if request:
            self.ui.description_text.setPlainText(request[0])
            self.set_uneditable_fields(str(request[1]), request[2])

        # Очищаем таблицу и добавляем связанные позиции заявки
        self.ui.tableWidget.setRowCount(0)
        items = cur.execute("SELECT item_id, amount FROM Request_items WHERE request_id = ?", (request_id,)).fetchall()
        for item_id, amount in items:
            nomenclature = cur.execute("SELECT name, unit FROM Nomenclature WHERE id = ?", (item_id,)).fetchone()
            if nomenclature:
                row = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.setRowCount(row + 1)
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item_id)))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(nomenclature[0]))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(nomenclature[1]))
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(amount)))
        
        con.close()
        self.set_is_created(request_id)

    def delete(self):
        res = QMessageBox.warning(self, "Предупреждение", "Вы уверены, что хотите удалить объект?", QMessageBox.Yes, QMessageBox.No)
        if res == QMessageBox.No:
            return

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        cur.execute("DELETE FROM Request_items WHERE request_id=?", (self.id,))
        cur.execute("DELETE FROM Requests WHERE id=?", (self.id,))
        con.commit()
        con.close()

        self.parent.close_current_tab()