import sys
import sqlite3

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic menu.ui -o ui_form.py, or
#     pyside2-uic menu.ui -o ui_form.py
from interfaces.ui_mainwindow import Ui_MainWindow
from interfaces.ui_menu import Ui_Menu
from interfaces.ui_invoice_registry import Ui_Invoice_registry


class InvoiceRegistryWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Invoice_registry()
        self.ui.setupUi(self)

        self.ui.open_menu_btn.clicked.connect(parent.open_menu)


class MenuWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)

        self.ui.invoice_registry_btn.clicked.connect(parent.open_invoice_registry)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.menu_widget = MenuWidget(self)
        self.invoice_registry_widget = InvoiceRegistryWidget(self)

        self.stacked_widget.addWidget(self.menu_widget)
        self.stacked_widget.addWidget(self.invoice_registry_widget)

    def open_invoice_registry(self):
        self.stacked_widget.setCurrentWidget(self.invoice_registry_widget)

    def open_menu(self):
        self.stacked_widget.setCurrentWidget(self.menu_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())