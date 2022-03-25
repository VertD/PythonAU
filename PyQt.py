from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

import webbrowser

def add_label():
    webbrowser.open('https://time100.ru/Saint-Petersburg')

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Текущее время")
    window.setGeometry(300, 250, 800, 700)


    btn = QtWidgets.QPushButton(window)
    btn.move(150,200)
    btn.setText("Нажми, чтобы узнать время в спб")
    btn.clicked.connect(add_label)
    btn.setFixedWidth(200)

    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    application()