import sqlite3
import datetime as dt

from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem, QMessageBox
from PySide6.QtSql import QSqlTableModel

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic menu.ui -o ui_form.py, or
#     pyside2-uic menu.ui -o ui_form.py
from interfaces.ui_create_request import Ui_Create_request
from nomenclature.nomenclature_dialog import NomenclatureDialog


class CreateRequestWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Create_request()
        self.ui.setupUi(self)

        self.ui.add_nomenclature_btn.clicked.connect(self.open_nomenclature_dialog)
        self.ui.save_btn.clicked.connect(self.save_request)
        self.ui.menu_btn.clicked.connect(parent.open_menu)

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

    def save_request(self):
        description = self.ui.description_text.toPlainText()
        created_at = dt.datetime.now()
        status = "Не согласовано"
        rows = self.ui.tableWidget.rowCount()
        amounts = [self.ui.tableWidget.item(row, 3) for row in range(rows)]
        item_ids = [self.ui.tableWidget.item(row, 0).text() for row in range(rows)]

        if not description:
            QMessageBox.critical(self, "Ошибка", "Вы не заполнили описание")
            return
        elif not rows:
            QMessageBox.critical(self, "Ошибка", "Вы не добавили номенклатуру")
            return
        elif not all(amounts):
            QMessageBox.critical(self, "Ошибка", "Вы не указали `Количество` у некоторых позиций")
            return
        
        amounts = map(lambda item: item.text(), amounts)

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        cur.execute("INSERT INTO Requests(description, created_at, status) VALUES (?, ?, ?);", 
                    (description, created_at, status))
        
        request_id = cur.lastrowid
        request_ids = [str(request_id)] * rows

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
            # Отображаем другие данные, если необходимо

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