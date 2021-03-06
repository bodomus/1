# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

In this example, we connect a signal
of a QtGui.QSlider to a slot
of a QtGui.QLCDNumber.

author: Jan Bodnar
website: zetcode.com
last edited: August 2011
"""

import sys
from PySide import QtGui, QtCore
class Communicate(QtCore.QObject):

    closeApp = QtCore.Signal()

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def mousePressEvent(self, event):

        self.c.closeApp.emit()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
