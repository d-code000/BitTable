from PySide6.QtWidgets import QDialog
from ui.migration.add import Ui_FormAdd


class AddWidget(QDialog):
    def __init__(self, parent=None):
        super(AddWidget, self).__init__(parent)

        self.ui = Ui_FormAdd()
        self.ui.setupUi(self)
