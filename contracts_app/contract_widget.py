import sqlite3

import PySide6.QtSql
from PySide6.QtCore import QDate, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox, QWidget

from interfaces.ui_contract import Ui_Contract
from vender_app.vender_dialog import VenderDialog


class ContractWidget(QWidget):
    def __init__(self, parent, contract_id=None):
        super().__init__()
        self.parent = parent
        self.contract_id = contract_id
        self.ui = Ui_Contract()
        self.ui.setupUi(self)
        self.ui.delete_btn.hide()

        # Подключение кнопок
        self.ui.vendor_btn.clicked.connect(self.open_vender_dialog)
        self.ui.attach_file.clicked.connect(self.attach_file)
        self.ui.delete_file.clicked.connect(self.delete_file)
        self.ui.open_file.clicked.connect(self.open_file)
        self.ui.save_btn.clicked.connect(self.save_contract)
        self.ui.delete_btn.clicked.connect(self.delete_contract)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)

        if self.contract_id:
            self.load_data()
            self.ui.delete_btn.show()

    def load_data(self):
        """Загружает данные контракта из базы для редактирования."""
        with sqlite3.connect(self.parent.database_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT number, date, vender_id, file_path FROM Contracts WHERE id = ?", (self.contract_id,))
            contract = cursor.fetchone()
            if contract:
                self.ui.number_edit.setText(contract[0])
                self.ui.date_edit.setDate(QDate.fromString(contract[1], "yyyy-MM-dd"))
                vendor_id = contract[2]
                file_path = contract[3]
                
                # Получение названия поставщика
                cursor.execute("SELECT name FROM Vendor WHERE id = ?", (vendor_id,))
                vendor = cursor.fetchone()
                if vendor:
                    self.ui.vendor_lbl.setText(vendor[0])
                
                self.ui.filename_lbl.setText(file_path if file_path else "")

    def save_contract(self):
        """Сохраняет новый контракт в базе данных."""
        number = self.ui.number_edit.text()
        date = self.ui.date_edit.date().toString("yyyy-MM-dd")
        vendor_name = self.ui.vendor_lbl.text()
        file_path = self.ui.filename_lbl.text()

        if not number:
            QMessageBox.warning(self, "Ошибка", "Вы не заполнили номер договора")
            return
        if not vendor_name:
            QMessageBox.warning(self, "Ошибка", "Вы не добавили контрагента")
            return
        if not date:
            QMessageBox.warning(self, "Ошибка", "Вы не заполнили дату договора")
            return

        with sqlite3.connect(self.parent.database_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM Vendor WHERE name = ?", (vendor_name,))
            vendor = cursor.fetchone()
            if not vendor:
                QMessageBox.warning(self, "Ошибка", "Выбранный поставщик не найден.")
                return
            vendor_id = vendor[0]

            if self.contract_id:
                # Обновление контракта
                cursor.execute("""
                    UPDATE Contracts
                    SET number = ?, date = ?, vender_id = ?, file_path = ?
                    WHERE id = ?
                """, (number, date, vendor_id, file_path, self.contract_id))
            else:
                # Сохранение нового контракта
                cursor.execute("""
                    INSERT INTO Contracts (number, date, vender_id, file_path)
                    VALUES (?, ?, ?, ?)
                """, (number, date, vendor_id, file_path))
                self.ui.delete_btn.hide()
            conn.commit()

        QMessageBox.information(self, "Успех", "Контракт успешно сохранен.")

    def delete_contract(self):
        """Удаляет контракт из базы данных."""
        if not self.contract_id:
            QMessageBox.warning(self, "Ошибка", "Контракт не найден.")
            return

        with sqlite3.connect(self.parent.database_file) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Contracts WHERE id = ?", (self.contract_id,))
            conn.commit()

        QMessageBox.information(self, "Успех", "Контракт успешно удален.")
        self.parent.close_current_tab()

    def attach_file(self):
        """Прикрепляет файл к контракту."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл")
        if file_path:
            self.ui.filename_lbl.setText(file_path)

    def delete_file(self):
        """Удаляет прикрепленный файл."""
        self.ui.filename_lbl.setText("")

    def open_file(self):
        """Открывает прикрепленный файл."""
        file_path = self.ui.filename_lbl.text()
        if file_path:
            QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))
        else:
            QMessageBox.warning(self, "Ошибка", "Файл не прикреплен.")

    def open_vender_dialog(self):
        """Открывает диалог выбора поставщика."""
        ans = QMessageBox.warning(
            self, 
            "Предупреждение", 
            "Если изменить контрагента в контракте, то он изменится во всех связанных счетах", 
            QMessageBox.Ok,
            QMessageBox.Cancel,
            )
        if ans == QMessageBox.Cancel:
            return
        dialog = VenderDialog(self.parent)
        if dialog.exec() == QDialog.Accepted:
            self.ui.vendor_lbl.setText(dialog.vender)