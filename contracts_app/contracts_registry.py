import sqlite3

from PySide6.QtWidgets import QMessageBox, QTableView, QTableWidgetItem, QWidget

from interfaces.ui_contract_registry import Ui_ContractRegistry
from utils.models import DateDelegate


class ContractRegistry(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_ContractRegistry()
        self.ui.setupUi(self)
        self.ui.tableWidget.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.tableWidget.hideColumn(0)
        date_delegate = DateDelegate()
        self.ui.tableWidget.setItemDelegateForColumn(2, date_delegate)
        self.ui.tableWidget.resizeColumnsToContents()

        self.update_list()

        self.ui.tableWidget.doubleClicked.connect(self.open_contract)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)
        self.ui.refresh_btn.clicked.connect(self.update_list)
        self.ui.create_btn.clicked.connect(parent.open_contract_creation)

    def update_list(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        contracts = cur.execute("SELECT id, number, date FROM Contracts;").fetchall()
        con.close()
        self.ui.tableWidget.setRowCount(len(contracts))
        for row, contract in enumerate(contracts):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(contract[0])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(contract[1])))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(contract[2])))
        self.ui.tableWidget.resizeColumnsToContents()

    def open_contract(self, index):
        contract_id_item = self.ui.tableWidget.item(index.row(), 0)
        if contract_id_item is not None:
            try:
                contract_id = int(contract_id_item.text())
                self.parent.open_contract_with_data(contract_id)
            except ValueError:
                QMessageBox.warning(self, "Ошибка", "Некорректный идентификатор контракта.")
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось получить идентификатор контракта.")
