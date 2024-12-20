import dataclasses
from dataclasses import dataclass
from datetime import date

from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex


@dataclass
class Subscriber:
    _id: int
    name: str
    count: int
    flag: bool


class SubscriberTable(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.subscribers: list[Subscriber] = []

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.subscribers)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(dataclasses.fields(Subscriber))

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        subscriber = self.subscribers[index.row()]
        column = index.column()

        if role == Qt.DisplayRole:
            if column == 0:
                return subscriber._id
            elif column == 1:
                return subscriber.name
            elif column == 2:
                return subscriber.count
            elif column == 3:
                return subscriber.flag
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if section == 0:
                    return "ID"
                elif section == 1:
                    return "Название"
                elif section == 2:
                    return "Количество"
                elif section == 3:
                    return "Посчитано"

        return None

    def addRow(self, subscriber: Subscriber):
        row = self.rowCount()
        self.beginInsertRows(QModelIndex(), row, row)
        self.subscribers.append(subscriber)
        self.endInsertRows()

    def updateRow(self, subscriber: Subscriber, row: int):
        self.beginInsertRows(QModelIndex(), row, row)
        self.subscribers[row] = subscriber
        self.endInsertRows()

    def removeRow(self, row: int, parent=QModelIndex()):
        if row < 0 or row >= len(self.subscribers):
            return False

        self.beginRemoveRows(parent, row, row)
        del self.subscribers[row]
        self.endRemoveRows()

        return True
