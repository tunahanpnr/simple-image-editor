import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 615)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 190, 821, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.openImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.openImgButton.setGeometry(QtCore.QRect(0, 0, 91, 31))
        self.openImgButton.setObjectName("openImgButton")
        self.openImgButton.clicked.connect(self.openImgClick)

        self.saveImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveImgButton.setGeometry(QtCore.QRect(90, 0, 91, 31))
        self.saveImgButton.setObjectName("saveImgButton")
        self.saveImgButton.clicked.connect(self.saveImgClick)

        self.blurImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.blurImgButton.setGeometry(QtCore.QRect(180, 0, 101, 31))
        self.blurImgButton.setObjectName("blurImgButton")
        self.blurImgButton.clicked.connect(self.blurImgClick)

        self.deblurImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.deblurImgButton.setGeometry(QtCore.QRect(280, 0, 81, 31))
        self.deblurImgButton.setObjectName("deblurImgButton")
        self.deblurImgButton.clicked.connect(self.deblurImgClick)

        self.grayscaleImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.grayscaleImgButton.setGeometry(QtCore.QRect(360, 0, 91, 31))
        self.grayscaleImgButton.setObjectName("grayscaleImgButton")
        self.grayscaleImgButton.clicked.connect(self.grayscaleImgClick)

        self.cropImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.cropImgButton.setGeometry(QtCore.QRect(450, 0, 91, 31))
        self.cropImgButton.setObjectName("cropImgButton")

        self.flipImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.flipImgButton.setGeometry(QtCore.QRect(540, 0, 91, 31))
        self.flipImgButton.setObjectName("flipImgButton")
        self.flipImgButton.clicked.connect(self.flipImgClick)

        self.mirrorImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.mirrorImgButton.setGeometry(QtCore.QRect(630, 0, 81, 31))
        self.mirrorImgButton.setObjectName("mirrorImgButton")
        self.mirrorImgButton.clicked.connect(self.mirrorImgClick)

        self.rotateImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.rotateImgButton.setGeometry(QtCore.QRect(710, 0, 91, 31))
        self.rotateImgButton.setObjectName("rotateImgButton")
        self.rotateImgButton.clicked.connect(self.rotateImgClick)

        self.reversecolorImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.reversecolorImgButton.setGeometry(QtCore.QRect(0, 30, 111, 31))
        self.reversecolorImgButton.setObjectName("reversecolorImgButton")

        self.colorbalanceImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.colorbalanceImgButton.setGeometry(QtCore.QRect(110, 30, 171, 31))
        self.colorbalanceImgButton.setObjectName("colorbalanceImgButton")

        self.brightnessImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.brightnessImgButton.setGeometry(QtCore.QRect(280, 30, 91, 31))
        self.brightnessImgButton.setObjectName("brightnessImgButton")

        self.contrastImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.contrastImgButton.setGeometry(QtCore.QRect(370, 30, 91, 31))
        self.contrastImgButton.setObjectName("contrastImgButton")

        self.saturationImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.saturationImgButton.setGeometry(QtCore.QRect(460, 30, 91, 31))
        self.saturationImgButton.setObjectName("saturationImgButton")

        self.noiseImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.noiseImgButton.setGeometry(QtCore.QRect(550, 30, 81, 31))
        self.noiseImgButton.setObjectName("noiseImgButton")

        self.detectedgeImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.detectedgeImgButton.setGeometry(QtCore.QRect(630, 30, 171, 31))
        self.detectedgeImgButton.setObjectName("detectedgeImgButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openImgButton.setText(_translate("MainWindow", "Open File"))
        self.saveImgButton.setText(_translate("MainWindow", "Save File"))
        self.blurImgButton.setText(_translate("MainWindow", "Blur"))
        self.grayscaleImgButton.setText(_translate("MainWindow", "Grayscale"))
        self.cropImgButton.setText(_translate("MainWindow", "Crop"))
        self.flipImgButton.setText(_translate("MainWindow", "Flip"))
        self.mirrorImgButton.setText(_translate("MainWindow", "Mirror"))
        self.rotateImgButton.setText(_translate("MainWindow", "Rotate"))
        self.reversecolorImgButton.setText(_translate("MainWindow", "Reverse Color"))
        self.colorbalanceImgButton.setText(_translate("MainWindow", "Color Balance"))
        self.brightnessImgButton.setText(_translate("MainWindow", " Brightness"))
        self.contrastImgButton.setText(_translate("MainWindow", "Contrast"))
        self.saturationImgButton.setText(_translate("MainWindow", "Saturation"))
        self.noiseImgButton.setText(_translate("MainWindow", "Noise"))
        self.detectedgeImgButton.setText(_translate("MainWindow", "Detect Edges"))
        self.deblurImgButton.setText(_translate("MainWindow", "Deblur"))

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
        self.image = cv2.blur(self.image, (3, 3))
        self.q_image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0],
                                    QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.q_image))

    def deblurImgClick(self):
        # Creating our sharpening filter
        filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        # Applying cv2.filter2D function on our Cybertruck image
        self.image = cv2.filter2D(self.image, -1, filter)
        self.q_image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0],
                                    QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.q_image))

    def grayscaleImgClick(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.q_image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0],
                                    QtGui.QImage.Format_Grayscale8).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.q_image))

    def flipImgClick(self):
        self.image = cv2.flip(self.image, 0)
        self.q_image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0],
                                    QtGui.QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.q_image))

    def mirrorImgClick(self):
            self.image = cv2.flip(self.image, 1)
            self.q_image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0],
                                        QtGui.QImage.Format_RGB888).rgbSwapped()
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.q_image))

    def rotateImgClick(self):
                self.image = cv2.rotate(self.image, cv2.cv2.ROTATE_90_CLOCKWISE)
                self.q_image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0],
                                            QtGui.QImage.Format_RGB888).rgbSwapped()
                self.label.setPixmap(QtGui.QPixmap.fromImage(self.q_image))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
