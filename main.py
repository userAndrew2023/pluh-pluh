import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        f = open("UI.ui")
        uic.loadUi(f, self)
        self.flag = False
        self.generate.clicked.connect(self.generateListener)

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.yellow, 10))
            rand = random.randint(50, 1000)
            painter.drawEllipse(100, 40, rand, rand)
            self.flag = False

    def generateListener(self):
        self.flag = True
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec_())
