import sqlite3

from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlRelation, QSqlRelationalTableModel
from PySide6.QtWidgets import QTableView, QWidget

from interfaces.ui_invoice_registry import Ui_Invoice_registry
from utils.models import DateDelegate


class InvoiceRegistryWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Invoice_registry()
        self.ui.setupUi(self)

        self.model = QSqlRelationalTableModel()
        self.model.setTable("Invoice")
        self.model.setRelation(5, QSqlRelation("Users", "id", "login"))
        self.model.select()

        self.ui.invoice_list.setModel(self.model)
        self.ui.invoice_list.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)
        self.ui.invoice_list.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.invoice_list.hideColumn(0)
        self.ui.invoice_list.hideColumn(6)
        self.ui.invoice_list.hideColumn(7)
        self.model.setHeaderData(1, Qt.Horizontal, "Номер")
        self.model.setHeaderData(2, Qt.Horizontal, "Описание")
        self.model.setHeaderData(3, Qt.Horizontal, "Дата создания")
        self.model.setHeaderData(4, Qt.Horizontal, "Статус")
        self.model.setHeaderData(5, Qt.Horizontal, "Закупщик")
        self.model.setHeaderData(6, Qt.Horizontal, "Контрагент")
        self.model.setHeaderData(7, Qt.Horizontal, "Файл")
        self.model.setHeaderData(8, Qt.Horizontal, "Сумма")
        date_delegate = DateDelegate()
        self.ui.invoice_list.setItemDelegateForColumn(3, date_delegate)
        self.ui.invoice_list.resizeColumnsToContents()

        self.setup_vender_combobox()

        self.ui.invoice_list.doubleClicked.connect(self.open_invoice_details)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)
        self.ui.refresh_btn.clicked.connect(self.refresh_values)
        self.ui.create_btn.clicked.connect(parent.open_invoice_creation)
        self.ui.vender_combo_box.currentTextChanged.connect(self.filter_list)
        self.ui.comboBox.currentTextChanged.connect(self.filter_list)

    def filter_list(self):
        vender_name = self.ui.vender_combo_box.currentText()
        status_name = self.ui.comboBox.currentText()

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()

        if vender_name == "-" and status_name == "-":
            self.model.setFilter("")
            return
        elif status_name == "-":
            vender_id = cur.execute("SELECT id FROM Vendor WHERE name=?", (vender_name,)).fetchone()[0]
            self.model.setFilter(f"vender_id={vender_id}")
        elif vender_name == "-":
            self.model.setFilter(f"status='{status_name}'")
        else:
            vender_id = cur.execute("SELECT id FROM Vendor WHERE name=?", (vender_name,)).fetchone()[0]
            self.model.setFilter(f"vender_id={vender_id} AND status='{status_name}'")

        con.close()
        self.refresh_values()

    def setup_vender_combobox(self):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        categories = cur.execute("SELECT name FROM Vendor").fetchall()
        con.close()
        self.ui.vender_combo_box.clear()
        categories = list(map(lambda x: x[0], categories))
        self.ui.vender_combo_box.insertItems(0, categories)
        self.ui.vender_combo_box.insertItem(0, "-")
        self.ui.vender_combo_box.setCurrentIndex(0)

    def open_invoice_details(self, index):
        invoice_id = self.ui.invoice_list.model().data(self.ui.invoice_list.model().index(index.row(), 0))
        self.parent.open_invoice_creation_with_data(invoice_id)

    def refresh_values(self):
        self.model.select()
        self.ui.invoice_list.reset()