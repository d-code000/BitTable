import random
import time
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QDialog, QTableView
from ui.migration.setting import Ui_SettingForm


class ProgressBarThread(QThread):
    update_progress = Signal(int)

    def run(self):
        for i in range(1, 101):
            self.update_progress.emit(i)
            time.sleep(random.uniform(0.1, 1))  # Более плавная задержка


class SettingWidget(QDialog):
    def __init__(self, table: QTableView, parent=None):
        super(SettingWidget, self).__init__(parent)

        self.ui = Ui_SettingForm()
        self.ui.setupUi(self)
        self.table = table
        self.ui.progressBar.setValue(0)

        self.progress_thread = ProgressBarThread()
        self.progress_thread.update_progress.connect(self.update_progress_bar)
        self.progress_thread.start()

    def update_progress_bar(self, value):
        self.ui.progressBar.setValue(value)
