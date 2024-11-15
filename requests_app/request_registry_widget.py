from PySide6.QtWidgets import QWidget, QTableView
from PySide6.QtSql import QSqlRelationalTableModel, QSqlRelation

from interfaces.ui_request_registry import Ui_Request_registry
from .models import DateDelegate


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
        self.model.select()

        self.ui.request_list.setModel(self.model)
        self.ui.request_list.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)
        self.ui.request_list.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.request_list.hideColumn(0)
        date_delegate = DateDelegate()
        self.ui.request_list.setItemDelegateForColumn(2, date_delegate)
        self.ui.request_list.resizeColumnsToContents()

        self.ui.open_menu_btn.clicked.connect(parent.open_menu)
        self.ui.request_list.doubleClicked.connect(self.open_request_details)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)
        self.ui.refresh_btn.clicked.connect(self.refresh_values)

    def open_request_details(self, index):
        # Получаем ID заявки из модели, например, из первой колонки
        request_id = self.ui.request_list.model().data(self.ui.request_list.model().index(index.row(), 0))
        self.parent.open_request_creation_with_data(request_id)

    def refresh_values(self):
        self.model.select()
        self.ui.request_list.reset()