import sqlite3

from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlRelationalTableModel, QSqlTableModel
from PySide6.QtWidgets import QMessageBox, QWidget

from interfaces.ui_vender import Ui_Form


class VenderWidget(QWidget):
    def __init__(self, parent, vender_id=None):
        super().__init__()
        self.parent = parent
        self.vender_id = vender_id
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Настройка начального состояния кнопки удаления
        self.ui.delete_btn.setDisabled(self.vender_id is None)

        # Настройка модели
        self.model = QSqlRelationalTableModel(self)
        self.model.setTable("Vendor_managers")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        # Задаем заголовки таблицы
        self.model.setHeaderData(1, Qt.Horizontal, "Имя")
        self.model.setHeaderData(2, Qt.Horizontal, "Фамилия")
        self.model.setHeaderData(3, Qt.Horizontal, "Отчество")
        self.model.setHeaderData(4, Qt.Horizontal, "Должность")
        self.model.setHeaderData(5, Qt.Horizontal, "Номер телефона")

        # Фильтрация по ID поставщика
        if self.vender_id is not None:
            self.model.setFilter(f"vender_id = {self.vender_id}")
            self.load_vendor_data()
        else:
            self.model.setFilter("vender_id = -1")

        self.model.select()

        # Настройка таблицы
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.hideColumn(0)  # Скрываем колонку ID
        self.ui.tableView.hideColumn(6)  # Скрываем колонку vendor_id
        self.ui.tableView.resizeColumnsToContents()

        # Привязка кнопок
        self.ui.save_btn.clicked.connect(self.save_vendor)
        self.ui.delete_btn.clicked.connect(self.delete_vendor)
        self.ui.add_btn.clicked.connect(self.add_manager_row)
        self.ui.remove_btn.clicked.connect(self.remove_manager_row)
        self.ui.cancel_btn.clicked.connect(self.revert_contacts)

    def revert_contacts(self):
        self.model.revertAll()
        self.model.select()

    def load_vendor_data(self):
        """Загрузка данных контрагента по ID."""
        try:
            con = sqlite3.connect(self.parent.database_file)
            cur = con.cursor()
            cur.execute("SELECT name, address FROM Vendor WHERE id = ?", (self.vender_id,))
            result = cur.fetchone()
            if result:
                name, address = result
                self.ui.name_edit.setText(name)
                self.ui.address_edit.setText(address)
            else:
                QMessageBox.warning(self, "Ошибка", "Контрагент с указанным ID не найден.")
        except sqlite3.DatabaseError as e:
            QMessageBox.critical(self, "Ошибка базы данных", f"Не удалось загрузить данные контрагента: {e}")
        finally:
            con.close()

    def save_vendor(self):
        """Сохранение поставщика и менеджеров."""
        name = self.ui.name_edit.text().strip()
        address = self.ui.address_edit.text().strip()

        if not name:
            QMessageBox.warning(self, "Ошибка", "Вы не заполнили Наименование контрагента")
            return

        try:
            con = sqlite3.connect(self.parent.database_file)
            cur = con.cursor()

            if self.vender_id is None:
                # Создание нового поставщика
                cur.execute("INSERT INTO Vendor (name, address) VALUES (?, ?)", (name, address))
                self.vender_id = cur.lastrowid
                QMessageBox.information(self, "Успех", "Поставщик успешно создан.")
            else:
                # Обновление существующего поставщика
                cur.execute("UPDATE Vendor SET name = ?, address = ? WHERE id = ?", (name, address, self.vender_id))
                QMessageBox.information(self, "Успех", "Данные поставщика успешно обновлены.")

            con.commit()
            self.model.submitAll()

            # Устанавливаем фильтр для модели после создания поставщика
            self.model.setFilter(f"vender_id = {self.vender_id}")
            self.model.select()
            self.ui.delete_btn.setDisabled(False)

        except sqlite3.DatabaseError as e:
            QMessageBox.critical(self, "Ошибка базы данных", f"Не удалось сохранить данные: {e}")
        finally:
            con.close()

    def delete_vendor(self):
        """Удаление поставщика."""
        confirm = QMessageBox.question(
            self, "Подтверждение удаления",
            "Вы уверены, что хотите удалить этого поставщика и всех его менеджеров?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                con = sqlite3.connect(self.parent.database_file)
                cur = con.cursor()
                cur.execute("DELETE FROM Vendor_managers WHERE vender_id = ?", (self.vender_id,))
                cur.execute("DELETE FROM Vendor WHERE id = ?", (self.vender_id,))
                con.commit()
                QMessageBox.information(self, "Успех", "Поставщик успешно удален.")
                self.parent.close_current_tab()
            except sqlite3.DatabaseError as e:
                QMessageBox.critical(self, "Ошибка базы данных", f"Не удалось удалить поставщика: {e}")
            finally:
                con.close()

    def add_manager_row(self):
        """Добавление строки для нового менеджера."""
        if self.vender_id is None:
            QMessageBox.warning(self, "Ошибка", "Сначала сохраните поставщика.")
            return

        row = self.model.rowCount()
        self.model.insertRow(row)
        self.model.setData(self.model.index(row, 6), self.vender_id)  # Установка vendor_id для новой строки
        self.ui.tableView.scrollToBottom()

    def remove_manager_row(self):
        """Удаление выбранной строки менеджера."""
        selected_rows = self.ui.tableView.selectionModel().selectedIndexes()
        if not selected_rows:
            QMessageBox.warning(self, "Ошибка", "Не выбрана строка для удаления.")
            return
        
        rows_to_remove = [index.row() for index in selected_rows]
        for row in rows_to_remove:
            self.model.removeRow(row)