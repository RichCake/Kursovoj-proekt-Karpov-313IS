import sqlite3
from PySide6.QtWidgets import QStyledItemDelegate, QPushButton, QHBoxLayout, QLineEdit, QWidget, QDialog, QTableWidgetItem
from PySide6.QtCore import QDateTime, Qt

from nomenclature.nomenclature_dialog import NomenclatureDialog

class DateDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        if isinstance(value, str):
            # Обрезаем строку до секунд, чтобы исключить доли секунды
            value = value.split(".")[0]
            # Преобразуем строку в QDateTime, используя соответствующий формат
            date_time = QDateTime.fromString(value, "yyyy-MM-dd HH:mm:ss")
            # Проверяем, удалось ли преобразование
            if date_time.isValid():
                # Возвращаем только дату
                return date_time.date().toString("yyyy-MM-dd")
        return value
    

class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return None


class EditableDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        # Создаём кастомный редактор с кнопками
        editor = QWidget(parent)
        layout = QHBoxLayout(editor)
        layout.setContentsMargins(0, 0, 0, 0)

        # Поле для ввода текста
        line_edit = QLineEdit(editor)
        layout.addWidget(line_edit)

        # Кнопка открытия окна
        open_button = QPushButton("■", editor)
        open_button.setFixedSize(20, 20)
        layout.addWidget(open_button)

        # Привязка событий
        open_button.clicked.connect(lambda: self.open_nomenclature_window_with_index(index))

        return editor

    def open_nomenclature_window_with_index(self, index):
        self.open_nomenclature_window(index)

    def setEditorData(self, editor, index):
        line_edit = editor.findChild(QLineEdit)
        line_edit.setText(index.data(Qt.DisplayRole))

    def setModelData(self, editor, model, index):
        line_edit = editor.findChild(QLineEdit)
        model.setData(index, line_edit.text(), Qt.EditRole)

    def show_dropdown(self, line_edit):
        # Здесь вы можете сделать запрос в базу данных и создать выпадающий список
        print(f"Показываем выпадающий список для подстроки: {line_edit.text()}")

    def open_nomenclature_window(self, index):
        dialog = NomenclatureDialog(self.parent.parent)
        if dialog.exec() == QDialog.Accepted:
            con = sqlite3.connect(self.parent.database_file)
            cur = con.cursor()
            nomenclature = cur.execute("SELECT * FROM Nomenclature WHERE id=?", (dialog.nomenclature_id,)).fetchone()
            con.close()

            if nomenclature:
                # Получаем доступ к таблице
                table = self.parent.ui.tableWidget

                # Определяем строку, в которой находится делегат
                row = index.row()

                # Устанавливаем значения в ячейки
                table.setItem(row, 0, QTableWidgetItem(str(nomenclature[0])))  # ID
                table.setItem(row, 1, QTableWidgetItem(nomenclature[1]))      # Наименование
                table.setItem(row, 2, QTableWidgetItem(nomenclature[2]))      # Другие данные