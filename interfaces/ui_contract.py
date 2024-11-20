# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contract.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Contract(object):
    def setupUi(self, Contract):
        if not Contract.objectName():
            Contract.setObjectName(u"Contract")
        Contract.resize(671, 420)
        self.verticalLayout = QVBoxLayout(Contract)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.save_btn = QPushButton(Contract)
        self.save_btn.setObjectName(u"save_btn")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.save_btn.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.save_btn)

        self.delete_btn = QPushButton(Contract)
        self.delete_btn.setObjectName(u"delete_btn")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.delete_btn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.delete_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.close_btn = QPushButton(Contract)
        self.close_btn.setObjectName(u"close_btn")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.close_btn.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.label = QLabel(Contract)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(Contract)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(Contract)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(Contract)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.number_edit = QLineEdit(Contract)
        self.number_edit.setObjectName(u"number_edit")

        self.horizontalLayout.addWidget(self.number_edit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.date_edit = QDateEdit(Contract)
        self.date_edit.setObjectName(u"date_edit")

        self.horizontalLayout_2.addWidget(self.date_edit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.vendor_lbl = QLabel(Contract)
        self.vendor_lbl.setObjectName(u"vendor_lbl")

        self.horizontalLayout_3.addWidget(self.vendor_lbl)

        self.vendor_btn = QPushButton(Contract)
        self.vendor_btn.setObjectName(u"vendor_btn")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.vendor_btn.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.vendor_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.filename_lbl = QLabel(Contract)
        self.filename_lbl.setObjectName(u"filename_lbl")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.filename_lbl)


        self.verticalLayout.addLayout(self.formLayout)

        self.attach_file = QPushButton(Contract)
        self.attach_file.setObjectName(u"attach_file")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailAttachment))
        self.attach_file.setIcon(icon4)

        self.verticalLayout.addWidget(self.attach_file)

        self.delete_file = QPushButton(Contract)
        self.delete_file.setObjectName(u"delete_file")
        self.delete_file.setIcon(icon1)

        self.verticalLayout.addWidget(self.delete_file)

        self.open_file = QPushButton(Contract)
        self.open_file.setObjectName(u"open_file")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.open_file.setIcon(icon5)

        self.verticalLayout.addWidget(self.open_file)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Contract)

        QMetaObject.connectSlotsByName(Contract)
    # setupUi

    def retranslateUi(self, Contract):
        Contract.setWindowTitle(QCoreApplication.translate("Contract", u"Form", None))
        self.save_btn.setText(QCoreApplication.translate("Contract", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.delete_btn.setText(QCoreApplication.translate("Contract", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.close_btn.setText(QCoreApplication.translate("Contract", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Contract", u"\u041d\u043e\u043c\u0435\u0440:", None))
        self.label_2.setText(QCoreApplication.translate("Contract", u"\u0414\u0430\u0442\u0430:", None))
        self.label_3.setText(QCoreApplication.translate("Contract", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442:", None))
        self.label_4.setText(QCoreApplication.translate("Contract", u"\u0424\u0430\u0439\u043b:", None))
        self.vendor_lbl.setText("")
        self.vendor_btn.setText(QCoreApplication.translate("Contract", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442\u044b", None))
        self.filename_lbl.setText("")
        self.attach_file.setText(QCoreApplication.translate("Contract", u"\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.delete_file.setText(QCoreApplication.translate("Contract", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.open_file.setText(QCoreApplication.translate("Contract", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
    # retranslateUi

