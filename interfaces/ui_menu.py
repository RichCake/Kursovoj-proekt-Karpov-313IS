# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Menu(object):
    def setupUi(self, Menu):
        if not Menu.objectName():
            Menu.setObjectName(u"Menu")
        Menu.resize(548, 356)
        self.verticalLayout_3 = QVBoxLayout(Menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_3 = QGroupBox(Menu)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.user_registry_btn = QPushButton(self.groupBox_3)
        self.user_registry_btn.setObjectName(u"user_registry_btn")

        self.verticalLayout_5.addWidget(self.user_registry_btn)


        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.groupBox_4 = QGroupBox(Menu)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.groupBox_4.setCheckable(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.report_btn = QPushButton(self.groupBox_4)
        self.report_btn.setObjectName(u"report_btn")
        sizePolicy.setHeightForWidth(self.report_btn.sizePolicy().hasHeightForWidth())
        self.report_btn.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.report_btn)


        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Menu)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMouseTracking(False)
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.groupBox_2.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.request_registry_btn = QPushButton(self.groupBox_2)
        self.request_registry_btn.setObjectName(u"request_registry_btn")

        self.verticalLayout_2.addWidget(self.request_registry_btn)

        self.create_request_btn = QPushButton(self.groupBox_2)
        self.create_request_btn.setObjectName(u"create_request_btn")

        self.verticalLayout_2.addWidget(self.create_request_btn)

        self.accept_request_btn = QPushButton(self.groupBox_2)
        self.accept_request_btn.setObjectName(u"accept_request_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.accept_request_btn.sizePolicy().hasHeightForWidth())
        self.accept_request_btn.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.accept_request_btn)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.retranslateUi(Menu)

        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Menu", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.user_registry_btn.setText(QCoreApplication.translate("Menu", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Menu", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.report_btn.setText(QCoreApplication.translate("Menu", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Menu", u"\u0417\u0430\u044f\u0432\u043a\u0438", None))
        self.request_registry_btn.setText(QCoreApplication.translate("Menu", u"\u0420\u0435\u0435\u0441\u0442\u0440 \u0437\u0430\u044f\u0432\u043e\u043a", None))
        self.create_request_btn.setText(QCoreApplication.translate("Menu", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u044f\u0432\u043a\u0443", None))
        self.accept_request_btn.setText(QCoreApplication.translate("Menu", u"\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0438", None))
    # retranslateUi

