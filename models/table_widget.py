from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QHeaderView, QAbstractItemView, QMessageBox

from models.filter_widget import FilterWidget
from ui.migration.main import Ui_MainWindow

from models.add_widget import AddWidget
from models.edit_widget import EditWidget
from models import subscriber_table


class TableWidget(QMainWindow):
    def __init__(self):
        super(TableWidget, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.saveFileAction.triggered.connect(self.save_file)
        self.ui.openFileAction.triggered.connect(self.open_file)
        self.ui.addAction.triggered.connect(self.add_widget)
        self.ui.editAction.triggered.connect(self.edit_widget)
        self.ui.deleteAction.triggered.connect(self.delete_line)
        self.ui.filterAction.triggered.connect(self.filter_widget)
        self.ui.programSettingAction.triggered.connect(self.setting_widget)

        self.ui.subscribersTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.subscribersTable.setModel(subscriber_table)
        self.ui.subscribersTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.subscribersTable.setSelectionMode(QAbstractItemView.SingleSelection)

    def save_file(self):
        pass

    def open_file(self):
        pass

    def add_widget(self):
        widget = AddWidget(self)
        widget.exec()

    def edit_widget(self):
        selected_indexes = self.ui.subscribersTable.selectionModel().selectedRows()

        if not selected_indexes:
            QMessageBox.warning(self, "Редактирование записи", "Выберите строку для редактирования.")
            return

        row = selected_indexes[0].row()
        sub = subscriber_table.subscribers[row]
        widget = EditWidget(sub, row, self)
        widget.exec()

    def delete_line(self):
        selected_indexes = self.ui.subscribersTable.selectionModel().selectedRows()

        if not selected_indexes:
            QMessageBox.warning(self, "Удаление строки", "Выберите строку для удаления.")
            return

        for index in sorted(selected_indexes, key=lambda x: x.row(), reverse=True):
            subscriber_table.removeRow(index.row())

    def filter_widget(self):
        widget = FilterWidget(self)
        widget.exec()

    def setting_widget(self):
        pass
