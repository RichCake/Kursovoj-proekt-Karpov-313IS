from PySide6.QtWidgets import QWidget, QTableView
from PySide6.QtSql import QSqlRelationalTableModel, QSqlRelation

from interfaces.ui_request_registry import Ui_Request_registry
from requests_app.models import DateDelegate


class InvoiceRegistryWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Request_registry()
        self.ui.setupUi(self)

        self.model = QSqlRelationalTableModel()
        self.model.setTable("Invoice")
        self.model.setRelation(4, QSqlRelation("Vendor_managers", "id", "second_name"))
        self.model.setRelation(5, QSqlRelation("Users", "id", "login"))
        self.model.select()

        self.ui.request_list.setModel(self.model)
        self.ui.request_list.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)
        self.ui.request_list.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.request_list.hideColumn(0)
        date_delegate = DateDelegate()
        self.ui.request_list.setItemDelegateForColumn(3, date_delegate)
        self.ui.request_list.resizeColumnsToContents()

        self.ui.open_menu_btn.clicked.connect(parent.open_menu)
        self.ui.request_list.doubleClicked.connect(self.open_invoice_details)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)
        self.ui.refresh_btn.clicked.connect(self.refresh_values)

    def open_invoice_details(self, index):
        # Получаем ID заявки из модели, например, из первой колонки
        invoice_id = self.ui.request_list.model().data(self.ui.request_list.model().index(index.row(), 0))
        # self.parent.open_request_creation_with_data(invoice_id)

    def refresh_values(self):
        self.model.select()
        self.ui.request_list.reset()