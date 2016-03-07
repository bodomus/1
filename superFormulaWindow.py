import sys
from PySide.QtCore import *
from PySide.QtGui import *


class SliderPreferences(QWidget):
    """ represents gui interface for superformula """

    sliderChanged = Signal()

    def __init__(self, parent=None):
        super(SliderPreferences, self).__init__(parent)

        # (name, slider_name, text_box name)
        self.gui_objects = []
        self.status_bar = QStatusBar()

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
            self.textbox = QTextEdit()
            self.textbox.setMaximumHeight(24)
            self.textbox.setObjectName("textbox" + names[x])
            self.lbl = QLabel(names[x])
            self.slider = QSlider(Qt.Horizontal)
            self.slider.setObjectName("slider" + names[x])
            self.slider.valueChanged.connect(self.slider_changed)
            self.gui_objects.append((names[x], self.slider, self.textbox))
            self.grid.addWidget(self.lbl, x, y)
            self.grid.addWidget(self.slider, x, y + 1)
            self.grid.addWidget(self.textbox, x, y + 2)

        for i in xrange(6, 8):
            lbl = QLabel("123")
            self.grid.addWidget(lbl, i, 0)

        self.setLayout(self.grid)
        self.setWindowTitle("SpinBox demo")

    def slider_changed(self, arg):
        sender = self.sender()
        value = sender.value()
        for name, slider, textbox in self.gui_objects:
            if self.__eq__(sender, slider):
                textbox.setText(str(value))

    def __eq__(self, other1, other2):
        if type(other1) is type(other2):
            return other2.__dict__ == other1.__dict__
        return False


def main():
    app = QApplication(sys.argv)
    ex = SliderPreferences()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
