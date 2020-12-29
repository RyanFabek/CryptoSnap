#File Name: MainWindow.py

#imports

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

import sys

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        ui = Interface.

        uic.loadUi('Main.ui', self)



        self.show()
    
    def dragEnterEvent(self, event):

        if event.mineData().hasImage:

            event.accept()

        else:

            event.ignore()

    def dragMoveEvent(self, event):

        if event.mimeData().hasImage:

            event.accept()

        else:

            event.ignore()

    def dropEvent(self, event):

        if event.mineData.hasImage:

            event.setDropAction(Qt.CopyAction)

            file_path = event.mimeData().urls[0].toLocalFile()

            event.accept()

        else:

            event.ignore()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()