from PySide6.QtCore import QDateTime, QDate
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit
from ui.migration.edit import Ui_FormAdd
from models import subscriber_table
from models.table import Subscriber
from PySide6.QtCore import QRegularExpression


class EditWidget(QDialog):
    def __init__(self, sub: Subscriber, row: int, parent=None):
        super(EditWidget, self).__init__(parent)

        self.row = row

        self.ui = Ui_FormAdd()
        self.ui.setupUi(self)

        self.ui.pushButtonSave.clicked.connect(self.add_subscriber)
        self.ui.pushButtonCancel.clicked.connect(self.close)

        # init default val
        self.ui.lineEditID.setText(str(sub._id))
        self.ui.lineEditName.setText(sub.name)
        self.ui.lineEditNumber.setText(str(sub.count))
        self.ui.checkCount.setChecked(sub.flag)

        self.ui.lineEditID.setValidator(QIntValidator(0, 999999999, self))

    def add_subscriber(self):

        sub = Subscriber(
            _id=int(self.ui.lineEditID.text()),
            name=self.ui.lineEditName.text(),
            count=int(self.ui.lineEditNumber.text()),
            flag=self.ui.checkCount.isChecked(),
        )
        subscriber_table.updateRow(sub, self.row)
        self.close()

    def show_error(self, message):
        error_msg = QMessageBox(self)
        error_msg.setIcon(QMessageBox.Critical)
        error_msg.setWindowTitle("Ошибка")
        error_msg.setText(message)
        error_msg.setStandardButtons(QMessageBox.Ok)
        error_msg.exec()

    def cancel(self):
        self.close()
