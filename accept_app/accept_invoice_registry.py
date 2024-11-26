import datetime as dt
import sqlite3

from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlRelation, QSqlRelationalTableModel
from PySide6.QtWidgets import QMessageBox, QTableView, QWidget

from interfaces.ui_accept_requests_registry import Ui_Accept_requests_registry
from utils.models import DateDelegate


class AcceptInvoiceRegistry(QWidget):
    def __init__(self, parent):
        # Инициализация виджета для обработки заявок на согласование
        super().__init__()
        self.parent = parent
        self.ui = Ui_Accept_requests_registry()
        self.ui.setupUi(self)

        # Настройка модели таблицы для отображения заявок
        self.model = QSqlRelationalTableModel()
        self.model.setTable("Invoice")
        self.model.setRelation(5, QSqlRelation("Users", "id", "login"))

        # Загрузка списка заявок, доступных для согласования
        try:
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
        except sqlite3.DatabaseError as e:
            # Обработка ошибок при работе с базой данных
            QMessageBox.critical(self, "Ошибка базы данных", f"Не удалось загрузить данные: {e}")
            invoice_ids = []
        finally:
            con.close()

        # Установка фильтра для отображения заявок текущего пользователя
        self.model.setFilter(f"Invoice.id IN ({', '.join(map(lambda x: str(x[0]), invoice_ids))})")
        self.model.select()

        # Настройка отображения таблицы заявок
        self.ui.request_list.setModel(self.model)
        self.ui.request_list.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)
        self.ui.request_list.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.request_list.hideColumn(0)
        self.ui.request_list.hideColumn(6)
        self.ui.request_list.hideColumn(7)
        self.model.setHeaderData(1, Qt.Horizontal, "Номер")
        self.model.setHeaderData(2, Qt.Horizontal, "Описание")
        self.model.setHeaderData(3, Qt.Horizontal, "Дата создания")
        self.model.setHeaderData(4, Qt.Horizontal, "Статус")
        self.model.setHeaderData(5, Qt.Horizontal, "Закупщик")
        self.model.setHeaderData(6, Qt.Horizontal, "Контрагент")
        self.model.setHeaderData(7, Qt.Horizontal, "Файл")
        self.model.setHeaderData(8, Qt.Horizontal, "Сумма")
        date_delegate = DateDelegate()
        self.ui.request_list.setItemDelegateForColumn(3, date_delegate)
        self.ui.request_list.resizeColumnsToContents()

        # Привязка событий к элементам интерфейса
        self.ui.request_list.doubleClicked.connect(self.load_invoice)
        self.ui.accept_btn.clicked.connect(self.accept_invoice)
        self.ui.reject_btn.clicked.connect(self.reject_invoice)
        self.ui.refresh_btn.clicked.connect(self.refresh_list)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)

    def refresh_list(self):
        """Обновление списка заявок"""
        self.model.select()
        self.ui.request_list.reset()

    def load_invoice(self):
        """Загрузка данных о выбранной заявке"""
        selected_rows = self.ui.request_list.selectionModel().selectedRows()
        if len(selected_rows) != 1:
            QMessageBox.warning(self, "Ошибка выбора", "Выберите только одну заявку.")
            return
        invoice_id = self.model.data(selected_rows[0])
        if not invoice_id:
            QMessageBox.warning(self, "Ошибка", "Идентификатор заявки не найден.")
            return
        self.parent.open_invoice_creation_with_data(invoice_id)
        self.parent.status_bar.showMessage("Заявка успешно выбрана", 3000)

    def check_to_change_invoice_status(self):
        """Проверка и изменение статуса заявки на основе этапов согласования"""
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        invoice_ids = cur.execute("SELECT DISTINCT invoice_id FROM Invoice_approvals_stages").fetchall()
        invoice_ids = map(lambda x: x[0], invoice_ids)
        for id in invoice_ids:
            statuss = cur.execute("SELECT approval_status FROM Invoice_approvals_stages WHERE invoice_id=?;", (id,)).fetchall()
            if not statuss:
                QMessageBox.warning(self, "Ошибка", f"Статусы для заявки {id} не найдены.")
                continue
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
        """Согласование выбранной заявки"""
        selected_rows = self.ui.request_list.selectionModel().selectedRows()
        if len(selected_rows) != 1:
            QMessageBox.warning(self, "Ошибка выбора", "Выберите только одну заявку.")
            return
        approved_at = dt.datetime.now()
        comment = self.ui.lineEdit.text()
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        invoice_id = self.model.data(selected_rows[0])
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
        """Отклонение выбранной заявки"""
        selected_rows = self.ui.request_list.selectionModel().selectedRows()
        if len(selected_rows) != 1:
            QMessageBox.warning(self, "Ошибка выбора", "Выберите только одну заявку.")
            return
        approved_at = dt.datetime.now()
        comment = self.ui.lineEdit.text()
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        invoice_id = self.model.data(selected_rows[0])
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