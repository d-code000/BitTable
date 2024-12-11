from PySide6.QtCore import QDateTime
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit
from ui.migration.add import Ui_FormAdd
from models import subscriber_table
from models.table import Subscriber
from PySide6.QtCore import QRegularExpression


class AddWidget(QDialog):
    def __init__(self, parent=None):
        super(AddWidget, self).__init__(parent)

        self.ui = Ui_FormAdd()
        self.ui.setupUi(self)

        self.ui.pushButtonSave.clicked.connect(self.add_subscriber)
        self.ui.pushButtonCancel.clicked.connect(self.close)

        # init default val
        self.ui.lineEditID.setText('0')
        self.ui.lineEditName.setText('None')
        self.ui.lineEditNumber.setText('+71112223344')
        self.ui.dateEdit.setDate(QDateTime.currentDateTime().date())

        self.ui.lineEditID.setValidator(QIntValidator(0, 999999999, self))

        phone_regex = QRegularExpression(r'^\+7\d{10}$')
        phone_validator = QRegularExpressionValidator(phone_regex, self)
        self.ui.lineEditNumber.setValidator(phone_validator)

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
        if not self.validate_inputs():
            return

        sub = Subscriber(
            user_id=int(self.ui.lineEditID.text()),
            name=self.ui.lineEditName.text(),
            phone_number=self.ui.lineEditNumber.text(),
            user_type=self.ui.comboBoxType.currentText(),
            date=self.ui.dateEdit.text(),
        )
        subscriber_table.addRow(sub)
        self.close()

    def validate_inputs(self):
        """Проверка всех введённых данных."""
        try:
            int(self.ui.lineEditID.text())
        except ValueError:
            self.show_error("ID должен быть числом.")
            return False

        if not self.ui.lineEditName.text():
            self.show_error("Имя не может быть пустым.")
            return False

        phone = self.ui.lineEditNumber.text()
        if not QRegularExpression(r'^\+7\d{10}$').match(phone).hasMatch():
            self.show_error("Неверный формат номера телефона. Пример: +7XXXXXXXXXX")
            return False
        return True

    def show_error(self, message):
        error_msg = QMessageBox(self)
        error_msg.setIcon(QMessageBox.Critical)
        error_msg.setWindowTitle("Ошибка")
        error_msg.setText(message)
        error_msg.setStandardButtons(QMessageBox.Ok)
        error_msg.exec()

    def cancel(self):
        self.close()
