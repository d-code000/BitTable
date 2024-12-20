from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit

from models import subscriber_table
from models.table import Subscriber
from ui.migration.add import Ui_FormAdd


class AddWidget(QDialog):
    def __init__(self, parent=None):
        super(AddWidget, self).__init__(parent)

        self.ui = Ui_FormAdd()
        self.ui.setupUi(self)

        self.ui.pushButtonSave.clicked.connect(self.add_subscriber)
        self.ui.pushButtonCancel.clicked.connect(self.close)

        # init default val
        self.ui.lineEditID.setText('0')
        self.ui.lineEditName.setText('Название')
        self.ui.lineEditNumber.setText('0')

        self.ui.lineEditID.setValidator(QIntValidator(0, 999999999, self))

        self.ui.lineEditID.textChanged.connect(self.validate_not_empty)
        self.ui.lineEditName.textChanged.connect(self.validate_not_empty)
        self.ui.lineEditNumber.textChanged.connect(self.validate_not_empty)

    def validate_not_empty(self):
        """Проверка, чтобы имя не было пустым."""

        text: QLineEdit = self.sender().text()
        if not text:
            self.sender().setStyleSheet('border: 1px solid red;')
        else:
            self.sender().setStyleSheet('')

    def add_subscriber(self):
        """Добавление подписчика после валидации всех данных."""

        sub = Subscriber(
            _id=int(self.ui.lineEditID.text()),
            name=self.ui.lineEditName.text(),
            count=int(self.ui.lineEditNumber.text()),
            flag=self.ui.checkCount.isChecked(),
        )
        subscriber_table.addRow(sub)
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
