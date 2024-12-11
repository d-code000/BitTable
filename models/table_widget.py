import csv

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QHeaderView, QAbstractItemView, QMessageBox, QFileDialog

from models.filter_widget import FilterWidget
from models.table import Subscriber
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

        self.ui.subscribersTable.setModel(subscriber_table)
        self.ui.subscribersTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.subscribersTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.subscribersTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.subscribersTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

    def save_file(self):
        """Сохранение данных таблицы в CSV-файл."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "CSV Files (*.csv)")
        if not file_path:
            return

        try:
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "ФИО", "Номер телефона", "Тип клиента", "Дата оформления"])
                for subscriber in subscriber_table.subscribers:
                    writer.writerow([
                        subscriber.user_id,
                        subscriber.name,
                        subscriber.phone_number,
                        subscriber.user_type,
                        subscriber.date
                    ])
            QMessageBox.information(self, "Сохранение файла", "Файл успешно сохранён.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка сохранения", f"Не удалось сохранить файл: {e}")

    def open_file(self):
        """Открытие данных из CSV-файла."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "CSV Files (*.csv)")
        if not file_path:
            return

        try:
            with open(file_path, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                headers = next(reader, None)
                subscriber_table.subscribers.clear()
                for row in reader:
                    if len(row) == 5:
                        subscriber = Subscriber(
                            user_id=int(row[0]),
                            name=row[1],
                            phone_number=row[2],
                            user_type=row[3],
                            date=row[4]
                        )
                        subscriber_table.addRow(subscriber)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка открытия", f"Не удалось открыть файл: {e}")

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
