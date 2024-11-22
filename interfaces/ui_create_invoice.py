# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_invoice.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLCDNumber,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Invoice(object):
    def setupUi(self, Invoice):
        if not Invoice.objectName():
            Invoice.setObjectName(u"Invoice")
        Invoice.resize(759, 574)
        self.verticalLayout = QVBoxLayout(Invoice)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.save_btn = QPushButton(Invoice)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_3.addWidget(self.save_btn)

        self.delete_btn = QPushButton(Invoice)
        self.delete_btn.setObjectName(u"delete_btn")

        self.horizontalLayout_3.addWidget(self.delete_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.close_btn = QPushButton(Invoice)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(Invoice)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.name_edit = QLineEdit(Invoice)
        self.name_edit.setObjectName(u"name_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name_edit.sizePolicy().hasHeightForWidth())
        self.name_edit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.name_edit)

        self.label_2 = QLabel(Invoice)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.date_lbl = QLabel(Invoice)
        self.date_lbl.setObjectName(u"date_lbl")

        self.horizontalLayout_4.addWidget(self.date_lbl)

        self.label_3 = QLabel(Invoice)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.status_lbl = QLabel(Invoice)
        self.status_lbl.setObjectName(u"status_lbl")

        self.horizontalLayout_4.addWidget(self.status_lbl)

        self.send_btn = QPushButton(Invoice)
        self.send_btn.setObjectName(u"send_btn")

        self.horizontalLayout_4.addWidget(self.send_btn)

        self.accept_viewer_btn = QPushButton(Invoice)
        self.accept_viewer_btn.setObjectName(u"accept_viewer_btn")

        self.horizontalLayout_4.addWidget(self.accept_viewer_btn)

        self.file_btn = QPushButton(Invoice)
        self.file_btn.setObjectName(u"file_btn")

        self.horizontalLayout_4.addWidget(self.file_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(Invoice)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setBold(True)
        font1.setKerning(True)
        self.label_4.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.vendor_lbl = QLabel(Invoice)
        self.vendor_lbl.setObjectName(u"vendor_lbl")

        self.horizontalLayout_7.addWidget(self.vendor_lbl)

        self.vendor_btn = QPushButton(Invoice)
        self.vendor_btn.setObjectName(u"vendor_btn")

        self.horizontalLayout_7.addWidget(self.vendor_btn)

        self.label_6 = QLabel(Invoice)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.contract_lbl = QLabel(Invoice)
        self.contract_lbl.setObjectName(u"contract_lbl")

        self.horizontalLayout_7.addWidget(self.contract_lbl)

        self.contract_btn = QPushButton(Invoice)
        self.contract_btn.setObjectName(u"contract_btn")
        self.contract_btn.setEnabled(True)

        self.horizontalLayout_7.addWidget(self.contract_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Invoice)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label.setMargin(10)

        self.horizontalLayout.addWidget(self.label)

        self.description_text = QTextEdit(Invoice)
        self.description_text.setObjectName(u"description_text")

        self.horizontalLayout.addWidget(self.description_text)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_nomenclature_btn = QPushButton(Invoice)
        self.add_nomenclature_btn.setObjectName(u"add_nomenclature_btn")

        self.horizontalLayout_2.addWidget(self.add_nomenclature_btn)

        self.delete_nomenclature_btn = QPushButton(Invoice)
        self.delete_nomenclature_btn.setObjectName(u"delete_nomenclature_btn")
        self.delete_nomenclature_btn.setCheckable(False)
        self.delete_nomenclature_btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.delete_nomenclature_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(Invoice)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_7 = QLabel(Invoice)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.sum_lcd = QLCDNumber(Invoice)
        self.sum_lcd.setObjectName(u"sum_lcd")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sum_lcd.sizePolicy().hasHeightForWidth())
        self.sum_lcd.setSizePolicy(sizePolicy2)
        self.sum_lcd.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_5.addWidget(self.sum_lcd)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Invoice)

        QMetaObject.connectSlotsByName(Invoice)
    # setupUi

    def retranslateUi(self, Invoice):
        Invoice.setWindowTitle(QCoreApplication.translate("Invoice", u"Form", None))
        self.save_btn.setText(QCoreApplication.translate("Invoice", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.delete_btn.setText(QCoreApplication.translate("Invoice", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.close_btn.setText(QCoreApplication.translate("Invoice", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("Invoice", u"\u041d\u043e\u043c\u0435\u0440:", None))
        self.label_2.setText(QCoreApplication.translate("Invoice", u"\u0421\u043e\u0437\u0434\u0430\u043d\u043e:", None))
        self.date_lbl.setText("")
        self.label_3.setText(QCoreApplication.translate("Invoice", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.status_lbl.setText("")
        self.send_btn.setText(QCoreApplication.translate("Invoice", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c...", None))
        self.accept_viewer_btn.setText(QCoreApplication.translate("Invoice", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.file_btn.setText(QCoreApplication.translate("Invoice", u"\u0424\u0430\u0439\u043b", None))
        self.label_4.setText(QCoreApplication.translate("Invoice", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0433\u043d\u0435\u0442:", None))
        self.vendor_lbl.setText("")
        self.vendor_btn.setText(QCoreApplication.translate("Invoice", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442\u044b", None))
        self.label_6.setText(QCoreApplication.translate("Invoice", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440:", None))
        self.contract_lbl.setText("")
        self.contract_btn.setText(QCoreApplication.translate("Invoice", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b", None))
        self.label.setText(QCoreApplication.translate("Invoice", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.description_text.setPlaceholderText(QCoreApplication.translate("Invoice", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0441\u0447\u0435\u0442\u0430...", None))
        self.add_nomenclature_btn.setText(QCoreApplication.translate("Invoice", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_nomenclature_btn.setText(QCoreApplication.translate("Invoice", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Invoice", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Invoice", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Invoice", u"\u0415\u0434. \u0438\u0437\u043c.", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Invoice", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Invoice", u"\u0426\u0435\u043d\u0430", None));
        self.label_7.setText(QCoreApplication.translate("Invoice", u"\u0421\u0443\u043c\u043c\u0430:", None))
    # retranslateUi

