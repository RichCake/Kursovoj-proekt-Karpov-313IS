# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contract_registry.ui'
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
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_ContractRegistry(object):
    def setupUi(self, ContractRegistry):
        if not ContractRegistry.objectName():
            ContractRegistry.setObjectName(u"ContractRegistry")
        ContractRegistry.resize(646, 387)
        self.verticalLayout = QVBoxLayout(ContractRegistry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.refresh_btn = QPushButton(ContractRegistry)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setAutoFillBackground(False)

        self.horizontalLayout_2.addWidget(self.refresh_btn)

        self.create_btn = QPushButton(ContractRegistry)
        self.create_btn.setObjectName(u"create_btn")

        self.horizontalLayout_2.addWidget(self.create_btn)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(ContractRegistry)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(ContractRegistry)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(ContractRegistry)

        QMetaObject.connectSlotsByName(ContractRegistry)
    # setupUi

    def retranslateUi(self, ContractRegistry):
        ContractRegistry.setWindowTitle(QCoreApplication.translate("ContractRegistry", u"Form", None))
        self.refresh_btn.setText(QCoreApplication.translate("ContractRegistry", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.create_btn.setText(QCoreApplication.translate("ContractRegistry", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.close_btn.setText(QCoreApplication.translate("ContractRegistry", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ContractRegistry", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ContractRegistry", u"\u041d\u043e\u043c\u0435\u0440", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ContractRegistry", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ContractRegistry", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442", None));
    # retranslateUi

