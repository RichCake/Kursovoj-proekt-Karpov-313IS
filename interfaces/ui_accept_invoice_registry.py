# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accept_invoice_registry.ui'
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

class Ui_Accept_invoice_registry(object):
    def setupUi(self, Accept_invoice_registry):
        if not Accept_invoice_registry.objectName():
            Accept_invoice_registry.setObjectName(u"Accept_invoice_registry")
        Accept_invoice_registry.resize(757, 555)
        self.verticalLayout = QVBoxLayout(Accept_invoice_registry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.refresh_btn = QPushButton(Accept_invoice_registry)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.horizontalLayout.addWidget(self.refresh_btn)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(Accept_invoice_registry)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.invoice_list = QTableView(Accept_invoice_registry)
        self.invoice_list.setObjectName(u"invoice_list")

        self.horizontalLayout_2.addWidget(self.invoice_list)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.accept_btn = QPushButton(Accept_invoice_registry)
        self.accept_btn.setObjectName(u"accept_btn")

        self.horizontalLayout_3.addWidget(self.accept_btn)

        self.reject_btn = QPushButton(Accept_invoice_registry)
        self.reject_btn.setObjectName(u"reject_btn")

        self.horizontalLayout_3.addWidget(self.reject_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.lineEdit = QLineEdit(Accept_invoice_registry)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)


        self.retranslateUi(Accept_invoice_registry)

        self.accept_btn.setDefault(False)


        QMetaObject.connectSlotsByName(Accept_invoice_registry)
    # setupUi

    def retranslateUi(self, Accept_invoice_registry):
        Accept_invoice_registry.setWindowTitle(QCoreApplication.translate("Accept_invoice_registry", u"Form", None))
        self.refresh_btn.setText(QCoreApplication.translate("Accept_invoice_registry", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.close_btn.setText(QCoreApplication.translate("Accept_invoice_registry", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.accept_btn.setText(QCoreApplication.translate("Accept_invoice_registry", u"\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u0442\u044c", None))
        self.reject_btn.setText(QCoreApplication.translate("Accept_invoice_registry", u"\u041e\u0442\u043a\u043b\u043e\u043d\u0438\u0442\u044c", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Accept_invoice_registry", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439...", None))
    # retranslateUi

