# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_registry_widget.ui'
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

class Ui_User_registry(object):
    def setupUi(self, User_registry):
        if not User_registry.objectName():
            User_registry.setObjectName(u"User_registry")
        User_registry.resize(534, 381)
        self.verticalLayout = QVBoxLayout(User_registry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.refresh_btn = QPushButton(User_registry)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.horizontalLayout.addWidget(self.refresh_btn)

        self.create_btn = QPushButton(User_registry)
        self.create_btn.setObjectName(u"create_btn")

        self.horizontalLayout.addWidget(self.create_btn)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(User_registry)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.user_list = QTableView(User_registry)
        self.user_list.setObjectName(u"user_list")

        self.verticalLayout.addWidget(self.user_list)


        self.retranslateUi(User_registry)

        QMetaObject.connectSlotsByName(User_registry)
    # setupUi

    def retranslateUi(self, User_registry):
        User_registry.setWindowTitle(QCoreApplication.translate("User_registry", u"Form", None))
        self.refresh_btn.setText(QCoreApplication.translate("User_registry", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.create_btn.setText(QCoreApplication.translate("User_registry", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.close_btn.setText(QCoreApplication.translate("User_registry", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

