import sqlite3

from PySide6.QtWidgets import QDialog, QTableWidgetItem, QCheckBox
from PySide6 import QtCore

from interfaces.ui_request_items_dialog import Ui_Dialog

class SelectRequestItemsDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tableWidget.hideColumn(0)
        self.ui.buttonBox.accepted.connect(self.select_items)

    def select_items(self):
        self.request_item_ids = []
        for i in range(self.ui.tableWidget.rowCount()):
            if self.ui.tableWidget.item(i, 1).checkState:
                self.request_item_ids.append(self.ui.tableWidget.item(i, 0).text())
        self.accept()

    def load_items(self, request_item_ids):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        items = cur.execute(
            f"""
            SELECT Request_items.id, 
                Request_items.amount, 
                Nomenclature.name, 
                Nomenclature.unit
            FROM Request_items
            LEFT JOIN Nomenclature ON Request_items.item_id = Nomenclature.id
            WHERE Request_items.id IN ({", ".join(["?"] * len(request_item_ids))})
            """, 
            *request_item_ids
        ).fetchall()
        for request_item_id, amount, name, unit in items:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(row + 1)
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(request_item_ids)))

            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked) 
            self.ui.tableWidget.setItem(row, 1, chkBoxItem)

            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(name))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(unit))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(amount)))