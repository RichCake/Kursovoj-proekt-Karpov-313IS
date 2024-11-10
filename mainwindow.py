from pathlib import Path
import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget
from PySide6.QtSql import QSqlDatabase

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic menu.ui -o ui_form.py, or
#     pyside2-uic menu.ui -o ui_form.py
from interfaces.ui_mainwindow import Ui_MainWindow
from interfaces.ui_menu import Ui_Menu
from requests_app.create_request_widget import CreateRequestWidget
from requests_app.request_registry_widget import RequestRegistryWidget
from invoices.invoice_registry_widget import InvoiceRegistryWidget


BASE_DIR = Path(__file__).resolve().parent


class MenuWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)

        self.ui.invoice_registry_btn.clicked.connect(parent.open_invoice_registry)
        self.ui.create_request_btn.clicked.connect(parent.open_request_creation)
        self.ui.request_registry_btn.clicked.connect(parent.open_request_registry)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.database_file = os.path.join(BASE_DIR, "database.db")
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("database.db")
        self.db.open()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.menu_widget = MenuWidget(self)
        self.invoice_registry_widget = InvoiceRegistryWidget(self)
        self.request_creation_widget = CreateRequestWidget(self)
        self.request_registry_widget = RequestRegistryWidget(self)

        self.stacked_widget.addWidget(self.menu_widget)
        self.stacked_widget.addWidget(self.invoice_registry_widget)
        self.stacked_widget.addWidget(self.request_creation_widget)
        self.stacked_widget.addWidget(self.request_registry_widget)

    def open_request_creation(self):
        self.stacked_widget.setCurrentWidget(self.request_creation_widget)

    def open_request_registry(self):
        self.stacked_widget.setCurrentWidget(self.request_registry_widget)

    def open_invoice_registry(self):
        self.stacked_widget.setCurrentWidget(self.invoice_registry_widget)

    def open_menu(self):
        self.stacked_widget.setCurrentWidget(self.menu_widget)

    def open_request_creation_with_data(self, request_id):
        # Устанавливаем виджет создания заявки как активный
        self.stacked_widget.setCurrentWidget(self.request_creation_widget)
        
        # Загружаем данные из базы данных и заполняем виджет
        self.request_creation_widget.load_request_data(request_id)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())