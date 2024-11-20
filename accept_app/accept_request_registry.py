import datetime as dt
import sqlite3

from PySide6.QtSql import QSqlRelation, QSqlRelationalTableModel
from PySide6.QtWidgets import QTableView, QWidget

from interfaces.ui_accept_requests_registry import Ui_Accept_requests_registry

from utils.models import DateDelegate


class AcceptRequestRegistry(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Accept_requests_registry()
        self.ui.setupUi(self)

        self.model = QSqlRelationalTableModel()
        self.model.setTable("Requests")
        self.model.setRelation(4, QSqlRelation("Request_category", "id", "name"))
        self.model.setRelation(5, QSqlRelation("Users", "id", "login"))

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        query = """
        SELECT DISTINCT r1.request_id
        FROM Request_approvals_stages AS r1
        WHERE r1.acceptor_id = ? 
        AND r1.approval_status = 'Не согласовано'
        AND NOT EXISTS (
            SELECT 1 
            FROM Request_approvals_stages AS r2
            WHERE r2.request_id = r1.request_id 
                AND r2.stage_order < r1.stage_order 
                AND r2.approval_status = 'Не согласовано'
        );
        """
        request_ids = cur.execute(query, (self.parent.user_id,)).fetchall()
        con.close()

        self.model.setFilter(f"Requests.id IN ({', '.join(map(lambda x: str(x[0]), request_ids))})")
        self.model.select()

        self.ui.request_list.setModel(self.model)
        self.ui.request_list.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)
        self.ui.request_list.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.request_list.hideColumn(0)
        self.ui.request_list.hideColumn(0)
        date_delegate = DateDelegate()
        self.ui.request_list.setItemDelegateForColumn(2, date_delegate)
        self.ui.request_list.resizeColumnsToContents()

        # self.request_widget = RequestWidget(self.parent)
        # self.request_widget.setDisabled(True)
        # self.ui.horizontalLayout_2.addWidget(self.request_widget)

        self.ui.request_list.doubleClicked.connect(self.load_request)
        self.ui.accept_btn.clicked.connect(self.accept_request)
        self.ui.reject_btn.clicked.connect(self.reject_request)
        self.ui.refresh_btn.clicked.connect(self.refresh_list)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)

    def refresh_list(self):
        self.model.select()
        self.ui.request_list.reset()

    def load_request(self):
        selected_rows = self.ui.request_list.selectionModel().selectedRows()
        if len(selected_rows) > 1:
            return
        request_id = self.model.data(selected_rows[0])
        # self.request_widget.load_request_data(request_id)
        self.parent.open_request_creation_with_data(request_id)

        self.parent.status_bar.showMessage("Заявка успешно выбрана", 3000)

    def check_to_change_request_status(self):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        request_ids = cur.execute("SELECT DISTINCT request_id FROM Request_approvals_stages").fetchall()
        request_ids = map(lambda x: x[0], request_ids)
        for id in request_ids:
            statuss = cur.execute("SELECT approval_status FROM Request_approvals_stages WHERE request_id=?;", (id,)).fetchall()
            statuss = list(map(lambda x: x[0], statuss))
            is_acepted = list(map(lambda x: x != "Не согласовано", statuss))
            if all(is_acepted):
                if "Отклонено" in list(statuss):
                    cur.execute("UPDATE Requests SET status=? WHERE id=?;", ("Отклонено", id))
                    self.parent.status_bar.showMessage("Статус заявки изменен на 'Отклонено'", 3000)
                else:
                    cur.execute("UPDATE Requests SET status=? WHERE id=?;", ("Согласовано", id))
                    self.parent.status_bar.showMessage("Статус заявки изменен на 'Согласовано'", 3000)
                cur.execute("DELETE FROM Request_approvals_stages WHERE request_id=?;", (id,))
        con.commit()
        con.close()

    def accept_request(self):
        approved_at = dt.datetime.now()
        comment = self.ui.lineEdit.text()
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        request_id = self.model.data(self.ui.request_list.selectionModel().selectedRows()[0])
        cur.execute("""
                    UPDATE Request_approvals_stages
                    SET comment=?, approval_status=?, approved_at=?
                    WHERE acceptor_id=? AND request_id=?;
                    """, (comment, "Согласовано", approved_at, self.parent.user_id, request_id))
        con.commit()
        con.close()
        self.refresh_list()
        self.check_to_change_request_status()

        self.parent.status_bar.showMessage("Заявка согласована", 3000)

    def reject_request(self):
        approved_at = dt.datetime.now()
        comment = self.ui.lineEdit.text()
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        request_id = self.model.data(self.ui.request_list.selectionModel().selectedRows()[0])
        cur.execute("""
                    UPDATE Request_approvals_stages 
                    SET comment=?, approval_status=? approved_at=?
                    WHERE acceptor_id=? AND request_id=?;
                    """, (comment, "Отклонено", approved_at, self.parent.user_id, request_id))
        con.commit()
        con.close()
        self.refresh_list()
        self.check_to_change_request_status()

        self.parent.status_bar.showMessage("Заявка отклонена", 3000)
