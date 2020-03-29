from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(400, 400, 500, 500)
        self.setWindowTitle("Wizualizacja wektrokardiogramu")

        self.b1 = QtWidgets.QPushButton(self)
        self.label = QtWidgets.QLabel(self)

        self.init_ui()

    def init_ui(self):
        self.label.setText("My text");
        self.label.move(100, 100)

        self.b1.setText("Dodaj pacjenta")
        self.b1.move(50, 50)
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you've pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())


window()