import sqlite3

from PySide6.QtWidgets import QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic menu.ui -o ui_form.py, or
#     pyside2-uic menu.ui -o ui_form.py
from interfaces.ui_invoice_registry import Ui_Invoice_registry


class InvoiceRegistryWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Invoice_registry()
        self.ui.setupUi(self)

        con = sqlite3.connect(parent.database_file)
        cur = con.cursor()
        invoice_list = cur.execute("SELECT * FROM Invoice").fetchall()
        for invoice in invoice_list:
            self.ui.invoice_list.addItem(str(invoice))
        con.close()

        self.ui.open_menu_btn.clicked.connect(parent.open_menu)