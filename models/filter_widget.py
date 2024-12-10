from PySide6.QtWidgets import QWidget, QDialog
from ui.migration.filter import Ui_Form


class FilterWidget(QDialog):
    def __init__(self, parent=None):
        super(FilterWidget, self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
