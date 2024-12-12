import sqlite3

from PyQt6.QtWidgets import QDialog, QListWidgetItem, QMessageBox

from interfaces.ui_request_category_dialog import Ui_Request_category


class RequestCategoryDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Request_category()
        self.ui.setupUi(self)

        self.update_list()

        self.ui.add_btn.clicked.connect(self.add_category)
        self.ui.buttonBox.accepted.connect(self.select_category)

    def update_list(self):
        self.ui.category_list.clear()
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        categories = cur.execute("SELECT id, name FROM Request_category;").fetchall()
        con.close()
        for category in categories:
            QListWidgetItem(category[1], self.ui.category_list)

    def select_category(self):
        categories = self.ui.category_list.selectedItems()
        if len(categories) != 1:
            QMessageBox.warning(self, "Предупреждение", "Выберете одну категорию")
            return
        self.category = categories[0].text()
        self.accept()

    def add_category(self):
        name = self.ui.name_edit.text()
        if name:
            try:
                con = sqlite3.connect(self.parent.database_file)
                cur = con.cursor()
                cur.execute("INSERT INTO Request_category(name) VALUES (?)", (name,))
                con.commit()
                con.close()
                self.update_list()
            except sqlite3.IntegrityError as err:
                QMessageBox.critical(self, "Ошибка", "Наименование уже присутствует в базе")
