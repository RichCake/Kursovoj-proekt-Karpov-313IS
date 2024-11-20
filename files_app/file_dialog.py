import sqlite3

from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

from interfaces.ui_file_dialog import Ui_FileDialog


class FileDialog(QDialog):
    def __init__(self, parent, invoice_id):
        super().__init__()
        self.parent = parent
        self.invoice_id = invoice_id
        self.ui = Ui_FileDialog()
        self.ui.setupUi(self)

        # Подключение сигналов к слотам
        self.ui.attach_file.clicked.connect(self.attach_file)
        self.ui.delete_file.clicked.connect(self.delete_file)
        self.ui.open_file.clicked.connect(self.open_file)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

        self.load_file_path()

    def load_file_path(self):
        """Загружает текущий путь к файлу из базы данных."""
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        cur.execute("SELECT file_path FROM Invoice WHERE id = ?", (self.invoice_id,))
        result = cur.fetchone()
        con.close()

        if result and result[0]:
            self.ui.filename_lbl.setText(result[0])
        else:
            self.ui.filename_lbl.setText("Файл не прикреплен.")

    def attach_file(self):
        """Прикрепляет новый файл к счету и сохраняет его в базе."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл")
        if file_path:
            # Сохраняем путь в базе данных
            con = sqlite3.connect(self.parent.database_file)
            cur = con.cursor()
            cur.execute("UPDATE Invoice SET file_path = ? WHERE id = ?", (file_path, self.invoice_id))
            con.commit()
            con.close()

            # Обновляем отображение
            self.ui.filename_lbl.setText(file_path)
            QMessageBox.information(self, "Успех", "Файл успешно прикреплен.")

    def delete_file(self):
        """Удаляет прикрепленный файл из базы данных."""
        confirmation = QMessageBox.question(
            self, "Удалить файл", "Вы уверены, что хотите удалить прикрепленный файл?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirmation == QMessageBox.Yes:
            # Удаляем путь из базы данных
            con = sqlite3.connect(self.parent.database_file)
            cur = con.cursor()
            cur.execute("UPDATE Invoice SET file_path = NULL WHERE id = ?", (self.invoice_id,))
            con.commit()
            con.close()

            # Обновляем отображение
            self.ui.filename_lbl.setText("Файл не прикреплен.")
            QMessageBox.information(self, "Успех", "Файл успешно удален.")

    def open_file(self):
        """Открывает прикрепленный файл через системное приложение."""
        file_path = self.ui.filename_lbl.text()
        if file_path and file_path != "Файл не прикреплен.":
            QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))
        else:
            QMessageBox.warning(self, "Ошибка", "Файл не прикреплен.")
