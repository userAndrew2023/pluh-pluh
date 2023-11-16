import random
import sys

from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        f = open("UI.ui")
        self.generate = QPushButton(self)
        self.generate.setGeometry(400, 800, 100, 50)
        self.generate.setText("Generate")
        self.setGeometry(0, 0, 1900, 1000)
        self.flag = False
        self.generate.clicked.connect(self.generateListener)

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter(self)
            painter.setPen(QPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 10))
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
