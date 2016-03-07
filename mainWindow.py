import sys
from PySide import QtGui, QtCore
import superFormulaWindow


class Communicate(QtCore.QObject):
    closeApp = QtCore.Signal()


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.c = Communicate()
        self.grid = None
        self.init_ui()

    def init_ui(self):
        self.c.closeApp.connect(self.close)
        # status bat
        self.statusBar()
        # grid
        self.grid = QtGui.QGridLayout()
        self.grid.setAlignment(QtCore.Qt.AlignTop)
        lbl = QtGui.QLabel("00000000000000000")
        self.grid.addWidget(lbl, 0, 0)
        lbl = QtGui.QLabel("11111111111111111")
        self.grid.addWidget(lbl, 0, 1)
        # button
        okbutton = QtGui.QPushButton("OK")
        cancelbutton = QtGui.QPushButton("Cancel")
        cancelbutton.clicked.connect(self.cancel_clicked)
        # Layouts
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okbutton)
        hbox.addWidget(cancelbutton)
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(self.grid, QtCore.Qt.AlignTop)
        vbox.addLayout(hbox)
        # main widget
        window = QtGui.QWidget()
        window.setLayout(vbox)
        self.setCentralWidget(window)

        self.setGeometry(500, 500, 590, 550)
        self.setWindowTitle('Main window')
        self.show()

    def cancel_clicked(self):
        self.c.closeApp.emit()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
