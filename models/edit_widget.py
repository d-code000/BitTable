from PySide6.QtWidgets import QDialog
from ui.migration.edit import Ui_FormEdit


class EditWidget(QDialog):
    def __init__(self, parent=None):
        super(EditWidget, self).__init__(parent)

        self.ui = Ui_FormEdit()
        self.ui.setupUi(self)
