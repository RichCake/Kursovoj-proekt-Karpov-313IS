import sqlite3
from PySide6.QtWidgets import QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Main Window
class ReportWidget(QWidget):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()
        self.setWindowTitle("Отчеты")

        # Buttons to switch between reports
        self.layout = QVBoxLayout(self)
        self.buttons = {
            "Объем заявок по месяцам": Report1,
            "Топ-10 поставщиков": Report2,
            "Статистика по категориям": Report3,
            "Рейтинг сотрудников": Report6,
        }
        for name, report_class in self.buttons.items():
            btn = QPushButton(name)
            btn.clicked.connect(lambda checked, cls=report_class, parent=parent: self.show_report(cls, parent))
            self.layout.addWidget(btn)

        self.current_widget = None

    def show_report(self, report_class, parent):
        if self.current_widget:
            self.current_widget.deleteLater()
        self.current_widget = report_class(parent)
        self.layout.addWidget(self.current_widget)


# Report 1: Объем заявок по месяцам
class Report1(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout(self)
        conn = sqlite3.connect(parent.database_file)
        cursor = conn.cursor()
        cursor.execute("SELECT strftime('%Y-%m', created_at) AS month, COUNT(*) FROM Requests GROUP BY month")
        data = cursor.fetchall()
        conn.close()

        months, counts = zip(*data) if data else ([], [])
        fig = Figure(figsize=(5, 3))
        ax = fig.add_subplot(111)
        ax.bar(months, counts)
        ax.set_title("Объем заявок по месяцам")
        ax.set_xlabel("Месяц")
        ax.set_ylabel("Количество заявок")

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)


# Report 2: Топ-10 поставщиков
class Report2(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout(self)
        conn = sqlite3.connect(parent.database_file)
        cursor = conn.cursor()
        cursor.execute("""
                        SELECT Vendor.name, COUNT(*) 
                        FROM Invoice
                        LEFT JOIN Contracts ON Invoice.contract_id = Contracts.id
                        LEFT JOIN Vendor ON Contracts.vender_id = Vendor.id
                        GROUP BY Vendor.id
                        ORDER BY COUNT(*) DESC
                        LIMIT 10
                       """)
        data = cursor.fetchall()
        conn.close()

        table = QTableWidget(len(data), 2)
        table.setHorizontalHeaderLabels(["Поставщик", "Количество счетов"])
        for row, (supplier, count) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(supplier))
            table.setItem(row, 1, QTableWidgetItem(str(count)))
        table.resizeColumnsToContents()
        layout.addWidget(table)


# Report 3: Статистика по категориям
class Report3(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout(self)
        conn = sqlite3.connect(parent.database_file)
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT Request_category.name, COUNT(*) 
                       FROM Requests 
                       LEFT JOIN Request_category ON Requests.category_id = Request_category.id
                       GROUP BY Requests.category_id""")
        data = cursor.fetchall()
        conn.close()

        categories, counts = zip(*data) if data else ([], [])
        fig = Figure(figsize=(5, 3))
        ax = fig.add_subplot(111)
        ax.pie(counts, labels=categories, autopct="%1.1f%%")
        ax.set_title("Статистика по категориям")

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)


# Report 6: Рейтинг сотрудников
class Report6(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout(self)
        conn = sqlite3.connect(parent.database_file)
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT Users.login, COUNT(*) 
                       FROM Requests 
                       LEFT JOIN Users ON Requests.initiator_id = Users.id
                       GROUP BY Users.id 
                       ORDER BY COUNT(*) DESC
                       """)
        data = cursor.fetchall()
        conn.close()

        table = QTableWidget(len(data), 2)
        table.setHorizontalHeaderLabels(["Сотрудник", "Количество заявок"])
        for row, (employee, count) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(employee))
            table.setItem(row, 1, QTableWidgetItem(str(count)))
        layout.addWidget(table)