from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtWidgets import QDialog, QHeaderView
from ui.migration.filter import Ui_Form
from models import subscriber_table


class FilterWidget(QDialog):
    def __init__(self, parent=None):
        super(FilterWidget, self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(subscriber_table)
        self.ui.subscribersTable.setModel(self.proxy_model)
        self.ui.subscribersTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.subscribersTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        self.ui.filterButton.clicked.connect(self.filter)
        self.ui.resetButton.clicked.connect(self.reset_filter)

    def filter(self):
        filter_text = self.ui.comboBox.currentText()

        self.proxy_model.setFilterKeyColumn(3)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_model.setFilterFixedString(filter_text)

    def reset_filter(self):
        self.proxy_model.setFilterFixedString("")
