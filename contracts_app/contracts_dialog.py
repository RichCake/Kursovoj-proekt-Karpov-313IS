import sqlite3

from PySide6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QTableView

from interfaces.ui_contract_dialog import Ui_Dialog
from utils.models import DateDelegate


class ContractDialog(QDialog):
    def __init__(self, parent, vender_id):
        super().__init__()
        self.parent = parent
        self.vender_id = vender_id
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tableWidget.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.tableWidget.hideColumn(0)
        date_delegate = DateDelegate()
        self.ui.tableWidget.setItemDelegateForColumn(2, date_delegate)
        self.ui.tableWidget.resizeColumnsToContents()

        self.update_list()

        self.ui.pushButton.clicked.connect(self.add_contract)
        self.ui.buttonBox.accepted.disconnect()
        self.ui.buttonBox.accepted.connect(self.select_contract)

    def update_list(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        contracts = cur.execute("SELECT id, number, date FROM Contracts WHERE vender_id=?;", (self.vender_id,)).fetchall()
        con.close()
        self.ui.tableWidget.setRowCount(len(contracts))
        for row, contract in enumerate(contracts):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(contract[0])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(contract[1])))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(contract[2])))
        self.ui.tableWidget.resizeColumnsToContents()

    def select_contract(self):
        print(len(self.ui.tableWidget.selectedItems()))
        if len(self.ui.tableWidget.selectedItems()) != 2:
            QMessageBox.warning(self, "Предупреждение", "Выберете один договор")
            return
        self.contract_id = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text()
        contract_number = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 1).text()
        contract_date = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 2).text()
        self.contract_name = contract_number + " от " + contract_date
        self.accept()

    def add_contract(self):
        number = self.ui.lineEdit.text()
        date = self.ui.dateEdit.date().toPython()
        if number and date:
            con = sqlite3.connect(self.parent.database_file)
            cur = con.cursor()
            cur.execute("INSERT INTO Contracts(number, date, vender_id) VALUES (?, ?, ?)", (number, date, self.vender_id))
            con.commit()
            con.close()
            self.update_list()
