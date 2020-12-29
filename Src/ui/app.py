#File Name: app.py

#imports

import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QLabel, QWidget, QApplication, QMainWindow, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

sys.path.insert(1, "../functions/")
from Steganography import *

import sys

class Drop_Image(QWidget):

    def __init__(self):

        super().__init__()

        self.setAcceptDrops(True)

        self.Image_Label = QtWidgets.QLabel()
        self.Image_Label.setGeometry(QtCore.QRect(150, 80, 311, 231))
        self.Image_Label.setStyleSheet("border: 2px dashed grey")
        self.Image_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Image_Label.setObjectName("Image_Drop")
        self.Image_Label.setText("Drop Image Here")

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(self.Image_Label)

        self.text = QText

        self.setLayout(self.layout)




    def dragEnterEvent(self, event):

        if event.mimeData().hasUrls():
            event.acceptProposedAction()

        else:

            event.ignore()

    def dragMoveEvent(self, event):

        if event.mimeData().hasUrls():

            event.acceptProposedAction()

        else:

            event.ignore()

    def dropEvent(self, event):

        if event.mimeData().hasUrls():

            event.setDropAction(Qt.CopyAction)
            filepath = event.mimeData().urls()[0].toLocalFile()
            

            hideMessage(filepath, "Test")
 
            event.acceptProposedAction()
        else:
            event.ignore()


class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.setFixedSize(640,480)
        self.setWindowTitle("Crypto")


        self.Image_Widget = Drop_Image()
        self.setCentralWidget(self.Image_Widget)

        

if __name__ == "__main__":

    app = QApplication([])

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())