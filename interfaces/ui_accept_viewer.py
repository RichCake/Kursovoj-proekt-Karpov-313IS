# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accept_viewer.ui'
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

class Ui_AcceptViewer(object):
    def setupUi(self, AcceptViewer):
        if not AcceptViewer.objectName():
            AcceptViewer.setObjectName(u"AcceptViewer")
        AcceptViewer.resize(699, 425)
        self.verticalLayout = QVBoxLayout(AcceptViewer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(AcceptViewer)
        self.close_btn.setObjectName(u"close_btn")

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_btn = QPushButton(AcceptViewer)
        self.add_btn.setObjectName(u"add_btn")

        self.horizontalLayout_2.addWidget(self.add_btn)

        self.remove_btn = QPushButton(AcceptViewer)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setCheckable(False)
        self.remove_btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.remove_btn)

        self.cancel_btn = QPushButton(AcceptViewer)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setCheckable(False)
        self.cancel_btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.cancel_btn)

        self.save_btn = QPushButton(AcceptViewer)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_2.addWidget(self.save_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableView = QTableView(AcceptViewer)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(AcceptViewer)

        QMetaObject.connectSlotsByName(AcceptViewer)
    # setupUi

    def retranslateUi(self, AcceptViewer):
        AcceptViewer.setWindowTitle(QCoreApplication.translate("AcceptViewer", u"Form", None))
        self.close_btn.setText(QCoreApplication.translate("AcceptViewer", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.add_btn.setText(QCoreApplication.translate("AcceptViewer", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.remove_btn.setText(QCoreApplication.translate("AcceptViewer", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.cancel_btn.setText(QCoreApplication.translate("AcceptViewer", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c", None))
        self.save_btn.setText(QCoreApplication.translate("AcceptViewer", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

