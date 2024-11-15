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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Invoice(object):
    def setupUi(self, Invoice):
        if not Invoice.objectName():
            Invoice.setObjectName(u"Invoice")
        Invoice.resize(553, 428)
        self.verticalLayout = QVBoxLayout(Invoice)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menu_btn = QPushButton(Invoice)
        self.menu_btn.setObjectName(u"menu_btn")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        self.menu_btn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.menu_btn)

        self.save_btn = QPushButton(Invoice)
        self.save_btn.setObjectName(u"save_btn")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.save_btn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.save_btn)

        self.delete_btn = QPushButton(Invoice)
        self.delete_btn.setObjectName(u"delete_btn")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.delete_btn.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.delete_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.close_btn = QPushButton(Invoice)
        self.close_btn.setObjectName(u"close_btn")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.close_btn.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(Invoice)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.num_edit = QLineEdit(Invoice)
        self.num_edit.setObjectName(u"num_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_edit.sizePolicy().hasHeightForWidth())
        self.num_edit.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.num_edit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(Invoice)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.date_lbl = QLabel(Invoice)
        self.date_lbl.setObjectName(u"date_lbl")

        self.horizontalLayout_4.addWidget(self.date_lbl)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(Invoice)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.status_lbl = QLabel(Invoice)
        self.status_lbl.setObjectName(u"status_lbl")

        self.horizontalLayout_5.addWidget(self.status_lbl)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

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
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.add_nomenclature_btn.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.add_nomenclature_btn)

        self.delete_nomenclature_btn = QPushButton(Invoice)
        self.delete_nomenclature_btn.setObjectName(u"delete_nomenclature_btn")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.delete_nomenclature_btn.setIcon(icon5)
        self.delete_nomenclature_btn.setCheckable(False)
        self.delete_nomenclature_btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.delete_nomenclature_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(Invoice)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Invoice)

        QMetaObject.connectSlotsByName(Invoice)
    # setupUi

    def retranslateUi(self, Invoice):
        Invoice.setWindowTitle(QCoreApplication.translate("Invoice", u"Form", None))
        self.menu_btn.setText("")
        self.save_btn.setText(QCoreApplication.translate("Invoice", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.delete_btn.setText(QCoreApplication.translate("Invoice", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.close_btn.setText(QCoreApplication.translate("Invoice", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("Invoice", u"\u041d\u043e\u043c\u0435\u0440:", None))
        self.label_2.setText(QCoreApplication.translate("Invoice", u"\u0421\u043e\u0437\u0434\u0430\u043d\u043e:", None))
        self.date_lbl.setText("")
        self.label_3.setText(QCoreApplication.translate("Invoice", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.status_lbl.setText("")
        self.label.setText(QCoreApplication.translate("Invoice", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.description_text.setPlaceholderText(QCoreApplication.translate("Invoice", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u044f\u0432\u043a\u0438...", None))
        self.add_nomenclature_btn.setText("")
        self.delete_nomenclature_btn.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Invoice", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Invoice", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Invoice", u"\u0415\u0434. \u0438\u0437\u043c.", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Invoice", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None));
    # retranslateUi

