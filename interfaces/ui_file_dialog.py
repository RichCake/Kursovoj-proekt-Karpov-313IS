# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_dialog.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_FileDialog(object):
    def setupUi(self, FileDialog):
        if not FileDialog.objectName():
            FileDialog.setObjectName(u"FileDialog")
        FileDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(FileDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(FileDialog)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_4)

        self.filename_lbl = QLabel(FileDialog)
        self.filename_lbl.setObjectName(u"filename_lbl")

        self.horizontalLayout.addWidget(self.filename_lbl)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.attach_file = QPushButton(FileDialog)
        self.attach_file.setObjectName(u"attach_file")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailAttachment))
        self.attach_file.setIcon(icon)

        self.verticalLayout.addWidget(self.attach_file)

        self.delete_file = QPushButton(FileDialog)
        self.delete_file.setObjectName(u"delete_file")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.delete_file.setIcon(icon1)

        self.verticalLayout.addWidget(self.delete_file)

        self.open_file = QPushButton(FileDialog)
        self.open_file.setObjectName(u"open_file")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.open_file.setIcon(icon2)

        self.verticalLayout.addWidget(self.open_file)

        self.buttonBox = QDialogButtonBox(FileDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(FileDialog)

        QMetaObject.connectSlotsByName(FileDialog)
    # setupUi

    def retranslateUi(self, FileDialog):
        FileDialog.setWindowTitle(QCoreApplication.translate("FileDialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("FileDialog", u"\u0424\u0430\u0439\u043b:", None))
        self.filename_lbl.setText("")
        self.attach_file.setText(QCoreApplication.translate("FileDialog", u"\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.delete_file.setText(QCoreApplication.translate("FileDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.open_file.setText(QCoreApplication.translate("FileDialog", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
    # retranslateUi

