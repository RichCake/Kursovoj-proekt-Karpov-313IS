from pathlib import Path
import sys
import os
import sqlite3

from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QDialog, QMessageBox
from PySide6.QtSql import QSqlDatabase

from interfaces.ui_mainwindow import Ui_MainWindow
from interfaces.ui_auth_dialog import Ui_Auth_dialog
from requests_app.request_widget import RequestWidget
from requests_app.request_registry_widget import RequestRegistryWidget
from requests_app.accept_request_registry import AcceptRequestRegistry
from users.user_registry_widget import UserRegistryWidget
from users.user_widget import UserWidget


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
        user = cur.execute("SELECT id, login, password, purchaser FROM Users WHERE login=? AND password=?;", (login, password)).fetchone()
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

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabBarAutoHide(False)
        self.tab_widget.setTabsClosable(True)
        self.ui.horizontalLayout.addWidget(self.tab_widget)

        self.tab_widget.tabCloseRequested.connect(lambda i: self.tab_widget.removeTab(i))
        self.ui.create_request_btn.clicked.connect(self.open_request_creation)
        self.ui.request_registry_btn.clicked.connect(self.open_request_registry)
        self.ui.user_registry_btn.clicked.connect(self.open_user_registry)
        self.ui.accept_request_btn.clicked.connect(self.open_accept_request_registry)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = MainWindow()
    ex.showFullScreen()
    sys.exit(app.exec())