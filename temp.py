from PySide6.QtWidgets import QTreeView, QTableView, QVBoxLayout, QWidget, QApplication
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QSortFilterProxyModel

class CategoryModel(QStandardItemModel):
    def __init__(self, categories):
        super().__init__()
        self.setHorizontalHeaderLabels(['Категории'])
        self.build_tree(categories)

    def build_tree(self, categories):
        items_by_id = {}
        for cat in categories:
            item = QStandardItem(cat['name'])
            items_by_id[cat['id']] = item
            if cat['parent_category_id']:
                items_by_id[cat['parent_category_id']].appendRow(item)
            else:
                self.appendRow(item)

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Пример данных, которые можно загрузить из таблицы Nomenclature_category
        categories = [
            {'id': 1, 'name': 'Продукты', 'parent_category_id': None},
            {'id': 2, 'name': 'Техника', 'parent_category_id': None},
            {'id': 3, 'name': 'Фрукты', 'parent_category_id': 1},
        ]
        
        # Пример данных для отображения в таблице
        nomenclature_data = [
            {'name': 'Яблоко', 'unit': 'шт', 'category_id': 3},
            {'name': 'Компьютер', 'unit': 'шт', 'category_id': 2},
        ]
        
        # Инициализация модели для дерева
        self.tree_model = CategoryModel(categories)
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.tree_model)
        self.tree_view.expandAll()
        
        # Инициализация модели для таблицы
        self.table_model = QStandardItemModel()
        self.table_model.setHorizontalHeaderLabels(['Название', 'Ед.изм.'])
        for item in nomenclature_data:
            row = [QStandardItem(item['name']), QStandardItem(item['unit'])]
            self.table_model.appendRow(row)
        
        # Фильтр для таблицы
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.table_model)
        
        self.table_view = QTableView()
        self.table_view.setModel(self.proxy_model)

        # Событие при выборе категории в дереве
        self.tree_view.selectionModel().selectionChanged.connect(self.on_tree_selection_changed)
        
        # Макет
        layout = QVBoxLayout()
        layout.addWidget(self.tree_view)
        layout.addWidget(self.table_view)
        self.setLayout(layout)

    def on_tree_selection_changed(self, selected, deselected):
        index = self.tree_view.selectionModel().currentIndex()
        category_name = self.tree_model.itemFromIndex(index).text()
        # Здесь должна быть фильтрация данных по ID категории
        # ...

app = QApplication([])
window = MainWidget()
window.show()
app.exec()