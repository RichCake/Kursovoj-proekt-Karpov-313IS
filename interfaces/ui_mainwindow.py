# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(798, 594)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.accept_request_btn.sizePolicy().hasHeightForWidth())
        self.accept_request_btn.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.accept_request_btn)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.invoice_registry_btn = QPushButton(self.groupBox)
        self.invoice_registry_btn.setObjectName(u"invoice_registry_btn")

        self.verticalLayout_4.addWidget(self.invoice_registry_btn)

        self.create_invoice_btn = QPushButton(self.groupBox)
        self.create_invoice_btn.setObjectName(u"create_invoice_btn")

        self.verticalLayout_4.addWidget(self.create_invoice_btn)

        self.accept_invoice_btn = QPushButton(self.groupBox)
        self.accept_invoice_btn.setObjectName(u"accept_invoice_btn")

        self.verticalLayout_4.addWidget(self.accept_invoice_btn)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.user_registry_btn = QPushButton(self.groupBox_3)
        self.user_registry_btn.setObjectName(u"user_registry_btn")

        self.verticalLayout_5.addWidget(self.user_registry_btn)

        self.contract_registry_btn = QPushButton(self.groupBox_3)
        self.contract_registry_btn.setObjectName(u"contract_registry_btn")

        self.verticalLayout_5.addWidget(self.contract_registry_btn)

        self.vendor_btn = QPushButton(self.groupBox_3)
        self.vendor_btn.setObjectName(u"vendor_btn")

        self.verticalLayout_5.addWidget(self.vendor_btn)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.reports_btn = QPushButton(self.groupBox_4)
        self.reports_btn.setObjectName(u"reports_btn")

        self.verticalLayout_6.addWidget(self.reports_btn)


        self.verticalLayout.addWidget(self.groupBox_4)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 798, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \"\u041e\u0442\u0434\u0435\u043b \u0441\u043d\u0430\u0431\u0436\u0435\u043d\u0438\u044f\"", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u044f\u0432\u043a\u0438", None))
        self.request_registry_btn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0435\u0441\u0442\u0440 \u0437\u0430\u044f\u0432\u043e\u043a", None))
        self.create_request_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u044f\u0432\u043a\u0443", None))
        self.accept_request_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0447\u0435\u0442\u0430", None))
        self.invoice_registry_btn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0435\u0441\u0442\u0440 \u0441\u0447\u0435\u0442\u043e\u0432", None))
        self.create_invoice_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0441\u0447\u0435\u0442", None))
        self.accept_invoice_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u0442\u044c \u0441\u0447\u0435\u0442\u0430", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0421\u0418 ", None))
        self.user_registry_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.contract_registry_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b", None))
        self.vendor_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442\u044b", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.reports_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
    # retranslateUi

