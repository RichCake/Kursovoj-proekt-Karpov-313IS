# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accept_requests_registry.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_Accept_requests_registry(object):
    def setupUi(self, Accept_requests_registry):
        if not Accept_requests_registry.objectName():
            Accept_requests_registry.setObjectName(u"Accept_requests_registry")
        Accept_requests_registry.resize(682, 567)
        self.verticalLayout = QVBoxLayout(Accept_requests_registry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.refresh_btn = QPushButton(Accept_requests_registry)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.horizontalLayout.addWidget(self.refresh_btn)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(Accept_requests_registry)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.request_list = QTableView(Accept_requests_registry)
        self.request_list.setObjectName(u"request_list")

        self.horizontalLayout_2.addWidget(self.request_list)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lineEdit = QLineEdit(Accept_requests_registry)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.accept_btn = QPushButton(Accept_requests_registry)
        self.accept_btn.setObjectName(u"accept_btn")

        self.horizontalLayout_3.addWidget(self.accept_btn)

        self.reject_btn = QPushButton(Accept_requests_registry)
        self.reject_btn.setObjectName(u"reject_btn")

        self.horizontalLayout_3.addWidget(self.reject_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Accept_requests_registry)

        self.accept_btn.setDefault(False)


        QMetaObject.connectSlotsByName(Accept_requests_registry)
    # setupUi

    def retranslateUi(self, Accept_requests_registry):
        Accept_requests_registry.setWindowTitle(QCoreApplication.translate("Accept_requests_registry", u"Form", None))
        self.refresh_btn.setText(QCoreApplication.translate("Accept_requests_registry", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.close_btn.setText(QCoreApplication.translate("Accept_requests_registry", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Accept_requests_registry", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439...", None))
        self.accept_btn.setText(QCoreApplication.translate("Accept_requests_registry", u"\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u0442\u044c", None))
        self.reject_btn.setText(QCoreApplication.translate("Accept_requests_registry", u"\u041e\u0442\u043a\u043b\u043e\u043d\u0438\u0442\u044c", None))
    # retranslateUi

