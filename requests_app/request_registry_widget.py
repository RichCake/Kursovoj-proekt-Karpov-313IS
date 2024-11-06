import sqlite3

from PySide6.QtWidgets import QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic menu.ui -o ui_form.py, or
#     pyside2-uic menu.ui -o ui_form.py
from interfaces.ui_request_registry import Ui_Request_registry


class RequestRegistryWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Request_registry()
        self.ui.setupUi(self)

        con = sqlite3.connect(parent.database_file)
        cur = con.cursor()
        request_list = cur.execute("SELECT * FROM Requests").fetchall()
        for request in request_list:
            self.ui.request_list.addItem(str(request))
        con.close()

        self.ui.open_menu_btn.clicked.connect(parent.open_menu)