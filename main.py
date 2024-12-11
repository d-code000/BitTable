import sys
from models.table_widget import TableWidget

from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = TableWidget()
    window.show()

    sys.exit(app.exec())