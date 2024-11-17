# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vender_dialog.ui'
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

class Ui_Vender_dialog(object):
    def setupUi(self, Vender_dialog):
        if not Vender_dialog.objectName():
            Vender_dialog.setObjectName(u"Vender_dialog")
        Vender_dialog.resize(558, 425)
        self.verticalLayout_2 = QVBoxLayout(Vender_dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget = QListWidget(Vender_dialog)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_edit = QLineEdit(Vender_dialog)
        self.name_edit.setObjectName(u"name_edit")

        self.horizontalLayout.addWidget(self.name_edit)

        self.address_edit = QLineEdit(Vender_dialog)
        self.address_edit.setObjectName(u"address_edit")

        self.horizontalLayout.addWidget(self.address_edit)

        self.add_btn = QPushButton(Vender_dialog)
        self.add_btn.setObjectName(u"add_btn")

        self.horizontalLayout.addWidget(self.add_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Vender_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Vender_dialog)
        self.buttonBox.accepted.connect(Vender_dialog.accept)
        self.buttonBox.rejected.connect(Vender_dialog.reject)

        QMetaObject.connectSlotsByName(Vender_dialog)
    # setupUi

    def retranslateUi(self, Vender_dialog):
        Vender_dialog.setWindowTitle(QCoreApplication.translate("Vender_dialog", u"Dialog", None))
        self.name_edit.setPlaceholderText(QCoreApplication.translate("Vender_dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435..", None))
        self.address_edit.setPlaceholderText(QCoreApplication.translate("Vender_dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441...", None))
        self.add_btn.setText(QCoreApplication.translate("Vender_dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

