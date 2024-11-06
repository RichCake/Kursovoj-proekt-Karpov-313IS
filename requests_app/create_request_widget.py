import sqlite3
import datetime as dt

from PySide6.QtWidgets import QWidget, QDialog, QTableWidgetItem

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
        self.nomenclature_list = []
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

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        cur.execute("INSERT INTO Requests(description, created_at, status) VALUES (?, ?, ?);", 
                    (description, created_at, status))
        request_id = cur.lastrowid

        rows = self.ui.tableWidget.rowCount()
        amounts = [self.ui.tableWidget.item(row, 3).text() for row in range(rows)]
        request_ids = [str(request_id)] * rows  # Создаем список с ID заявки
        item_ids = [self.ui.tableWidget.item(row, 0).text() for row in range(rows)]

        cur.executemany("INSERT INTO Request_items(amount, request_id, item_id) VALUES (?, ?, ?);", 
                        zip(amounts, request_ids, item_ids))
        con.commit()
        con.close()