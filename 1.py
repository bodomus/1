# -*- coding: utf-8 -*-
"""
"""
import sys
import superformula

from PySide.QtCore import *
from PySide.QtGui import *


class SignalEscape(QObject):
    closeApp = Signal()


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.scale = 1
        self.c = SignalEscape()
        self.c.closeApp.connect(self.close)
        self.ss = superformula.SuperFormula(3, 1, 1, 5, 18, 18)  # initialize SuperFormula instance
        self.ss.get_radius()  #
        self.points = self.ss.calc_points()
        self.lblA = QLabel("Var a")
        self.lblB = QLabel("Var b")
        self.lblM = QLabel("Var M")
        self.lblN1 = QLabel("Var N1")
        self.lblN2 = QLabel("Var N2")
        self.lblN3 = QLabel("Var N3")
        self.add_buitton_layout()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Superformula')
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.c.closeApp.emit()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_axis(qp)
        self.draw_points(qp)
        qp.end()

    def draw_axis(self, qp):
        qp.setPen(Qt.red)
        size = self.size()
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        # Аргументы: цвет, ширинац линии, тип линии (здесь -- сплошная линия).
        y2 = size.height() / 2
        x1 = 0
        y1 = y2
        x2 = size.width()
        qp.setPen(pen)  # Будем рисовать на qp с помощью объекта pen.
        qp.drawLine(x1, y1, x2, y2)  # проведём линию от точки (20, 40) до точки (250, 40).
        # Координаты относительно левого верхнего угла, ось y
        # направлена вниз.
        x1 = size.width() / 2
        y1 = 0
        x2 = x1
        y2 = size.height()
        qp.drawLine(x1, y1, x2, y2)
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawText(size.width() / 2 + 2, 10, 'Y')
        qp.drawText(size.width() - 10, size.height() / 2, 'X')

    def draw_points(self, qp):
        size = self.size()
        zero_x = size.width() / 2
        zero_y = size.height() / 2
        qp.setPen(Qt.blue)
        cpx = 0
        cpy = 0
        for item in self.points:
            qp.drawPoint((item[0] + zero_x) * self.scale, (item[1] + zero_y) * self.scale)
            if cpx != 0 and cpy != 0:
                qp.drawLine(cpx, cpy, (item[0] + zero_x) * self.scale, (item[1] + zero_y) * self.scale)
            cpx = (item[0] + zero_x) * self.scale
            cpy = (item[1] + zero_y) * self.scale

    def add_buitton_layout(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.lblA.setAlignment(Qt.AlignRight)
        # vbox.addWidget(self.lblA)
        self.setLayout(vbox)

        # def add_sliders_ui(self):


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
