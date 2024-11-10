# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nomenclature_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
    QHBoxLayout, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Nomenclature_dialog(object):
    def setupUi(self, Nomenclature_dialog):
        if not Nomenclature_dialog.objectName():
            Nomenclature_dialog.setObjectName(u"Nomenclature_dialog")
        Nomenclature_dialog.resize(522, 379)
        self.verticalLayout = QVBoxLayout(Nomenclature_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(Nomenclature_dialog)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setSortingEnabled(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(Nomenclature_dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(Nomenclature_dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.pushButton = QPushButton(Nomenclature_dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Nomenclature_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Nomenclature_dialog)
        self.buttonBox.accepted.connect(Nomenclature_dialog.accept)
        self.buttonBox.rejected.connect(Nomenclature_dialog.reject)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Nomenclature_dialog)
    # setupUi

    def retranslateUi(self, Nomenclature_dialog):
        Nomenclature_dialog.setWindowTitle(QCoreApplication.translate("Nomenclature_dialog", u"Dialog", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Nomenclature_dialog", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Nomenclature_dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Nomenclature_dialog", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None));
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Nomenclature_dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Nomenclature_dialog", u"\u0415\u0434. \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("Nomenclature_dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

