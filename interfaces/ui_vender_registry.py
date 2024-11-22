# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vender_registry.ui'
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

class Ui_VenderRegistry(object):
    def setupUi(self, VenderRegistry):
        if not VenderRegistry.objectName():
            VenderRegistry.setObjectName(u"VenderRegistry")
        VenderRegistry.resize(560, 421)
        self.verticalLayout = QVBoxLayout(VenderRegistry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.refresh_btn = QPushButton(VenderRegistry)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.horizontalLayout.addWidget(self.refresh_btn)

        self.create_btn = QPushButton(VenderRegistry)
        self.create_btn.setObjectName(u"create_btn")

        self.horizontalLayout.addWidget(self.create_btn)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(VenderRegistry)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(VenderRegistry)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(VenderRegistry)

        QMetaObject.connectSlotsByName(VenderRegistry)
    # setupUi

    def retranslateUi(self, VenderRegistry):
        VenderRegistry.setWindowTitle(QCoreApplication.translate("VenderRegistry", u"Form", None))
        self.refresh_btn.setText(QCoreApplication.translate("VenderRegistry", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.create_btn.setText(QCoreApplication.translate("VenderRegistry", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.close_btn.setText(QCoreApplication.translate("VenderRegistry", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VenderRegistry", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VenderRegistry", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VenderRegistry", u"\u0410\u0434\u0440\u0435\u0441", None));
    # retranslateUi

