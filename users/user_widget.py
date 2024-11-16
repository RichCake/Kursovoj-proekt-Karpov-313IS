import sqlite3

from PySide6.QtWidgets import QWidget, QMessageBox

from interfaces.ui_user_widget import Ui_User_widget


class UserWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_User_widget()
        self.ui.setupUi(self)
        self.ui.delete_btn.hide()
        self.ui.change_password_frame.hide()

        self.ui.save_btn.clicked.connect(self.save_request)
        self.ui.close_btn.clicked.connect(parent.close_current_tab)
        self.ui.delete_btn.clicked.connect(self.delete_request)
        self.ui.chenge_password_btn.clicked.connect(self.change_password)

    def set_is_created(self):
        self.ui.save_btn.clicked.disconnect()
        self.ui.save_btn.clicked.connect(self.update_request)
        self.ui.delete_btn.show()
        self.ui.change_password_frame.show()
        self.ui.login_edit.setDisabled(True)
        self.ui.password_edit.setDisabled(True)

    def check_and_return_editable_fields(self):
        first_name = self.ui.first_name_edit.text()
        second_name = self.ui.second_name_edit.text()
        third_name = self.ui.third_name_edit.text()
        position = self.ui.position_edit.text()
        login = self.ui.login_edit.text()
        if not login:
            QMessageBox.warning(self, "Предупреждение", "Необходимо заполнить поле Логин")
            return
        password = self.ui.password_edit.text()
        if not password:
            QMessageBox.warning(self, "Предупреждение", "Необходимо заполнить поле Пароль")
            return
        return first_name, second_name, third_name, position, login, password

    def save_request(self):
        first_name, second_name, third_name, position, login, password = self.check_and_return_editable_fields()
        access_rights = self.ui.access_rights_combobox.currentText()
        purchaser = access_rights == "Закупщик"

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO Users(login, password, first_name, second_name, third_name, position, purchaser) VALUES (?, ?, ?, ?, ?, ?, ?);", 
                        (login, password, first_name, second_name, third_name, position, purchaser))
        except sqlite3.Error as err:
            QMessageBox.critical(self, "Неизвестная ошибка", str(err))
        
        user_id = cur.lastrowid
        con.commit()
        con.close()

        self.parent.tab_widget.setTabText(self.parent.tab_widget.currentIndex(), f"Пользователь {user_id}")
        self.ui.id_ldl.setText(str(user_id))
        self.set_is_created()

        self.parent.status_bar.showMessage("Пользователь сохранен", 3000)

    def update_request(self):
        first_name, second_name, third_name, position, login, password = self.check_and_return_editable_fields()
        user_id = self.ui.id_ldl.text()
        access_rights = self.ui.access_rights_combobox.currentText()
        purchaser = access_rights == "Закупщик"

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        try:
            cur.execute("UPDATE Users SET first_name=?, second_name=?, third_name=?, position=?, purchaser=? WHERE id=?;", (first_name, second_name, third_name, position, purchaser, user_id))
        except sqlite3.Error as err:
            QMessageBox.critical(self, "Неизвестная ошибка", str(err))
        con.commit()
        con.close()

        self.parent.status_bar.showMessage("Пользователь сохранен", 3000)

    def load_data(self, user_id):
        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
    
        user = cur.execute("SELECT first_name, second_name, third_name, position, login, password, purchaser FROM Users WHERE id=?;", (str(user_id),)).fetchone()
        if user:
            self.ui.first_name_edit.setText(user[0])
            self.ui.second_name_edit.setText(user[1])
            self.ui.third_name_edit.setText(user[2])
            self.ui.position_edit.setText(user[3])
            self.ui.login_edit.setText(user[4])
            self.ui.password_edit.setText(user[5])
            if user[6]:
                self.ui.access_rights_combobox.setCurrentIndex(1)
            else:
                self.ui.access_rights_combobox.setCurrentIndex(0)

        con.close()
        self.set_is_created()
        self.ui.id_ldl.setText(str(user_id))

    def delete_request(self):
        res = QMessageBox.warning(self, "Предупреждение", "Вы уверены, что хотите удалить объект?", QMessageBox.Yes, QMessageBox.No)
        if res == QMessageBox.No:
            return
        user_id = self.ui.id_ldl.text()

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        cur.execute("DELETE FROM USERS WHERE id=?", (user_id,))
        con.commit()
        con.close()

        self.parent.close_current_tab()

        self.parent.status_bar.showMessage("Пользователь удален", 3000)

    def change_password(self):
        password1 = self.ui.new_password1_edit.text()
        password2 = self.ui.new_password2_edit.text()
        if password1 != password2:
            QMessageBox.warning(self, "Предупреждение", "Введенные пароли не совпадают")
            return
        user_id = self.ui.id_ldl.text()

        con = sqlite3.connect(self.parent.database_file)
        cur = con.cursor()
        try:
            cur.execute("UPDATE Users SET password=? WHERE id=?;", (password1, user_id))
        except sqlite3.Error as err:
            QMessageBox.critical(self, "Неизвестная ошибка", str(err))
        con.commit()
        con.close()
        QMessageBox.information(self, "Завершено успешно", "Пароль изменен")