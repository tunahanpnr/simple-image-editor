import random

import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageEnhance
from PyQt5.QtWidgets import QFileDialog, QMainWindow


class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):
        self.toolType = ''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 703)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.original_image_label = QtWidgets.QLabel(self.centralwidget)
        self.original_image_label.setGeometry(QtCore.QRect(0, 340, 530, 340))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHeightForWidth(self.original_image_label.sizePolicy().hasHeightForWidth())
        self.original_image_label.setSizePolicy(sizePolicy)
        self.original_image_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.original_image_label.setObjectName("original_image_label")
        self.original_image_label.setScaledContents(True)

        self.edited_image_label = QtWidgets.QLabel(self.centralwidget)
        self.edited_image_label.setGeometry(QtCore.QRect(530, 340, 480, 340))
        sizePolicy.setHeightForWidth(self.edited_image_label.sizePolicy().hasHeightForWidth())
        self.edited_image_label.setSizePolicy(sizePolicy)
        self.edited_image_label.setObjectName("edited_image_label")
        self.edited_image_label.setScaledContents(True)

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.hide()
        self.horizontalSlider.setGeometry(QtCore.QRect(370, 210, 261, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalSlider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSlider.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.horizontalSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setMinimum(-99)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setObjectName("horizontalSlider")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1015, 22))
        self.menuBar.setObjectName("menuBar")

        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")

        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")

        MainWindow.setMenuBar(self.menuBar)

        self.actionOpen_Image = QtWidgets.QAction(MainWindow)
        self.actionOpen_Image.setObjectName("actionOpen_Image")
        self.actionOpen_Image.triggered.connect(self.openImgClick)

        self.actionSave_Image = QtWidgets.QAction(MainWindow)
        self.actionSave_Image.setObjectName("actionSave_Image")
        self.actionSave_Image.triggered.connect(self.saveImgClick)

        self.actionBlur = QtWidgets.QAction(MainWindow)
        self.actionBlur.setObjectName("actionBlur")
        self.actionBlur.triggered.connect(self.blurImgClick)

        self.actionDeblur = QtWidgets.QAction(MainWindow)
        self.actionDeblur.setObjectName("actionDeblur")
        self.actionDeblur.triggered.connect(self.deblurImgClick)

        self.actionGrayscale = QtWidgets.QAction(MainWindow)
        self.actionGrayscale.setObjectName("actionGrayscale")
        self.actionGrayscale.triggered.connect(self.grayscaleImgClick)

        self.actionCrop = QtWidgets.QAction(MainWindow)
        self.actionCrop.setObjectName("actionCrop")
        self.actionCrop.triggered.connect(self.cropImgClick)

        self.actionFlip = QtWidgets.QAction(MainWindow)
        self.actionFlip.setObjectName("actionFlip")
        self.actionFlip.triggered.connect(self.flipImgClick)

        self.actionMirror = QtWidgets.QAction(MainWindow)
        self.actionMirror.setObjectName("actionMirror")
        self.actionMirror.triggered.connect(self.mirrorImgClick)

        self.actionRotate = QtWidgets.QAction(MainWindow)
        self.actionRotate.setObjectName("actionRotate")
        self.actionRotate.triggered.connect(self.rotateImgClick)

        self.actionReverse_Color = QtWidgets.QAction(MainWindow)
        self.actionReverse_Color.setObjectName("actionReverse_Color")
        self.actionReverse_Color.triggered.connect(self.reversecolorImgClick)

        self.actionColor_Balance = QtWidgets.QAction(MainWindow)
        self.actionColor_Balance.setObjectName("actionColor_Balance")
        self.actionColor_Balance.triggered.connect(self.colorBalanceImgClick)

        self.actionBrightness = QtWidgets.QAction(MainWindow)
        self.actionBrightness.setObjectName("actionBrightness")
        self.actionBrightness.triggered.connect(self.brightnessImgClick)

        self.actionContrast = QtWidgets.QAction(MainWindow)
        self.actionContrast.setObjectName("actionContrast")
        self.actionContrast.triggered.connect(self.contrastImgClick)

        self.actionSaturation = QtWidgets.QAction(MainWindow)
        self.actionSaturation.setObjectName("actionSaturation")
        self.actionSaturation.triggered.connect(self.saturationImgClick)

        self.actionNoise = QtWidgets.QAction(MainWindow)
        self.actionNoise.setObjectName("actionNoise")
        self.actionNoise.triggered.connect(self.noiseImgClick)

        self.actionDetect_Edges = QtWidgets.QAction(MainWindow)
        self.actionDetect_Edges.setObjectName("actionDetect_Edges")
        self.actionDetect_Edges.triggered.connect(self.detectEdgeImgClick)

        self.horizontalSlider.valueChanged.connect(lambda: self.sliderHandler(self.toolType))

        self.menuFile.addAction(self.actionOpen_Image)
        self.menuFile.addAction(self.actionSave_Image)
        self.menuTools.addAction(self.actionBlur)
        self.menuTools.addAction(self.actionDeblur)
        self.menuTools.addAction(self.actionGrayscale)
        self.menuTools.addAction(self.actionCrop)
        self.menuTools.addAction(self.actionFlip)
        self.menuTools.addAction(self.actionMirror)
        self.menuTools.addAction(self.actionRotate)
        self.menuTools.addAction(self.actionReverse_Color)
        self.menuTools.addAction(self.actionColor_Balance)
        self.menuTools.addAction(self.actionBrightness)
        self.menuTools.addAction(self.actionContrast)
        self.menuTools.addAction(self.actionSaturation)
        self.menuTools.addAction(self.actionNoise)
        self.menuTools.addAction(self.actionDetect_Edges)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.original_image_label.setText(_translate("MainWindow", "TextLabel"))
        self.edited_image_label.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionOpen_Image.setText(_translate("MainWindow", "Open Image"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image"))
        self.actionBlur.setText(_translate("MainWindow", "Blur"))
        self.actionDeblur.setText(_translate("MainWindow", "Deblur"))
        self.actionGrayscale.setText(_translate("MainWindow", "Grayscale"))
        self.actionCrop.setText(_translate("MainWindow", "Crop"))
        self.actionFlip.setText(_translate("MainWindow", "Flip"))
        self.actionMirror.setText(_translate("MainWindow", "Mirror"))
        self.actionRotate.setText(_translate("MainWindow", "Rotate"))
        self.actionReverse_Color.setText(_translate("MainWindow", "Reverse Color"))
        self.actionColor_Balance.setText(_translate("MainWindow", "Color Balance"))
        self.actionBrightness.setText(_translate("MainWindow", "Brightness"))
        self.actionContrast.setText(_translate("MainWindow", "Contrast"))
        self.actionSaturation.setText(_translate("MainWindow", "Saturation"))
        self.actionNoise.setText(_translate("MainWindow", "Noise"))
        self.actionDetect_Edges.setText(_translate("MainWindow", "Detect Edges"))

    def openImgClick(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files(*);;PNG(*.png);;JPG(*.jpg)")
        if fname[0] != '':
            self.original_image_cv2 = cv2.imread(fname[0])
            self.edited_image_cv2 = cv2.imread(fname[0])
            self.edited_image_copy_cv2 = cv2.imread(fname[0])
            self.showImage(self.original_image_cv2, self.original_image_label)

    def saveImgClick(self):
        dir_name = QFileDialog.getSaveFileName(self, "Save File", "", "All Files(*);;PNG(*.png);;JPG(*.jpg)")
        if dir_name[0] != '':
            cv2.imwrite(dir_name[0], self.edited_image_cv2)

    def blurImgClick(self):
        self.toolType = 'blur'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.show()

    def blurImg(self, val):
        self.edited_image_cv2 = cv2.blur(self.edited_image_copy_cv2, (val, val))
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def deblurImgClick(self):
        self.toolType = 'deblur'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.show()

    def deblurImg(self, val):
        pil_img = self.cv2_to_pil(self.edited_image_copy_cv2)
        enhancer = ImageEnhance.Sharpness(pil_img)
        factor = 1 + val  
        im_output = enhancer.enhance(factor)
        self.edited_image_cv2 = self.pil_to_cv2(im_output)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def grayscaleImgClick(self):
        self.isGrayScaled = True
        self.edited_image_cv2 = cv2.cvtColor(self.edited_image_cv2, cv2.cv2.COLOR_BGR2GRAY)
        self.edited_image_cv2 = cv2.cvtColor(self.edited_image_cv2, cv2.cv2.COLOR_RGB2BGR)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def flipImgClick(self):
        self.edited_image_cv2 = cv2.flip(self.edited_image_cv2, 0)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def mirrorImgClick(self):
        self.edited_image_cv2 = cv2.flip(self.edited_image_cv2, 1)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def rotateImgClick(self):
        self.edited_image_cv2 = cv2.rotate(self.edited_image_cv2, cv2.ROTATE_90_CLOCKWISE)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def reversecolorImgClick(self):
        self.edited_image_cv2 = cv2.bitwise_not(self.edited_image_cv2)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def cropImgClick(self):
        r = cv2.selectROI(self.edited_image_cv2)
        cv2.destroyAllWindows()
        self.edited_image_cv2 = self.edited_image_cv2[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])].copy()
        self.showImage(self.edited_image_cv2, self.edited_image_label)
        # editted_image = QtGui.QImage(self.edited_image_cv2.data, self.edited_image_cv2.shape[1],
        #                              self.edited_image_cv2.shape[0],
        #                              QtGui.QImage.Format_RGB888).rgbSwapped()
        #
        # editted_image = QtGui.QPixmap.fromImage(editted_image)
        # crop_tool = QCrop(editted_image)
        # status = crop_tool.exec()
        #
        # if status == 1:
        #     cropped_image = crop_tool.image
        #     self.edited_image_cv2 = self.qimg2cv(cropped_image)
        #     self.showImage(self.edited_image_cv2, self.edited_image_label)

        # else crop_tool.image == original_image

    def reset(self):
        edited_image = QtGui.QImage(self.original_image_cv2.data, self.original_image_cv2.shape[1],
                                    self.original_image_cv2.shape[0],
                                    QtGui.QImage.Format_RGB888).rgbSwapped()
        self.edited_image_label.setPixmap(QtGui.QPixmap.fromImage(edited_image))

    def detectEdgeImgClick(self):
        grayscale = cv2.cvtColor(self.edited_image_cv2, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(grayscale, (5, 5), 1)
        self.edited_image_cv2 = cv2.Canny(blurred_image, threshold1=100, threshold2=100)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def saturationImgClick(self):
        self.toolType = 'saturation'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSlider.setMinimum(-99)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.show()

    def saturationImg(self, val):
        pil_img = self.cv2_to_pil(self.edited_image_copy_cv2)
        enhancer = ImageEnhance.Color(pil_img)
        factor = 1 + val
        im_output = enhancer.enhance(factor)
        self.edited_image_cv2 = self.pil_to_cv2(im_output)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def showImage(self, img, label):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        edited_image = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], QtGui.QImage.Format_RGB888)
        label.setPixmap(QtGui.QPixmap.fromImage(edited_image))

    def colorBalanceImgClick(self):
        value = 20
        B, G, R = self.edited_image_cv2[:, :, 0], self.edited_image_cv2[:, :, 1], self.edited_image_cv2[:, :, 2]
        R += value
        G += value
        B += value
        self.edited_image_cv2 = cv2.merge((B, G, R))
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def noiseImgClick(self):
        self.toolType = 'noise'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.show()

    def noiseImg(self, prob):
        output = np.zeros(self.edited_image_copy_cv2.shape, np.uint8)
        thres = 1 - prob
        for i in range(self.edited_image_copy_cv2.shape[0]):
            for j in range(self.edited_image_copy_cv2.shape[1]):
                rdn = random.random()
                if rdn < prob:
                    output[i][j] = 0
                elif rdn > thres:
                    output[i][j] = 255
                else:
                    output[i][j] = self.edited_image_copy_cv2[i][j]
        self.edited_image_cv2 = output
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def noisy(self, noise_typ):
        if noise_typ == "gauss":
            row, col, ch = self.edited_image_cv2.shape
            mean = 0
            var = 0.1
            sigma = var ** 0.5
            gauss = np.random.normal(mean, sigma, (row, col, ch))
            gauss = gauss.reshape(row, col, ch)
            noisy = self.edited_image_cv2 + gauss
            return noisy
        elif noise_typ == "s&p":
            row, col, ch = self.edited_image_cv2.shape
            s_vs_p = 0.5
            amount = 0.004
            out = np.copy(self.edited_image_cv2)
            # Salt mode
            num_salt = np.ceil(amount * self.edited_image_cv2.size * s_vs_p)
            coords = [np.random.randint(0, i - 1, int(num_salt))
                      for i in self.edited_image_cv2.shape]
            out[coords] = 1

            # Pepper mode
            num_pepper = np.ceil(amount * self.edited_image_cv2.size * (1. - s_vs_p))
            coords = [np.random.randint(0, i - 1, int(num_pepper))
                      for i in self.edited_image_cv2.shape]
            out[coords] = 0
            return out

        elif noise_typ == "poisson":
            vals = len(np.unique(self.edited_image_cv2))
            vals = 2 ** np.ceil(np.log2(vals))
            noisy = np.random.poisson(self.edited_image_cv2 * vals) / float(vals)
            return noisy

        elif noise_typ == "speckle":
            row, col, ch = self.edited_image_cv2.shape
            gauss = np.random.randn(row, col, ch)
            gauss = gauss.reshape(row, col, ch)
            noisy = self.edited_image_cv2 + self.edited_image_cv2 * gauss
            return noisy

    def brightnessImgClick(self):
        self.toolType = 'brightness'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSlider.setMinimum(-99)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.show()

    def brightnessImg(self, sliderVal):
        pil_img = self.cv2_to_pil(self.edited_image_copy_cv2)
        enhancer = ImageEnhance.Brightness(pil_img)
        factor = 1 + sliderVal  
        im_output = enhancer.enhance(factor)
        self.edited_image_cv2 = self.pil_to_cv2(im_output)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

        # hls_image = cv2.cvtColor(self.edited_image_cv2, cv2.COLOR_BGR2HLS)
        # increase_value = 20
        # hls_image[:, :, 1] += increase_value
        # normal_image = cv2.cvtColor(hls_image, cv2.COLOR_HLS2BGR)
        # self.edited_image_cv2 = normal_image
        # self.showImage(self.edited_image_cv2, self.edited_image_label)

    def contrastImgClick(self):
        self.toolType = 'contrast'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSlider.setMinimum(-99)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.show()

    def contrastImg(self, val):
        pil_img = self.cv2_to_pil(self.edited_image_copy_cv2)
        enhancer = ImageEnhance.Contrast(pil_img)
        factor = 1 + val
        im_output = enhancer.enhance(factor)
        self.edited_image_cv2 = self.pil_to_cv2(im_output)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

        # lab_image = cv2.cvtColor(self.edited_image_cv2, cv2.COLOR_BGR2LAB)
        # l, a, b = cv2.split(lab_image)
        # clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        # cl = clahe.apply(l)
        # merged = cv2.merge((cl, a, b))
        # self.edited_image_cv2 = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)
        # self.showImage(self.edited_image_cv2, self.edited_image_label)

    def cv2_to_pil(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(img)
        return im_pil

    def pil_to_cv2(self, img):
        cv2_img = np.asarray(img)
        return cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)

    def sliderHandler(self, toolType):
        val = self.horizontalSlider.value()
        if toolType == 'blur':
            val = (val - (val % 10)) // 10
            if val != 0:
                val = val + 1 if (val > 3) else 3
                print(val)
                self.blurImg(val)

        elif toolType == 'deblur':
            val /= 5
            self.deblurImg(val)

        elif toolType == 'saturation':
            val /= 50
            self.saturationImg(val)

        elif toolType == 'noise':
            val /= 1000
            self.noiseImg(val)

        elif toolType == 'contrast':
            val /= 50
            self.contrastImg(val)

        elif toolType == 'brightness':
            val /= 100
            self.brightnessImg(val)

        return val


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
