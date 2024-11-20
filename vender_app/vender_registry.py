import sqlite3

from PySide6.QtWidgets import QMessageBox, QTableView, QTableWidgetItem, QWidget

from interfaces.ui_vender_registry import Ui_VenderRegistry


class VenderRegistry(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_VenderRegistry()
        self.ui.setupUi(self)
        self.ui.tableWidget.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.tableWidget.hideColumn(0)
        self.ui.tableWidget.resizeColumnsToContents()

        self.update_list()

        self.ui.tableWidget.doubleClicked.connect(self.open_vender)
        self.ui.close_btn_2.clicked.connect(parent.close_current_tab)
        self.ui.refresh_btn_2.clicked.connect(self.update_list)
        self.ui.create_btn_2.clicked.connect(parent.open_vender_creation)

    def update_list(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        contracts = cur.execute("SELECT id, name, address FROM Vendor;").fetchall()
        con.close()
        self.ui.tableWidget.setRowCount(len(contracts))
        for row, contract in enumerate(contracts):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(contract[0])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(contract[1])))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(contract[2])))
        self.ui.tableWidget.resizeColumnsToContents()

    def open_vender(self, index):
        vender_id_item = self.ui.tableWidget.item(index.row(), 0)
        if vender_id_item is not None:
            try:
                vender_id = int(vender_id_item.text())
                self.parent.open_vender_with_data(vender_id)
            except ValueError:
                QMessageBox.warning(self, "Ошибка", "Некорректный идентификатор.")
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось получить идентификатор.")
