from PySide6.QtWidgets import QMainWindow

from models.filter_widget import FilterWidget
from ui.migration.main import Ui_MainWindow

from models.add_widget import AddWidget
from models.edit_widget import EditWidget


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

    def save_file(self):
        pass

    def open_file(self):
        pass

    def add_widget(self):
        widget = AddWidget(self)
        widget.exec()

    def edit_widget(self):
        widget = EditWidget(self)
        widget.exec()

    def delete_line(self):
        pass

    def filter_widget(self):
        widget = FilterWidget(self)
        widget.exec()

    def setting_widget(self):
        pass
