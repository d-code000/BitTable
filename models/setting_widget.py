from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QDialog, QTableView
from ui.migration.setting import Ui_SettingForm


class SettingWidget(QDialog):
    def __init__(self, table: QTableView, parent=None):
        super(SettingWidget, self).__init__(parent)

        self.ui = Ui_SettingForm()
        self.ui.setupUi(self)
        self.table = table

        self.ui.fontSizeSpinBox.setMaximum(20)

        # set value
        self.ui.fontComboBox.setCurrentFont(self.table.font())
        self.ui.fontSizeSpinBox.setValue(self.table.fontInfo().pointSize())
        self.ui.boldCheckBox.setChecked(self.table.fontInfo().bold())

        self.ui.setButton.clicked.connect(self.save)
        self.ui.cancelButton.clicked.connect(self.close)

    def save(self):
        font = QFont()
        font.setFamily(self.ui.fontComboBox.currentText())
        font.setPointSize(self.ui.fontSizeSpinBox.value())
        font.setBold(self.ui.boldCheckBox.isChecked())
        self.table.setFont(font)
        self.close()

    def cancel(self):
        self.close()
