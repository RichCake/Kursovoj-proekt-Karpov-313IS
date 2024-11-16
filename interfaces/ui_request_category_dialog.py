# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'request_category_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Request_category(object):
    def setupUi(self, Request_category):
        if not Request_category.objectName():
            Request_category.setObjectName(u"Request_category")
        Request_category.resize(512, 347)
        self.verticalLayout = QVBoxLayout(Request_category)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.category_list = QListWidget(Request_category)
        self.category_list.setObjectName(u"category_list")
        self.category_list.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.category_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_edit = QLineEdit(Request_category)
        self.name_edit.setObjectName(u"name_edit")

        self.horizontalLayout.addWidget(self.name_edit)

        self.add_btn = QPushButton(Request_category)
        self.add_btn.setObjectName(u"add_btn")

        self.horizontalLayout.addWidget(self.add_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Request_category)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Request_category)
        self.buttonBox.accepted.connect(Request_category.accept)
        self.buttonBox.rejected.connect(Request_category.reject)

        QMetaObject.connectSlotsByName(Request_category)
    # setupUi

    def retranslateUi(self, Request_category):
        Request_category.setWindowTitle(QCoreApplication.translate("Request_category", u"Dialog", None))
        self.name_edit.setText("")
        self.name_edit.setPlaceholderText(QCoreApplication.translate("Request_category", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435...", None))
        self.add_btn.setText(QCoreApplication.translate("Request_category", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

