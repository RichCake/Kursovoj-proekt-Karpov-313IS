import sys
import sqlite3
import datetime as dt

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QDialog, QTableWidgetItem

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic menu.ui -o ui_form.py, or
#     pyside2-uic menu.ui -o ui_form.py
from interfaces.ui_mainwindow import Ui_MainWindow
from interfaces.ui_menu import Ui_Menu
from interfaces.ui_invoice_registry import Ui_Invoice_registry
from interfaces.ui_nomenclature_dialog import Ui_Nomenclature_dialog
from interfaces.ui_create_request import Ui_Create_request


class NomenclatureDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Nomenclature_dialog()
        self.ui.setupUi(self)

        self.database_file = parent.database_file

        con = sqlite3.connect(parent.database_file)
        cur = con.cursor()
        nomenclatures = cur.execute("SELECT * FROM Nomenclature").fetchall()
        con.close()

        self.ui.tableWidget.setRowCount(len(nomenclatures))
        for i, nomenclature in enumerate(nomenclatures):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(nomenclature[1]))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(nomenclature[2]))

        self.ui.pushButton.clicked.connect(self.add_nomenclature)
        self.ui.buttonBox.accepted.connect(self.select_nomenclature)

    def add_nomenclature(self):
        new_name = self.ui.lineEdit.text().strip()
        new_unit = self.ui.lineEdit_2.text().strip()
        if new_name and new_unit:
            con = sqlite3.connect(self.database_file)
            cur = con.cursor()
            cur.execute("INSERT INTO Nomenclature (name, unit) VALUES (?, ?)", (new_name, new_unit))
            con.commit()
            con.close()
            rows = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(rows + 1)
            self.ui.tableWidget.setItem(rows, 0, QTableWidgetItem(new_name))
            self.ui.tableWidget.setItem(rows, 1, QTableWidgetItem(new_unit))
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()

    def select_nomenclature(self):
        row = self.ui.tableWidget.currentRow()
        selected_name = self.ui.tableWidget.item(row, 0)
        selected_unit = self.ui.tableWidget.item(row, 1)
        if selected_name and selected_unit:
            self.selected_name = selected_name.text()
            self.selected_unit = selected_unit.text()
            self.accept()


class CreateRequestWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Create_request()
        self.ui.setupUi(self)

        self.ui.add_nomenclature_btn.clicked.connect(self.open_nomenclature_dialog)
        self.ui.save_btn.clicked.connect(self.save_request)
        self.ui.menu_btn.clicked.connect(parent.open_menu)

    def open_nomenclature_dialog(self):
        dialog = NomenclatureDialog(self.parent)
        if dialog.exec() == QDialog.Accepted:
            rows = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(rows + 1)
            self.ui.tableWidget.setItem(rows, 0, QTableWidgetItem(dialog.selected_name))
            self.ui.tableWidget.setItem(rows, 1, QTableWidgetItem(dialog.selected_unit))

    def save_request(self):
        descroption = self.ui.description_text.text()
        crated_at = dt.datetime.now()
        status = "Не согласовано"

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        cur.execute("INSERT INTO Requests(description, created_at, status) VALUES (?, ?, ?);", (descroption, crated_at, status))

        con.commit()
        con.close()


class InvoiceRegistryWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Invoice_registry()
        self.ui.setupUi(self)

        con = sqlite3.connect(parent.database_file)
        cur = con.cursor()
        invoice_list = cur.execute("SELECT * FROM Invoice").fetchall()
        for invoice in invoice_list:
            self.ui.invoice_list.addItem(str(invoice))
        con.close()

        self.ui.open_menu_btn.clicked.connect(parent.open_menu)


class MenuWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)

        self.ui.invoice_registry_btn.clicked.connect(parent.open_invoice_registry)
        self.ui.create_request_btn.clicked.connect(parent.open_request_creation)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.database_file = "database.db"

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.menu_widget = MenuWidget(self)
        self.invoice_registry_widget = InvoiceRegistryWidget(self)
        self.request_creation_widget = CreateRequestWidget(self)

        self.stacked_widget.addWidget(self.menu_widget)
        self.stacked_widget.addWidget(self.invoice_registry_widget)
        self.stacked_widget.addWidget(self.request_creation_widget)

    def open_request_creation(self):
        self.stacked_widget.setCurrentWidget(self.request_creation_widget)

    def open_invoice_registry(self):
        self.stacked_widget.setCurrentWidget(self.invoice_registry_widget)

    def open_menu(self):
        self.stacked_widget.setCurrentWidget(self.menu_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())