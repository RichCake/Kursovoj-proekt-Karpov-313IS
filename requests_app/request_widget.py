import sqlite3
import datetime as dt

from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem, QMessageBox

from interfaces.ui_create_request import Ui_Request
from nomenclature.nomenclature_dialog import NomenclatureDialog
from requests_app.request_category_dialog import RequestCategoryDialog
from accept_app.accept_dialog import AcceptDialog


class RequestWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.id = None
        self.ui = Ui_Request()
        self.ui.setupUi(self)
        self.ui.delete_btn.hide()
        self.ui.mark_done_btn.hide()
        self.ui.send_btn.hide()
        self.ui.accept_viewer_btn.hide()
        self.ui.date_lbl.setText("--.--.----")
        self.ui.status_lbl.setText("---------")
        self.setup_category_combobox()

        self.ui.tableWidget.hideColumn(0)

        if not self.parent.purchaser:
            self.ui.category_dialog_btn.hide()
            self.ui.mark_done_btn.hide()

        self.ui.add_nomenclature_btn.clicked.connect(self.open_nomenclature_dialog)
        self.ui.delete_nomenclature_btn.clicked.connect(self.delete_nomenclature_row)
        self.ui.save_btn.clicked.connect(self.save_request)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)
        self.ui.delete_btn.clicked.connect(self.delete_request)
        self.ui.category_dialog_btn.clicked.connect(self.open_category_dialog)
        self.ui.send_btn.clicked.connect(self.open_accept_dialog)
        self.ui.mark_done_btn.clicked.connect(self.mark_done)
        self.ui.accept_viewer_btn.clicked.connect(lambda: parent.open_accept_request_viewer(self.id))

    def setup_category_combobox(self):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        categories = cur.execute("SELECT name FROM Request_category").fetchall()
        con.close()
        self.ui.category_combobox.clear()
        categories = list(map(lambda x: x[0], categories))
        self.ui.category_combobox.insertItems(0, categories)

    def open_category_dialog(self):
        dialog = RequestCategoryDialog(self.parent)
        if dialog.exec() == QDialog.Accepted:
            self.setup_category_combobox()
            if dialog.category:
                self.ui.category_combobox.setCurrentText(dialog.category)

    def open_nomenclature_dialog(self):
        dialog = NomenclatureDialog(self.parent)
        if dialog.exec() == QDialog.Accepted:
            if dialog.nomenclature_id:
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

    def set_is_created(self, id):
        self.ui.save_btn.clicked.disconnect()
        self.ui.save_btn.clicked.connect(self.update_request)
        self.id = id
        self.ui.delete_btn.show()
        self.ui.send_btn.show()
        self.ui.accept_viewer_btn.show()
        if self.parent.purchaser:
            self.ui.mark_done_btn.show()

    def set_uneditable_fields(self, date, status):
        self.ui.date_lbl.setText(date.split(".")[0])
        self.ui.status_lbl.setText(status)

    def check_and_return_editable_fields(self):
        description = self.ui.description_text.toPlainText()
        rows = self.ui.tableWidget.rowCount()
        amounts = [self.ui.tableWidget.item(row, 3) for row in range(rows)]
        item_ids = None

        if not description:
            QMessageBox.warning(self, "Предупреждение", "Вы не заполнили описание")
        elif not rows:
            QMessageBox.warning(self, "Предупреждение", "Вы не добавили номенклатуру")
        elif not all(amounts):
            QMessageBox.warning(self, "Предупреждение", "Вы не указали `Количество` у некоторых позиций")
        else:
            amounts = map(lambda item: item.text(), amounts)
            item_ids = [self.ui.tableWidget.item(row, 0).text() for row in range(rows)]

        return description, rows, amounts, item_ids

    def save_request(self):
        description, rows, amounts, item_ids = self.check_and_return_editable_fields()
        if not (description and rows and all(amounts)):
            return
        category_name = self.ui.category_combobox.currentText()
        
        created_at = dt.datetime.now()
        status = "Не согласовано"
        user_id = self.parent.user_id

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        category_id = cur.execute("SELECT id FROM Request_category WHERE name=?", (category_name, )).fetchone()[0]
        try:
            cur.execute("INSERT INTO Requests(description, created_at, status, category_id, initiator_id) VALUES (?, ?, ?, ?, ?);", 
                        (description, created_at, status, category_id, user_id))
        except sqlite3.Error as err:
            QMessageBox.critical(self, "Неизвестная ошибка", str(err))
        
        request_id = cur.lastrowid
        request_ids = [str(request_id)] * rows

        cur.executemany("INSERT INTO Request_items(amount, request_id, item_id) VALUES (?, ?, ?);", 
                        zip(amounts, request_ids, item_ids))
        con.commit()
        con.close()

        self.parent.tab_widget.setTabText(self.parent.tab_widget.currentIndex(), f"Заявка {request_id}")
        self.set_is_created(request_id)
        self.set_uneditable_fields(str(created_at), status)
        self.parent.status_bar.showMessage("Заявка успешно сохранена", 3000)

    def update_request(self):
        description, rows, amounts, item_ids = self.check_and_return_editable_fields()
        if not (description and rows and amounts):
            return
        category_name = self.ui.category_combobox.currentText()
        
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        category_id = cur.execute("SELECT id FROM Request_category WHERE name=?", (category_name, )).fetchone()[0]
        try:
            cur.execute("UPDATE Requests SET description=?, category_id=? WHERE id=?;", (description, category_id, self.id))
        except sqlite3.OperationalError as err:
            QMessageBox.critical(self, "Неизвестная ошибка", str(err))
        
        request_ids = [str(self.id)] * rows

        cur.execute("DELETE FROM Request_items WHERE request_id=?", (self.id,))
        cur.executemany("INSERT INTO Request_items(amount, request_id, item_id) VALUES (?, ?, ?);", 
                        zip(amounts, request_ids, item_ids))
        con.commit()
        con.close()
        self.parent.status_bar.showMessage("Заявка успешно сохранена", 3000)


    def load_request_data(self, request_id):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        
        # Получаем основную информацию о заявке
        request = cur.execute("""
                              SELECT 
                                Requests.description, 
                                Requests.created_at, 
                                Requests.status, 
                                Request_category.name 
                              FROM Requests 
                              LEFT JOIN Request_category ON Requests.category_id=Request_category.id 
                              WHERE Requests.id = ?;""", (request_id,)).fetchone()
        if request:
            self.ui.description_text.setPlainText(request[0])
            self.ui.category_combobox.setCurrentText(request[3])
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

    def delete_request(self):
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
        self.parent.status_bar.showMessage("Заявка успешно удалена", 3000)

    def open_accept_dialog(self):
        if not self.id:
            ans = QMessageBox.warning(self, "Предупреждение", "Для продолжения необходимо сохранить объект")
            if ans == QMessageBox.Ok:
                self.save_request()
            else:
                return
        dialog = AcceptDialog(self.parent)
        if dialog.exec() == QDialog.Accepted:
            approval_status = "Не согласовано"
            con = sqlite3.connect(self.parent.database_file)
            cur = con.cursor()

            max_stage = cur.execute("SELECT MAX(stage_order) FROM Request_approvals_stages WHERE request_id=?;", (self.id,)).fetchone()[0]
            if not max_stage:
                max_stage = 0
            else:
                max_stage = int(max_stage) + 1

            for stage_order, acceptor_id in enumerate(dialog.accepted_users):
                cur.execute("""
                            INSERT INTO Request_approvals_stages(approval_status, stage_order, request_id, acceptor_id) 
                            VALUES (?, ?, ?, ?)
                            """, (approval_status, max_stage + stage_order if dialog.is_step_by_step else max_stage, self.id, acceptor_id))

            con.commit()
            con.close()
        if not dialog.accepted_users:
            self.parent.status_bar.showMessage("Не выбраны согласованты", 3000)
        else:
            self.parent.status_bar.showMessage("Заявка успешно отправлена на согласование", 3000)

    def mark_done(self):
        ans = QMessageBox(self, "Предупреждение", "Для продолжения необходимо сохранить объект")
        if ans == QMessageBox.Ok:
            self.save_request()
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        cur.execute("UPDATE Requests SET status=? WHERE id=?;", ("Выполнено", self.id))
        con.commit()
        con.close()

        self.parent.status_bar.showMessage("Заявка помечена как Выполнена", 3000)