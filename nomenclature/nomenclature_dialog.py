import sqlite3

from PySide6.QtWidgets import QDialog, QTableWidgetItem, QTableView

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic menu.ui -o ui_form.py, or
#     pyside2-uic menu.ui -o ui_form.py
from interfaces.ui_nomenclature_dialog import Ui_Nomenclature_dialog


class NomenclatureDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Nomenclature_dialog()
        self.ui.setupUi(self)
        self.update_list()

        self.ui.tableWidget.hideColumn(0)
        self.ui.tableWidget.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)

        self.ui.pushButton.clicked.connect(self.add_nomenclature)
        self.ui.buttonBox.accepted.connect(self.select_nomenclature)

    def update_list(self):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        nomenclatures = cur.execute("SELECT * FROM Nomenclature").fetchall()
        con.close()

        self.ui.tableWidget.setRowCount(len(nomenclatures))
        for i, nomenclature in enumerate(nomenclatures):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(nomenclature[0])))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(nomenclature[1]))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(nomenclature[2]))

    def add_nomenclature(self):
        new_name = self.ui.lineEdit.text().strip()
        new_unit = self.ui.lineEdit_2.text().strip()
        if new_name and new_unit:
            con = sqlite3.connect(self.parent.database_file)
            cur = con.cursor()
            cur.execute("INSERT INTO Nomenclature (name, unit) VALUES (?, ?)", (new_name, new_unit))
            con.commit()
            con.close()
            self.update_list()
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()

    def select_nomenclature(self):
        row = self.ui.tableWidget.currentRow()
        nomenclature_id = self.ui.tableWidget.item(row, 0).text()
        if nomenclature_id:
            self.nomenclature_id = nomenclature_id
            self.accept()