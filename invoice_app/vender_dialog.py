import sqlite3

from PySide6.QtWidgets import QDialog, QListWidgetItem, QMessageBox

from interfaces.ui_vender_dialog import Ui_Vender_dialog


class VenderDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Vender_dialog()
        self.ui.setupUi(self)

        self.update_list()

        self.ui.add_btn.clicked.connect(self.add_vender)
        self.ui.buttonBox.accepted.connect(self.select_vender)

    def update_list(self):
        self.ui.listWidget.clear()
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        venders = cur.execute("SELECT id, name FROM Vendor;").fetchall()
        con.close()
        for vender in venders:
            QListWidgetItem(vender[1], self.ui.listWidget)

    def select_vender(self):
        self.vender = self.ui.listWidget.currentItem().text()
        self.accept()

    def add_vender(self):
        name = self.ui.name_edit.text()
        if name:
            try:
                con = sqlite3.connect(self.parent.database_file)
                cur = con.cursor()
                cur.execute("INSERT INTO Vendor(name) VALUES (?)", (name,))
                con.commit()
                con.close()
                self.update_list()
            except sqlite3.IntegrityError:
                QMessageBox.critical(self, "Ошибка", "Наименование уже присутствует в базе")
