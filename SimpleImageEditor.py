import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui

import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("openfile.ui", self)

        self.openFileButton = self.findChild(QPushButton, 'openFileButton')
        self.saveFileButton = self.findChild(QPushButton, 'saveFileButton')
        self.label = self.findChild(QLabel, 'label')

        self.openFileButton.clicked.connect(self.openFileClick)
        self.saveFileButton.clicked.connect(self.saveFileClick)

        self.show()

    def openFileClick(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files(*);;PNG(*.png);;JPG(*.jpg)")
        if fname[0] != '':
            self.image = cv2.imread(fname[0])
            self.q_image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0],
                                        QtGui.QImage.Format_RGB888).rgbSwapped()
            self.pixmap = QPixmap(fname[0])
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.q_image))

    def saveFileClick(self):
        dir_name = QFileDialog.getSaveFileName(self, "Save File", "", "All Files(*);;PNG(*.png);;JPG(*.jpg)")
        if dir_name[0] != '':
            cv2.imwrite(dir_name[0], self.image)


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
