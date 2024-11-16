from PySide6.QtWidgets import QDialog, QTableView, QMessageBox
from PySide6.QtSql import QSqlRelationalTableModel
from PySide6.QtGui import QStandardItem, QStandardItemModel

from interfaces.ui_accept_dialog import Ui_Accept_dialog


class AcceptDialog(QDialog):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()
        self.ui = Ui_Accept_dialog()
        self.ui.setupUi(self)

        # Модель для таблицы пользователей
        self.user_model = QSqlRelationalTableModel()
        self.user_model.setTable("Users")
        self.user_model.select()

        self.ui.user_table.setModel(self.user_model)
        self.ui.user_table.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)
        self.ui.user_table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.user_table.hideColumn(0)
        self.ui.user_table.hideColumn(5)
        self.ui.user_table.hideColumn(6)
        self.ui.user_table.hideColumn(7)
        self.ui.user_table.resizeColumnsToContents()

        # Модель для таблицы выбранных пользователей
        self.accept_model = QStandardItemModel(0, 4, self)  # Пустая модель с четырьмя колонками
        self.accept_model.setHorizontalHeaderLabels(["ID", "Имя", "Фамилия", "Отчество"])
        self.ui.accept_table.setModel(self.accept_model)
        self.ui.accept_table.setEditTriggers(QTableView.EditTriggers.NoEditTriggers)
        self.ui.accept_table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.accept_table.hideColumn(0)
        self.ui.accept_table.resizeColumnsToContents()

        # События для кнопок
        self.ui.add_btn.clicked.connect(self.add_user)
        self.ui.remove_btn.clicked.connect(self.remove_user)
        self.ui.up_btn.clicked.connect(self.move_up)
        self.ui.down_btn.clicked.connect(self.move_down)

        # Событие для подтверждения выбора
        self.ui.buttonBox.accepted.connect(self.select_accept_users)

    def add_user(self):
        """Перенос пользователя из user_table в accept_table."""
        selected_rows = self.ui.user_table.selectionModel().selectedRows()

        if not selected_rows:
            QMessageBox.warning(self, "Ошибка", "Выберите хотя бы одного пользователя.")
            return

        for index in selected_rows:
            row = index.row()
            user_id = self.user_model.data(self.user_model.index(row, 0))
            first_name = self.user_model.data(self.user_model.index(row, 1))
            second_name = self.user_model.data(self.user_model.index(row, 2))
            third_name = self.user_model.data(self.user_model.index(row, 3))

            # Проверка на наличие в accept_table
            if self.find_in_accept_table(user_id):
                continue

            # Добавление в accept_table
            self.add_to_accept_table(user_id, first_name, second_name, third_name)
        self.ui.accept_table.resizeColumnsToContents()

    def remove_user(self):
        """Удаление пользователя из accept_table."""
        selected_rows = self.ui.accept_table.selectionModel().selectedRows()

        if not selected_rows:
            QMessageBox.warning(self, "Ошибка", "Выберите хотя бы одного пользователя для удаления.")
            return

        for index in sorted(selected_rows, reverse=True):  # Удаление с конца списка
            self.accept_model.removeRow(index.row())

    def add_to_accept_table(self, user_id, first_name, second_name, third_name):
        """Добавляет пользователя в accept_table."""
        id_item = QStandardItem(str(user_id))
        first_name_item = QStandardItem(first_name)
        second_name_item = QStandardItem(second_name)
        third_name_item = QStandardItem(third_name)

        self.accept_model.appendRow([id_item, first_name_item, second_name_item, third_name_item])

    def find_in_accept_table(self, user_id):
        """Проверяет, есть ли пользователь с данным ID в accept_table."""
        for row in range(self.accept_model.rowCount()):
            if self.accept_model.item(row, 0).text() == str(user_id):
                return True
        return False

    def move_up(self):
        """Перемещает выделенную строку вверх."""
        selected_rows = self.ui.accept_table.selectionModel().selectedRows()

        if len(selected_rows) != 1:
            QMessageBox.warning(self, "Ошибка", "Выберите одну строку для перемещения.")
            return

        row = selected_rows[0].row()
        if row == 0:
            return  # Нельзя поднять первую строку выше

        self.swap_rows(row, row - 1)

    def move_down(self):
        """Перемещает выделенную строку вниз."""
        selected_rows = self.ui.accept_table.selectionModel().selectedRows()

        if len(selected_rows) != 1:
            QMessageBox.warning(self, "Ошибка", "Выберите одну строку для перемещения.")
            return

        row = selected_rows[0].row()
        if row == self.accept_model.rowCount() - 1:
            return  # Нельзя опустить последнюю строку ниже

        self.swap_rows(row, row + 1)

    def swap_rows(self, row1, row2):
        """Меняет местами две строки в модели accept_table."""
        items_row1 = [self.accept_model.item(row1, col).text() for col in range(self.accept_model.columnCount())]
        items_row2 = [self.accept_model.item(row2, col).text() for col in range(self.accept_model.columnCount())]

        # Заменяем строки, создавая новые элементы
        for col in range(self.accept_model.columnCount()):
            self.accept_model.setItem(row1, col, QStandardItem(items_row2[col]))
            self.accept_model.setItem(row2, col, QStandardItem(items_row1[col]))

        # Обновляем выделение
        self.ui.accept_table.selectRow(row2)

    def select_accept_users(self):
        """Сохраняет выбранных пользователей из accept_table."""
        selected_user_ids = []
        for row in range(self.accept_model.rowCount()):
            user_id = self.accept_model.item(row, 0).text()
            selected_user_ids.append(int(user_id))

        self.accepted_users = selected_user_ids