import datetime as dt
import os
import sqlite3
import sys
from pathlib import Path

import pandas as pd
from matplotlib.figure import Figure
from PyQt6.QtCore import QDateTime, QFile, Qt, QTextStream
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtSql import QSqlDatabase, QSqlRelation, QSqlRelationalTableModel
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QHBoxLayout,
    QLineEdit,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStyledItemDelegate,
    QTableView,
    QTableWidgetItem,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from accept_app.accept_dialog import AcceptDialog
from accept_app.accept_request_registry import AcceptRequestRegistry
from accept_app.accept_request_viewer import AcceptRequestWidget
from create_db import create_db
from interfaces.ui_accept_dialog import Ui_Accept_dialog
from interfaces.ui_accept_requests_registry import Ui_Accept_requests_registry
from interfaces.ui_accept_viewer import Ui_AcceptViewer
from interfaces.ui_auth_dialog import Ui_Auth_dialog
from interfaces.ui_create_request import Ui_Request
from interfaces.ui_mainwindow import Ui_MainWindow
from interfaces.ui_nomenclature_dialog import Ui_Nomenclature_dialog
from interfaces.ui_request_category_dialog import Ui_Request_category
from interfaces.ui_request_registry import Ui_Request_registry
from interfaces.ui_user_registry_widget import Ui_User_registry
from interfaces.ui_user_widget import Ui_User_widget
from nomenclature.nomenclature_dialog import NomenclatureDialog
from reports.reports_widget import Report1, Report2, Report3, Report4, ReportWidget
from requests_app.request_category_dialog import RequestCategoryDialog
from requests_app.request_registry_widget import RequestRegistryWidget
from requests_app.request_widget import RequestWidget
from users.user_registry_widget import UserRegistryWidget
from users.user_widget import UserWidget
from utils.models import DateDelegate, ReadOnlyDelegate


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


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
        self.database_file = resource_path("database.db")
        if not os.path.isfile(self.database_file):
            create_db(self.database_file)
        dialog = AuthDialog(self)
        if dialog.exec():
            self.user_login = dialog.user
            self.purchaser = dialog.purchaser
            self.user_id = dialog.id
        else:
            sys.exit()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.database_file)
        self.db.open()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.status_bar = self.statusBar()

        if not self.purchaser:
            self.ui.groupBox_3.hide()
            self.ui.groupBox_4.hide()

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabBarAutoHide(False)
        self.tab_widget.setTabsClosable(True)
        self.ui.horizontalLayout.addWidget(self.tab_widget)

        self.tab_widget.tabCloseRequested.connect(lambda i: self.tab_widget.removeTab(i))
        self.ui.create_request_btn.clicked.connect(self.open_request_creation)
        self.ui.request_registry_btn.clicked.connect(self.open_request_registry)
        self.ui.user_registry_btn.clicked.connect(self.open_user_registry)
        self.ui.accept_request_btn.clicked.connect(self.open_accept_request_registry)
        self.ui.reports_btn.clicked.connect(self.open_reports_widget)
        self.ui.exit_btn.clicked.connect(self.exit_app)

    def exit_app(self):
        ans = QMessageBox.warning(self, "Предупреждение", "Вы хотите выйти из приложения?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if ans == QMessageBox.StandardButton.Yes:
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

    def open_reports_widget(self):
        w = ReportWidget(self)
        self.tab_widget.addTab(w, "Отчеты")
        self.tab_widget.setCurrentWidget(w)

    def open_report1_widget(self):
        w = Report1(self)
        self.tab_widget.addTab(w, "Отчет")
        self.tab_widget.setCurrentWidget(w)

    def open_report2_widget(self):
        w = Report2(self)
        self.tab_widget.addTab(w, "Отчет")
        self.tab_widget.setCurrentWidget(w)

    def open_report3_widget(self):
        w = Report3(self)
        self.tab_widget.addTab(w, "Отчет")
        self.tab_widget.setCurrentWidget(w)

    def open_report4_widget(self):
        w = Report4(self)
        self.tab_widget.addTab(w, "Отчет")
        self.tab_widget.setCurrentWidget(w)

    def open_accept_request_viewer(self, request_id):
        w = AcceptRequestWidget(self, request_id)
        self.tab_widget.addTab(w, f"Согласование Заявки {request_id}")
        self.tab_widget.setCurrentWidget(w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    try:
        File = open(resource_path("style.qss"),"r")
        with File:
            qss = File.read()
            app.setStyleSheet(qss)
    except FileNotFoundError as ex:
        print("Файл со стилями не найден:", str(ex))

    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())