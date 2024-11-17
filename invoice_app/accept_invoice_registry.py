import sqlite3
import datetime as dt

from PySide6.QtWidgets import QWidget, QTableView
from PySide6.QtSql import QSqlRelationalTableModel, QSqlRelation

from interfaces.ui_accept_requests_registry import Ui_Accept_requests_registry
from requests_app.models import DateDelegate
from invoice_app.invoice_widget import InvoiceWidget


class AcceptInvoiceRegistry(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Accept_requests_registry()
        self.ui.setupUi(self)

        self.model = QSqlRelationalTableModel()
        self.model.setTable("Invoice")
        self.model.setRelation(5, QSqlRelation("Vendor", "id", "name"))
        self.model.setRelation(6, QSqlRelation("Users", "id", "login"))

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        query = """
        SELECT DISTINCT r1.invoice_id
        FROM Invoice_approvals_stages AS r1
        WHERE r1.acceptor_id = ? 
        AND r1.approval_status = 'Не согласовано'
        AND NOT EXISTS (
            SELECT 1 
            FROM Invoice_approvals_stages AS r2
            WHERE r2.invoice_id = r1.invoice_id 
                AND r2.stage_order < r1.stage_order 
                AND r2.approval_status = 'Не согласовано'
        );
        """
        invoice_ids = cur.execute(query, (self.parent.user_id,)).fetchall()
        con.close()

        self.model.setFilter(f"Invoice.id IN ({", ".join(map(lambda x: str(x[0]), invoice_ids))})")
        self.model.select()

        self.ui.request_list.setModel(self.model)
        self.ui.request_list.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)
        self.ui.request_list.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.request_list.hideColumn(0)
        date_delegate = DateDelegate()
        self.ui.request_list.setItemDelegateForColumn(3, date_delegate)
        self.ui.request_list.resizeColumnsToContents()

        # self.invoice_widget = InvoiceWidget(self.parent)
        # self.invoice_widget.setDisabled(True)
        # self.ui.horizontalLayout_2.addWidget(self.invoice_widget)

        self.ui.request_list.doubleClicked.connect(self.load_invoice)
        self.ui.accept_btn.clicked.connect(self.accept_invoice)
        self.ui.reject_btn.clicked.connect(self.reject_invoice)
        self.ui.refresh_btn.clicked.connect(self.refresh_list)

    def refresh_list(self):
        self.model.select()
        self.ui.request_list.reset()

    def load_invoice(self):
        selected_rows = self.ui.request_list.selectionModel().selectedRows()
        if len(selected_rows) > 1:
            return
        invoice_id = self.model.data(selected_rows[0])
        # self.invoice_widget.load_invoice_data(invoice_id)
        self.parent.open_invoice_creation_with_data(invoice_id)

        self.parent.status_bar.showMessage("Заявка успешно выбрана", 3000)

    def check_to_change_invoice_status(self):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        invoice_ids = cur.execute("SELECT DISTINCT invoice_id FROM Invoice_approvals_stages").fetchall()
        invoice_ids = map(lambda x: x[0], invoice_ids)
        for id in invoice_ids:
            statuss = cur.execute("SELECT approval_status FROM Invoice_approvals_stages WHERE invoice_id=?;", (id,)).fetchall()
            statuss = list(map(lambda x: x[0], statuss))
            is_acepted = list(map(lambda x: x != "Не согласовано", statuss))
            if all(is_acepted):
                if "Отклонено" in list(statuss):
                    cur.execute("UPDATE Invoice SET status=? WHERE id=?;", ("Отклонено", id))
                    self.parent.status_bar.showMessage("Статус заявки изменен на 'Отклонено'", 3000)
                else:
                    cur.execute("UPDATE Invoice SET status=? WHERE id=?;", ("Согласовано", id))
                    self.parent.status_bar.showMessage("Статус заявки изменен на 'Согласовано'", 3000)
                cur.execute("DELETE FROM Invoice_approvals_stages WHERE invoice_id=?;", (id,))
        con.commit()
        con.close()

    def accept_invoice(self):
        approved_at = dt.datetime.now()
        comment = self.ui.lineEdit.text()
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        invoice_id = self.model.data(self.ui.request_list.selectionModel().selectedRows()[0])
        cur.execute("""
                    UPDATE Invoice_approvals_stages
                    SET comment=?, approval_status=?, approved_at=?
                    WHERE acceptor_id=? AND invoice_id=?;
                    """, (comment, "Согласовано", approved_at, self.parent.user_id, invoice_id))
        con.commit()
        con.close()
        self.refresh_list()
        self.check_to_change_invoice_status()

        self.parent.status_bar.showMessage("Заявка согласована", 3000)

    def reject_invoice(self):
        approved_at = dt.datetime.now()
        comment = self.ui.lineEdit.text()
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        invoice_id = self.model.data(self.ui.request_list.selectionModel().selectedRows()[0])
        cur.execute("""
                    UPDATE Invoice_approvals_stages
                    SET comment=?, approval_status=?, approved_at=?
                    WHERE acceptor_id=? AND invoice_id=?;
                    """, (comment, "Отклонено", approved_at, self.parent.user_id, invoice_id))
        con.commit()
        con.close()
        self.refresh_list()
        self.check_to_change_invoice_status()

        self.parent.status_bar.showMessage("Заявка отклонена", 3000)
