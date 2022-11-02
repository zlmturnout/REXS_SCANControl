from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QColor

"""
This is the class for displaying pandas DataFrame data in QTable View
"""


class PandasInQTable(QAbstractTableModel):
    def __init__(self, pd_data):
        super(PandasInQTable, self).__init__()
        self._data = pd_data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role:int=Qt.DisplayRole):
        if index.isValid():
            value = self._data.iloc[index.row(), index.column()]
            if role == Qt.DisplayRole:
                if isinstance(value,int) or isinstance(value,str):
                    return "%s" % value
                if isinstance(value,float):
                    return "%.4f" % value
                else:
                    return str(value)
            # set alignment
            if role==Qt.TextAlignmentRole:
                return Qt.AlignVCenter + Qt.AlignCenter
            # set color
            if role==Qt.ForegroundRole:
                if isinstance(value,float) or isinstance(value,int):
                    return QColor(33, 190, 193)
                if isinstance(value,str):
                    return QColor(255, 95, 21)
                else:
                    return QColor(255,85,127)

    def headerData(self, section: int, orientation: Qt.Orientation, role:int=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[section]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.axes[0][section]
        return None
