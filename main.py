import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QApplication, QMainWindow
import random

from PyQt5 import QtCore, QtGui, QtWidgets


class DrawCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.update)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(300, 240, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git и случайные окружности"))
        self.btn.setText(_translate("MainWindow", "Создать окружность"))

    def paintEvent(self, event):
        rad = random.randint(20, 100)
        x, y = random.randint(50, 750), random.randint(50, 550)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor(r, g, b)))
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