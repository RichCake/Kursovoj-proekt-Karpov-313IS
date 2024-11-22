import os
import sqlite3
import sys
from pathlib import Path

from PySide6.QtCore import QFile, QTextStream
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QTabWidget,
)

from create_db import create_db
from accept_app.accept_invoice_registry import AcceptInvoiceRegistry
from accept_app.accept_invoice_viewer import AcceptInvoiceWidget
from accept_app.accept_request_registry import AcceptRequestRegistry
from accept_app.accept_request_viewer import AcceptRequestWidget
from contracts_app.contract_widget import ContractWidget
from contracts_app.contracts_registry import ContractRegistry
from interfaces.ui_auth_dialog import Ui_Auth_dialog
from interfaces.ui_mainwindow import Ui_MainWindow
from invoice_app.invoice_registry_widget import InvoiceRegistryWidget
from invoice_app.invoice_widget import InvoiceWidget
from reports.reports_widget import ReportWidget
from requests_app.request_registry_widget import RequestRegistryWidget
from requests_app.request_widget import RequestWidget
from users.user_registry_widget import UserRegistryWidget
from users.user_widget import UserWidget
from vender_app.vender_registry import VenderRegistry
from vender_app.vender_widget import VenderWidget

BASE_DIR = Path(__file__).resolve().parent


class AuthDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Auth_dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.disconnect()
        self.ui.buttonBox.accepted.connect(self.set_current_user)

    def check_login_and_password(self, login, password):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        user = cur.execute("""
                           SELECT id, login, password, purchaser 
                           FROM Users 
                           WHERE login=? AND password=?;
                           """, (login, password)).fetchone()
        con.close()
        return user

    def set_current_user(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        user = self.check_login_and_password(login, password)
        if not user:
            QMessageBox.warning(self, "Предупреждение", "Неверный логин или пароль")
            return
        self.user = login
        self.purchaser = user[3]
        self.id = user[0]
        self.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.database_file = os.path.join(BASE_DIR, "database.db")
        if not os.path.isfile(self.database_file):
            create_db(self.database_file)
        dialog = AuthDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.user_login = dialog.user
            self.purchaser = dialog.purchaser
            self.user_id = dialog.id
        else:
            sys.exit()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("database.db")
        self.db.open()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.status_bar = self.statusBar()

        if not self.purchaser:
            self.ui.groupBox_3.hide()
            self.ui.groupBox_4.hide()
            self.ui.create_invoice_btn.hide()
            self.ui.invoice_registry_btn.hide()
            self.ui.contract_registry_btn.hide()

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabBarAutoHide(False)
        self.tab_widget.setTabsClosable(True)
        self.ui.horizontalLayout.addWidget(self.tab_widget)

        self.tab_widget.tabCloseRequested.connect(lambda i: self.tab_widget.removeTab(i))
        self.ui.create_request_btn.clicked.connect(self.open_request_creation)
        self.ui.request_registry_btn.clicked.connect(self.open_request_registry)
        self.ui.user_registry_btn.clicked.connect(self.open_user_registry)
        self.ui.accept_request_btn.clicked.connect(self.open_accept_request_registry)
        self.ui.create_invoice_btn.clicked.connect(self.open_invoice_creation)
        self.ui.invoice_registry_btn.clicked.connect(self.open_invoice_registry)
        self.ui.accept_invoice_btn.clicked.connect(self.open_accept_invoice_registry)
        self.ui.reports_btn.clicked.connect(self.open_reports_widget)
        self.ui.contract_registry_btn.clicked.connect(self.open_contract_registry)
        self.ui.vendor_btn.clicked.connect(self.open_vender_registry)
        self.ui.exit_btn.clicked.connect(self.exit_app)

    def exit_app(self):
        ans = QMessageBox.warning(self, "Предупреждение", "Вы хотите выйти из приложения?", QMessageBox.Yes | QMessageBox.No)
        if ans == QMessageBox.Yes:
            sys.exit()

    def open_request_creation(self):
        request_creation_widget = RequestWidget(self)
        self.tab_widget.addTab(request_creation_widget, "Создание заявки")
        self.tab_widget.setCurrentWidget(request_creation_widget)

    def open_request_registry(self):
        request_registry_widget = RequestRegistryWidget(self)
        self.tab_widget.addTab(request_registry_widget, "Реестр заявок")
        self.tab_widget.setCurrentWidget(request_registry_widget)

    def open_request_creation_with_data(self, request_id):
        request_creation_widget = RequestWidget(self)
        request_creation_widget.load_request_data(request_id)
        self.tab_widget.addTab(request_creation_widget, f"Заявка {request_id}")
        self.tab_widget.setCurrentWidget(request_creation_widget)

    def open_user_creation(self):
        user_creation_widget = UserWidget(self)
        self.tab_widget.addTab(user_creation_widget, "Создание пользователя")
        self.tab_widget.setCurrentWidget(user_creation_widget)

    def open_user_creation_with_data(self, user_id):
        user_creation_widget = UserWidget(self)
        user_creation_widget.load_data(user_id)
        self.tab_widget.addTab(user_creation_widget, f"Пользователь {user_id}")
        self.tab_widget.setCurrentWidget(user_creation_widget)

    def open_user_registry(self):
        request_registry_widget = UserRegistryWidget(self)
        self.tab_widget.addTab(request_registry_widget, "Реестр пользователей")
        self.tab_widget.setCurrentWidget(request_registry_widget)

    def close_current_tab(self):
        self.tab_widget.removeTab(self.tab_widget.currentIndex())

    def open_accept_request_registry(self):
        accept_request_registry_widget = AcceptRequestRegistry(self)
        self.tab_widget.addTab(accept_request_registry_widget, "Согласовать заявки")
        self.tab_widget.setCurrentWidget(accept_request_registry_widget)

    def open_invoice_registry(self):
        w = InvoiceRegistryWidget(self)
        self.tab_widget.addTab(w, "Реестр счетов")
        self.tab_widget.setCurrentWidget(w)

    def open_invoice_creation(self):
        w = InvoiceWidget(self)
        self.tab_widget.addTab(w, "Создание счета")
        self.tab_widget.setCurrentWidget(w)
    
    def open_invoice_creation_with_data(self, invoice_id):
        w = InvoiceWidget(self)
        w.load_invoice_data(invoice_id)
        self.tab_widget.addTab(w, f"Счет {invoice_id}")
        self.tab_widget.setCurrentWidget(w)

    def open_accept_invoice_registry(self):
        w = AcceptInvoiceRegistry(self)
        self.tab_widget.addTab(w, "Согласовать счета")
        self.tab_widget.setCurrentWidget(w)

    def open_reports_widget(self):
        w = ReportWidget(self)
        self.tab_widget.addTab(w, "Отчеты")
        self.tab_widget.setCurrentWidget(w)

    def open_contract_registry(self):
        w = ContractRegistry(self)
        self.tab_widget.addTab(w, "Реестр договоров")
        self.tab_widget.setCurrentWidget(w)

    def open_contract_creation(self):
        w = ContractWidget(self)
        self.tab_widget.addTab(w, "Создание договора")
        self.tab_widget.setCurrentWidget(w)

    def open_contract_with_data(self, contract_id):
        w = ContractWidget(self, contract_id)
        self.tab_widget.addTab(w, f"Договор {contract_id}")
        self.tab_widget.setCurrentWidget(w)

    def open_vender_registry(self):
        w = VenderRegistry(self)
        self.tab_widget.addTab(w, "Реестр контрагентов")
        self.tab_widget.setCurrentWidget(w)

    def open_vender_creation(self):
        w = VenderWidget(self)
        self.tab_widget.addTab(w, "Создание контрагента")
        self.tab_widget.setCurrentWidget(w)

    def open_vender_with_data(self, vender_id):
        w = VenderWidget(self, vender_id)
        self.tab_widget.addTab(w, f"Контрагент {vender_id}")
        self.tab_widget.setCurrentWidget(w)

    def open_accept_request_viewer(self, request_id):
        w = AcceptRequestWidget(self, request_id)
        self.tab_widget.addTab(w, f"Согласование Заявки {request_id}")
        self.tab_widget.setCurrentWidget(w)

    def open_accept_invoice_viewer(self, invoice_id):
        w = AcceptInvoiceWidget(self, invoice_id)
        self.tab_widget.addTab(w, f"Согласование Счета {invoice_id}")
        self.tab_widget.setCurrentWidget(w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    file = QFile("style.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    qss = QTextStream(file)
    app.setStyleSheet(qss.readAll())

    ex = MainWindow()
    ex.showFullScreen()
    sys.exit(app.exec())