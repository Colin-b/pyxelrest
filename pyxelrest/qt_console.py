import re
import sys
import operator
import time

import logging
import threading
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

"""
Log Handler that pops up a QT table with filter:
    h = QtHandler()
    h.start()
    logging.getLogger().addHandler(h)
PyQt5 is not a mandatory package for pyxelrest
"""


class MyWidget(QtWidgets.QWidget):
    def __init__(self, header):
        super().__init__()
        self.table_model = MyTableModel(self, header)
        self.table_view = QtWidgets.QTableView(self)
        self.table_view.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.table_view.setModel(self.table_model)
        textEdit = QtWidgets.QLineEdit(self)
        textEdit.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        textEdit.returnPressed.connect(lambda: self.table_model.filter(textEdit.text()))
        textEdit.setPlaceholderText("Filter")
        resetButton = QtWidgets.QPushButton(self)
        resetButton.setText("Reset")
        resetButton.pressed.connect(lambda: self.table_model.clear())
#        font = QtGui.QFont("Courier New", 10)
#        table_view.setFont(font)
        self.table_view.resizeColumnsToContents()
        self.table_view.setSortingEnabled(True)
        layout = QtWidgets.QVBoxLayout(self)
        layout2 = QtWidgets.QHBoxLayout(self)
        layout.addLayout(layout2)
        layout2.addWidget(textEdit, 0)
        layout2.addWidget(resetButton, 0)
        layout.addWidget(self.table_view)
        self.setLayout(layout)


class MyWindow(QtWidgets.QMainWindow):
    signal_append = QtCore.pyqtSignal(list)

    def __init__(self, title, header, *args):
        super().__init__(*args)
        self.setGeometry(300, 200, 570, 450)
        self.setWindowTitle(title)
        self.wdg = MyWidget(header)
        self.setCentralWidget(self.wdg)
        self.signal_append.connect(self.append)

    def append(self, data):
        self.wdg.table_model.append(data)
        self.wdg.table_model.recompute()
        self.wdg.table_view.resizeColumnsToContents()
        self.show()


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, header, max_nb=1000, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.olist = []
        self.dlist = []
        self.sortCol = None
        self.reverseOrder = None
        self.expr = None
        self.header = header
        self.max = max_nb
        self.color_red = QtCore.QVariant(QtGui.QBrush(QtGui.QColor(QtCore.Qt.red)))
        self.color_yellow = QtCore.QVariant(QtGui.QBrush(QtGui.QColor(QtCore.Qt.yellow)))
        self.align_center = QtCore.QVariant(QtCore.Qt.AlignCenter)
        self.align_left = QtCore.QVariant(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

    def rowCount(self, parent):
        return len(self.dlist)

    def columnCount(self, parent):
        return len(self.header)

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role == QtCore.Qt.DisplayRole:
            return self.dlist[index.row()][index.column()]
        elif role == QtCore.Qt.BackgroundRole:
            level = self.dlist[index.row()][1]
            if level == 'ERROR':
                return self.color_red
            elif level == 'WARNING':
                return self.color_yellow
            return None
        elif role == QtCore.Qt.TextAlignmentRole:
            if index.column() < len(self.header) - 1:
                return self.align_center
            else:
                return self.align_left
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.sortCol = col
        self.reverseOrder = order == QtCore.Qt.DescendingOrder
        self.recompute()

    def filter(self, expr):
        """sort table by given column number col"""
        self.expr = None if expr == '' else expr.lower().split(' ')
        self.recompute()

    def recompute(self):
        def contains(x):
            def contains2(y):
                for e in x:
                    try:
                        if type(e) is str and e.lower().find(y) >= 0:
                            return True
                        elif type(e) is int and e == int(y):
                            return True
                        elif type(e) is float and abs(e - float(y)) < 1e-6:
                            return True
                    except:
                        pass
                return False

            for v in self.expr:
                if not contains2(v):
                    return False
            return True

        self.layoutAboutToBeChanged.emit()
        self.dlist = self.olist if self.expr is None \
            else filter(lambda x: contains(x), self.olist)
        if self.sortCol is not None:
            self.dlist = sorted(self.dlist, key=operator.itemgetter(self.sortCol), reverse=self.reverseOrder)
        self.layoutChanged.emit()

    def append(self, txt):
        if len(self.olist) > self.max:
            del self.olist[0]
        self.olist.append(txt)

    def get(self, pos):
        return self.olist[pos]

    def clear(self):
        self.olist = []
        self.recompute()


class QtHandler(logging.Handler):
    tags = re.compile(r'\[\w*=([^]]*)\]')

    def __init__(self):
        super().__init__()
        self.win = None

    def start(self):
        def ui():
            app = QtWidgets.QApplication(sys.argv)
            self.win = MyWindow("Log Viewer", ['Date', 'Level', 'Thread', 'Location', 'Message'])
            app.exec_()
            self.win = None
        if self.win is not None:
            threading.Thread(target=ui).start()

    def show(self):
        if self.win is not None:
            self.win.show()

    def emit(self, record):
        if self.win is not None:
            msg = self.tags.sub(r'\1', record.msg)
            data = [datetime.datetime.fromtimestamp(record.created).time().isoformat(), record.levelname, str(record.process) + ':' + str(record.thread),
                    record.filename + ':' + str(record.lineno), msg]
            self.win.signal_append.emit(data)


if __name__ == '__main__':
    l = logging.getLogger()
    h = QtHandler()
    h.start()
    l.addHandler(h)
    time.sleep(1)
    l.info('toto [a=2]')
    time.sleep(1000)
