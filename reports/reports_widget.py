import sqlite3

import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class ReportWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Отчеты")
        layout = QVBoxLayout(self)

        btn1 = QPushButton("Отчет 1: Объем заявок по месяцам")
        btn1.clicked.connect(self.parent.open_report1_widget)
        layout.addWidget(btn1)

        btn2 = QPushButton("Отчет 2: Статистика по категориям")
        btn2.clicked.connect(self.parent.open_report2_widget)
        layout.addWidget(btn2)

        btn3 = QPushButton("Отчет 3: Сколько заказано каждой номенклатуры")
        btn3.clicked.connect(self.parent.open_report3_widget)
        layout.addWidget(btn3)

        btn4 = QPushButton("Отчет 4: Отчет по стадиям согласования")
        btn4.clicked.connect(self.parent.open_report4_widget)
        layout.addWidget(btn4)


class Report1(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout(self)
        self.parent = parent
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

        export_btn = QPushButton("Выгрузить в Excel")
        export_btn.clicked.connect(lambda: self.export_to_excel(data, ["Месяц", "Количество"]))
        layout.addWidget(export_btn)

    def export_to_excel(self, data, columns):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить отчет", "", "Excel Files (*.xlsx)")
        if file_path:
            df = pd.DataFrame(data, columns=columns)
            df.to_excel(file_path, index=False)


class Report2(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout(self)
        self.parent = parent
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

        export_btn = QPushButton("Выгрузить в Excel")
        export_btn.clicked.connect(lambda: self.export_to_excel(data, ["Категория", "Количество"]))
        layout.addWidget(export_btn)

    def export_to_excel(self, data, columns):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить отчет", "", "Excel Files (*.xlsx)")
        if file_path:
            df = pd.DataFrame(data, columns=columns)
            df.to_excel(file_path, index=False)


class Report3(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout(self)
        self.parent = parent
        conn = sqlite3.connect(parent.database_file)
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT Nomenclature.name, SUM(Request_items.amount)
                       FROM Request_items
                       JOIN Nomenclature ON Request_items.item_id = Nomenclature.id
                       GROUP BY Request_items.item_id""")
        data = cursor.fetchall()
        conn.close()

        names, counts = zip(*data) if data else ([], [])
        fig = Figure(figsize=(5, 3))
        ax = fig.add_subplot(111)
        ax.pie(counts, labels=names, autopct="%1.1f%%")
        ax.set_title("Количество заказанных номенклатур")

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

        export_btn = QPushButton("Выгрузить в Excel")
        export_btn.clicked.connect(lambda: self.export_to_excel(data, ["Номенклатура", "Количество"]))
        layout.addWidget(export_btn)

    def export_to_excel(self, data, columns):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить отчет", "", "Excel Files (*.xlsx)")
        if file_path:
            df = pd.DataFrame(data, columns=columns)
            df.to_excel(file_path, index=False)


class Report4(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout(self)
        self.parent = parent
        conn = sqlite3.connect(parent.database_file)
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT approval_status, COUNT(*) 
                       FROM Request_approvals_stages
                       GROUP BY approval_status""")
        data = cursor.fetchall()
        conn.close()

        statuses, counts = zip(*data) if data else ([], [])
        fig = Figure(figsize=(5, 3))
        ax = fig.add_subplot(111)
        ax.pie(counts, labels=statuses, autopct="%1.1f%%")
        ax.set_title("Статусы согласования")

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

        export_btn = QPushButton("Выгрузить в Excel")
        export_btn.clicked.connect(lambda: self.export_to_excel(data, ["Статус", "Количество"]))
        layout.addWidget(export_btn)

    def export_to_excel(self, data, columns):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить отчет", "", "Excel Files (*.xlsx)")
        if file_path:
            df = pd.DataFrame(data, columns=columns)
            df.to_excel(file_path, index=False)