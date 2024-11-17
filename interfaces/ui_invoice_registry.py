# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invoice_registry.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_Invoice_registry(object):
    def setupUi(self, Invoice_registry):
        if not Invoice_registry.objectName():
            Invoice_registry.setObjectName(u"Invoice_registry")
        Invoice_registry.resize(735, 507)
        self.verticalLayout = QVBoxLayout(Invoice_registry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.refresh_btn = QPushButton(Invoice_registry)
        self.refresh_btn.setObjectName(u"refresh_btn")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.refresh_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.refresh_btn)

        self.create_btn = QPushButton(Invoice_registry)
        self.create_btn.setObjectName(u"create_btn")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.create_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.create_btn)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(Invoice_registry)
        self.close_btn.setObjectName(u"close_btn")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.close_btn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Invoice_registry)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label)

        self.vender_combo_box = QComboBox(Invoice_registry)
        self.vender_combo_box.setObjectName(u"vender_combo_box")

        self.horizontalLayout_2.addWidget(self.vender_combo_box)

        self.label_2 = QLabel(Invoice_registry)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(Invoice_registry)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.invoice_list = QTableView(Invoice_registry)
        self.invoice_list.setObjectName(u"invoice_list")

        self.verticalLayout.addWidget(self.invoice_list)


        self.retranslateUi(Invoice_registry)

        QMetaObject.connectSlotsByName(Invoice_registry)
    # setupUi

    def retranslateUi(self, Invoice_registry):
        Invoice_registry.setWindowTitle(QCoreApplication.translate("Invoice_registry", u"Form", None))
        self.refresh_btn.setText("")
        self.create_btn.setText("")
        self.close_btn.setText(QCoreApplication.translate("Invoice_registry", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Invoice_registry", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442:", None))
        self.label_2.setText(QCoreApplication.translate("Invoice_registry", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Invoice_registry", u"-", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Invoice_registry", u"\u041d\u0435 \u0441\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u043d\u043e", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Invoice_registry", u"\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u043d\u043e", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Invoice_registry", u"\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u043e", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Invoice_registry", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))

    # retranslateUi

