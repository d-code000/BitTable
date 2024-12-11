from PySide6.QtWidgets import QDialog, QHeaderView
from ui.migration.filter import Ui_Form
from models import subscriber_table


class FilterWidget(QDialog):
    def __init__(self, parent=None):
        super(FilterWidget, self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.subscribersTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.subscribersTable.setModel(subscriber_table)
