import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPolygonF, QColor, QBrush
from PyQt5.QtCore import Qt, QPointF, QRectF
from PyQt5.QtWidgets import QApplication, QMainWindow
import random


class DrawCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.update)

    def paintEvent(self, event):
        rad = random.randint(20, 100)
        x, y = random.randint(50, 750), random.randint(50, 550)
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor(255, 255, 0)))
        painter.drawEllipse(QPointF(x, y), rad, rad)
        painter.save()


def exept(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    sys.excepthook = exept
    app = QApplication(sys.argv)
    ex = DrawCircle()
    ex.show()
    sys.exit(app.exec_())