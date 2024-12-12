import sqlite3

from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlRelation, QSqlRelationalTableModel
from PyQt6.QtWidgets import QAbstractItemView, QDialog, QMessageBox, QTableView, QWidget

from accept_app.accept_dialog import AcceptDialog
from interfaces.ui_accept_viewer import Ui_AcceptViewer
from utils.models import ReadOnlyDelegate


class AcceptRequestWidget(QWidget):
    def __init__(self, parent, request_id):
        super().__init__()
        self.parent = parent
        self.request_id = request_id
        self.ui = Ui_AcceptViewer()
        self.ui.setupUi(self)

        # Настройка модели
        self.model = QSqlRelationalTableModel(self)
        self.model.setTable("Request_approvals_stages")
        self.ui.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.model.setRelation(6, QSqlRelation("Users", "id", "first_name || ' ' || second_name || ' ' || third_name AS ФИО"))

        # Задаем заголовки таблицы
        self.model.setHeaderData(1, Qt.Horizontal, "Статус")
        self.model.setHeaderData(2, Qt.Horizontal, "Дата утверждения")
        self.model.setHeaderData(3, Qt.Horizontal, "Комментарий")
        self.model.setHeaderData(4, Qt.Horizontal, "Порядок этапа")
        self.model.setHeaderData(7, Qt.Horizontal, "ФИО")

        # Фильтрация по ID заявки
        self.model.setFilter(f"request_id = {self.request_id}")
        self.model.select()

        # Настройка таблицы
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.hideColumn(0)  # Скрываем ID записи
        self.ui.tableView.hideColumn(5)  # Скрываем ID заявки
        self.ui.tableView.resizeColumnsToContents()

        # Устанавливаем запрет редактирования поля "Статус"
        self.ui.tableView.setItemDelegateForColumn(1, ReadOnlyDelegate())

        # Привязка кнопок
        self.ui.save_btn.clicked.connect(self.save_accept)
        self.ui.add_btn.clicked.connect(self.add_accept_row)
        self.ui.remove_btn.clicked.connect(self.remove_accept_row)
        self.ui.cancel_btn.clicked.connect(self.revert_contacts)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)

    def revert_contacts(self):
        self.model.revertAll()
        self.model.select()

    def save_accept(self):
        if self.model.submitAll():
            QMessageBox.information(self, "Сохранение", "Изменения успешно сохранены.")
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить изменения.")
        self.model.select()

    def add_accept_row(self):
        dialog = AcceptDialog(self.parent)
        if dialog.exec():
            approval_status = "Не согласовано"
            con = sqlite3.connect(self.parent.database_file)
            cur = con.cursor()

            max_stage = cur.execute("SELECT MAX(stage_order) FROM Request_approvals_stages WHERE request_id=?;", (self.request_id,)).fetchone()[0]
            if not max_stage:
                max_stage = 0
            else:
                max_stage = int(max_stage) + 1

            for stage_order, acceptor_id in enumerate(dialog.accepted_users):
                cur.execute("""
                            INSERT INTO Request_approvals_stages(approval_status, stage_order, request_id, acceptor_id) 
                            VALUES (?, ?, ?, ?)
                            """, (approval_status, max_stage + stage_order if dialog.is_step_by_step else 1, self.request_id, acceptor_id))

            con.commit()
            con.close()
        self.model.select()

    def remove_accept_row(self):
        selected_rows = self.ui.tableView.selectionModel().selectedIndexes()
        if not selected_rows:
            QMessageBox.warning(self, "Ошибка", "Не выбрана строка для удаления.")
            return

        confirm = QMessageBox.question(
            self, "Подтверждение удаления",
            "Вы уверены, что хотите удалить выбранные строки?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            for index in reversed(selected_rows):  # Удаляем строки в обратном порядке
                self.model.removeRow(index.row())