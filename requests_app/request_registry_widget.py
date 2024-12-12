import sqlite3

from PyQt6.QtSql import QSqlRelation, QSqlRelationalTableModel
from PyQt6.QtWidgets import QAbstractItemView, QTableView, QWidget

from interfaces.ui_request_registry import Ui_Request_registry
from utils.models import DateDelegate


class RequestRegistryWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Request_registry()
        self.ui.setupUi(self)

        self.model = QSqlRelationalTableModel()
        self.model.setTable("Requests")
        self.model.setRelation(4, QSqlRelation("Request_category", "id", "name"))
        self.model.setRelation(5, QSqlRelation("Users", "id", "login"))
        if not self.parent.purchaser:
            self.model.setFilter(f"initiator_id={self.parent.user_id}")
        self.model.select()

        self.ui.request_list.setModel(self.model)
        self.ui.request_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.request_list.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.request_list.hideColumn(0)
        self.ui.request_list.hideColumn(0)
        date_delegate = DateDelegate()
        self.ui.request_list.setItemDelegateForColumn(2, date_delegate)
        self.ui.request_list.resizeColumnsToContents()

        self.setup_category_combobox()

        self.ui.request_list.doubleClicked.connect(self.open_request_details)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)
        self.ui.refresh_btn.clicked.connect(self.refresh_values)
        self.ui.create_btn.clicked.connect(parent.open_request_creation)
        self.ui.category_combobox.currentTextChanged.connect(self.filter_list)
        self.ui.comboBox.currentTextChanged.connect(self.filter_list)

    def filter_list(self):
        category_name = self.ui.category_combobox.currentText()
        status_name = self.ui.comboBox.currentText()

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()

        if category_name == "-" and status_name == "-":
            if not self.parent.purchaser:
                self.model.setFilter(f"initiator_id={self.parent.user_id}")
            else:
                self.model.setFilter("")
            return
        elif status_name == "-":
            category_id = cur.execute("SELECT id FROM Request_category WHERE name=?", (category_name,)).fetchone()[0]
            if not self.parent.purchaser:
                self.model.setFilter(f"category_id={category_id} AND initiator_id={self.parent.user_id}")
            else:
                self.model.setFilter(f"category_id={category_id}")
        elif category_name == "-":
            if not self.parent.purchaser:
                self.model.setFilter(f"status='{status_name}' AND initiator_id={self.parent.user_id}")
            else:
                self.model.setFilter(f"status='{status_name}'")
        else:
            category_id = cur.execute("SELECT id FROM Request_category WHERE name=?", (category_name,)).fetchone()[0]
            if not self.parent.purchaser:
                self.model.setFilter(f"category_id={category_id} AND status='{status_name}' AND initiator_id={self.parent.user_id}")
            else:
                self.model.setFilter(f"category_id={category_id} AND status='{status_name}'")

        con.close()
        self.refresh_values()

    def setup_category_combobox(self):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        categories = cur.execute("SELECT name FROM Request_category").fetchall()
        con.close()
        self.ui.category_combobox.clear()
        categories = list(map(lambda x: x[0], categories))
        self.ui.category_combobox.insertItems(0, categories)
        self.ui.category_combobox.insertItem(0, "-")
        self.ui.category_combobox.setCurrentIndex(0)

    def open_request_details(self, index):
        # Получаем ID заявки из модели, например, из первой колонки
        request_id = self.ui.request_list.model().data(self.ui.request_list.model().index(index.row(), 0))
        self.parent.open_request_creation_with_data(request_id)

    def refresh_values(self):
        self.model.select()
        self.ui.request_list.reset()