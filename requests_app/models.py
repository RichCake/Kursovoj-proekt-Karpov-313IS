from PySide6.QtWidgets import QStyledItemDelegate
from PySide6.QtCore import QDateTime

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