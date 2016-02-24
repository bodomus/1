import sys
from PySide.QtCore import *
from PySide.QtGui import *


class sliderdemo(QWidget):
    valueChanged = Signal(int)

    def __init__(self, parent=None):
        super(sliderdemo, self).__init__(parent)

        self.grid = QGridLayout()
        names = ['A', 'B', 'M', 'N1', 'N2', 'N3']
        # (x, y, ) position in grid
        pos = [(0, 0), (0, 1), (0, 2),
               (1, 0), (1, 1), (1, 2),
               (2, 0), (2, 1), (2, 2),
               (3, 0), (3, 1), (3, 2),
               (4, 0), (4, 1), (4, 2),
               (5, 0), (5, 1), (5, 2),
               ]
        for x, y in [item for item in pos if item[1] == 0]:
            self.lbl = QLabel(names[x])
            self.slider = QSlider(Qt.Horizontal)
            self.slider.setObjectName("slider" + names[x])
            # self.slider.valueChanged.
            self.textbox = QTextEdit()
            self.textbox.setMaximumHeight(24)
            self.textbox.setObjectName("textbox" + names[x])
            self.grid.addWidget(self.lbl, x, y)
            self.grid.addWidget(self.slider, x, y + 1)
            self.grid.addWidget(self.textbox, x, y + 2)

        for i in xrange(6, 8):
            lbl = QLabel("123")
            self.grid.addWidget(lbl, i, 0)

        self.setLayout(self.grid)
        self.setWindowTitle("SpinBox demo")

    def valuechange(self):
        size = self.sl.value()
        self.l1.setFont(QFont("Arial", size))


def main():
    app = QApplication(sys.argv)
    ex = sliderdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
