# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'request_registry.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_Request_registry(object):
    def setupUi(self, Request_registry):
        if not Request_registry.objectName():
            Request_registry.setObjectName(u"Request_registry")
        Request_registry.resize(529, 352)
        self.verticalLayout_2 = QVBoxLayout(Request_registry)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.open_menu_btn = QPushButton(Request_registry)
        self.open_menu_btn.setObjectName(u"open_menu_btn")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        self.open_menu_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.open_menu_btn)

        self.refresh_btn = QPushButton(Request_registry)
        self.refresh_btn.setObjectName(u"refresh_btn")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.refresh_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.refresh_btn)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(Request_registry)
        self.close_btn.setObjectName(u"close_btn")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.close_btn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.request_list = QTableView(Request_registry)
        self.request_list.setObjectName(u"request_list")

        self.verticalLayout.addWidget(self.request_list)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Request_registry)

        QMetaObject.connectSlotsByName(Request_registry)
    # setupUi

    def retranslateUi(self, Request_registry):
        Request_registry.setWindowTitle(QCoreApplication.translate("Request_registry", u"Form", None))
        self.open_menu_btn.setText("")
        self.refresh_btn.setText("")
        self.close_btn.setText(QCoreApplication.translate("Request_registry", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

