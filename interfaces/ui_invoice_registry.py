# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invoice_registry.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListView, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Invoice_registry(object):
    def setupUi(self, Invoice_registry):
        if not Invoice_registry.objectName():
            Invoice_registry.setObjectName(u"Invoice_registry")
        Invoice_registry.resize(567, 415)
        self.verticalLayout_2 = QVBoxLayout(Invoice_registry)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.open_menu_btn = QPushButton(Invoice_registry)
        self.open_menu_btn.setObjectName(u"open_menu_btn")

        self.horizontalLayout.addWidget(self.open_menu_btn)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listView = QListView(Invoice_registry)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)

        self.open_invoice_btn = QPushButton(Invoice_registry)
        self.open_invoice_btn.setObjectName(u"open_invoice_btn")

        self.verticalLayout.addWidget(self.open_invoice_btn)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Invoice_registry)

        QMetaObject.connectSlotsByName(Invoice_registry)
    # setupUi

    def retranslateUi(self, Invoice_registry):
        Invoice_registry.setWindowTitle(QCoreApplication.translate("Invoice_registry", u"Form", None))
        self.open_menu_btn.setText(QCoreApplication.translate("Invoice_registry", u"\u041c\u0435\u043d\u044e", None))
        self.open_invoice_btn.setText(QCoreApplication.translate("Invoice_registry", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u0447\u0435\u0442", None))
    # retranslateUi

