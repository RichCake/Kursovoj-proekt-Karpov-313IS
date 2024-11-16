from PySide6.QtWidgets import QWidget, QTableView
from PySide6.QtSql import QSqlRelationalTableModel

from interfaces.ui_user_registry_widget import Ui_User_registry


class UserRegistryWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_User_registry()
        self.ui.setupUi(self)

        self.model = QSqlRelationalTableModel()
        self.model.setTable("Users")
        self.model.select()

        self.ui.user_list.setModel(self.model)
        self.ui.user_list.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)
        self.ui.user_list.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.user_list.hideColumn(0)
        self.ui.user_list.hideColumn(6)
        self.ui.user_list.resizeColumnsToContents()

        self.ui.user_list.doubleClicked.connect(self.open_user_details)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)
        self.ui.refresh_btn.clicked.connect(self.refresh_values)
        self.ui.create_btn.clicked.connect(parent.open_user_creation)

    def refresh_values(self):
        self.model.select()
        self.ui.user_list.reset()

    def open_user_details(self, index):
        user_id = self.ui.user_list.model().data(self.ui.user_list.model().index(index.row(), 0))
        self.parent.open_user_creation_with_data(user_id)