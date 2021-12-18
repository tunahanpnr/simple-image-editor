import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5 import QtGui

import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        self.isBlurred = False

        uic.loadUi("openfile.ui", self)

        self.openImgButton = self.findChild(QPushButton, 'openImgButton')
        self.saveImgButton = self.findChild(QPushButton, 'saveImgButton')
        self.blurImgButton = self.findChild(QPushButton, 'blurImgButton')

        self.openImgButton.clicked.connect(self.openImgClick)
        self.saveImgButton.clicked.connect(self.saveImgClick)
        self.blurImgButton.clicked.connect(self.blurImgClick)

        self.label = self.findChild(QLabel, 'label')

        self.show()

    def openImgClick(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files(*);;PNG(*.png);;JPG(*.jpg)")
        if fname[0] != '':
            self.image = cv2.imread(fname[0])
            self.q_image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0],
                                        QtGui.QImage.Format_RGB888).rgbSwapped()
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.q_image))

    def saveImgClick(self):
        dir_name = QFileDialog.getSaveFileName(self, "Save File", "", "All Files(*);;PNG(*.png);;JPG(*.jpg)")
        if dir_name[0] != '':
            cv2.imwrite(dir_name[0], self.image)

    def blurImgClick(self):
        self.image = cv2.blur(self.image, (10, 10))
        self.q_image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0],
                                    QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.q_image))





app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
