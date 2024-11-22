# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_User_widget(object):
    def setupUi(self, User_widget):
        if not User_widget.objectName():
            User_widget.setObjectName(u"User_widget")
        User_widget.resize(659, 383)
        self.verticalLayout_2 = QVBoxLayout(User_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.save_btn = QPushButton(User_widget)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_3.addWidget(self.save_btn)

        self.delete_btn = QPushButton(User_widget)
        self.delete_btn.setObjectName(u"delete_btn")

        self.horizontalLayout_3.addWidget(self.delete_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.close_btn = QPushButton(User_widget)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(User_widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.id_ldl = QLabel(User_widget)
        self.id_ldl.setObjectName(u"id_ldl")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.id_ldl)

        self.label_2 = QLabel(User_widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.first_name_edit = QLineEdit(User_widget)
        self.first_name_edit.setObjectName(u"first_name_edit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.first_name_edit)

        self.label_3 = QLabel(User_widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.second_name_edit = QLineEdit(User_widget)
        self.second_name_edit.setObjectName(u"second_name_edit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.second_name_edit)

        self.label_4 = QLabel(User_widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.third_name_edit = QLineEdit(User_widget)
        self.third_name_edit.setObjectName(u"third_name_edit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.third_name_edit)

        self.label_5 = QLabel(User_widget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.position_edit = QLineEdit(User_widget)
        self.position_edit.setObjectName(u"position_edit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.position_edit)

        self.login_edit = QLineEdit(User_widget)
        self.login_edit.setObjectName(u"login_edit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.login_edit)

        self.label_8 = QLabel(User_widget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.password_edit = QLineEdit(User_widget)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.password_edit)

        self.label_6 = QLabel(User_widget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.label_11 = QLabel(User_widget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_11)

        self.access_rights_combobox = QComboBox(User_widget)
        self.access_rights_combobox.addItem("")
        self.access_rights_combobox.addItem("")
        self.access_rights_combobox.setObjectName(u"access_rights_combobox")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.access_rights_combobox)


        self.horizontalLayout.addLayout(self.formLayout)

        self.change_password_frame = QFrame(User_widget)
        self.change_password_frame.setObjectName(u"change_password_frame")
        self.verticalLayout = QVBoxLayout(self.change_password_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_10 = QLabel(self.change_password_frame)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setBold(True)
        self.label_10.setFont(font)

        self.verticalLayout.addWidget(self.label_10)

        self.label_7 = QLabel(self.change_password_frame)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.new_password1_edit = QLineEdit(self.change_password_frame)
        self.new_password1_edit.setObjectName(u"new_password1_edit")
        font1 = QFont()
        font1.setKerning(True)
        self.new_password1_edit.setFont(font1)
        self.new_password1_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.new_password1_edit)

        self.label_9 = QLabel(self.change_password_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(False)

        self.verticalLayout.addWidget(self.label_9)

        self.new_password2_edit = QLineEdit(self.change_password_frame)
        self.new_password2_edit.setObjectName(u"new_password2_edit")
        self.new_password2_edit.setFont(font1)
        self.new_password2_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.new_password2_edit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.chenge_password_btn = QPushButton(self.change_password_frame)
        self.chenge_password_btn.setObjectName(u"chenge_password_btn")
        self.chenge_password_btn.setAutoExclusive(False)
        self.chenge_password_btn.setAutoDefault(False)

        self.verticalLayout.addWidget(self.chenge_password_btn)


        self.horizontalLayout.addWidget(self.change_password_frame)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(User_widget)

        self.chenge_password_btn.setDefault(False)


        QMetaObject.connectSlotsByName(User_widget)
    # setupUi

    def retranslateUi(self, User_widget):
        User_widget.setWindowTitle(QCoreApplication.translate("User_widget", u"Form", None))
        self.save_btn.setText(QCoreApplication.translate("User_widget", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.delete_btn.setText(QCoreApplication.translate("User_widget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.close_btn.setText(QCoreApplication.translate("User_widget", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("User_widget", u"id:", None))
        self.id_ldl.setText("")
        self.label_2.setText(QCoreApplication.translate("User_widget", u"\u0418\u043c\u044f:", None))
        self.label_3.setText(QCoreApplication.translate("User_widget", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.label_4.setText(QCoreApplication.translate("User_widget", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.label_5.setText(QCoreApplication.translate("User_widget", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.label_8.setText(QCoreApplication.translate("User_widget", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_6.setText(QCoreApplication.translate("User_widget", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_11.setText(QCoreApplication.translate("User_widget", u"\u041f\u0440\u0430\u0432\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u0430:", None))
        self.access_rights_combobox.setItemText(0, QCoreApplication.translate("User_widget", u"\u0418\u043d\u0438\u0446\u0438\u0430\u0442\u043e\u0440", None))
        self.access_rights_combobox.setItemText(1, QCoreApplication.translate("User_widget", u"\u0417\u0430\u043a\u0443\u043f\u0449\u0438\u043a", None))

        self.label_10.setText(QCoreApplication.translate("User_widget", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_7.setText(QCoreApplication.translate("User_widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_9.setText(QCoreApplication.translate("User_widget", u"\u041f\u043e\u0432\u0442\u043e\u0440\u043d\u043e \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.chenge_password_btn.setText(QCoreApplication.translate("User_widget", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

