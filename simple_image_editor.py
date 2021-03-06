import random
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageEnhance
from PyQt5.QtWidgets import QFileDialog, QMainWindow


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.toolType = ''
        self.original_image_cv2 = None
        self.edited_image_cv2 = None
        self.edited_image_copy_cv2 = None

    def setupUi(self, MainWindow):
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

        self.horizontalSliderRValue = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderRValue.hide()
        self.horizontalSliderRValue.setGeometry(QtCore.QRect(350, 110, 261, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.horizontalSliderRValue.setFont(font)
        self.horizontalSliderRValue.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalSliderRValue.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSliderRValue.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.horizontalSliderRValue.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalSliderRValue.setAutoFillBackground(False)
        self.horizontalSliderRValue.setMinimum(-99)
        self.horizontalSliderRValue.setSliderPosition(0)
        self.horizontalSliderRValue.setTracking(True)
        self.horizontalSliderRValue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderRValue.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSliderRValue.setTickInterval(0)
        self.horizontalSliderRValue.setObjectName("horizontalSliderRValue")
        self.horizontalSliderGValue = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderGValue.hide()
        self.horizontalSliderGValue.setGeometry(QtCore.QRect(350, 160, 261, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.horizontalSliderGValue.setFont(font)
        self.horizontalSliderGValue.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalSliderGValue.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSliderGValue.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.horizontalSliderGValue.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalSliderGValue.setAutoFillBackground(False)
        self.horizontalSliderGValue.setMinimum(-99)
        self.horizontalSliderGValue.setSliderPosition(0)
        self.horizontalSliderGValue.setTracking(True)
        self.horizontalSliderGValue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderGValue.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSliderGValue.setTickInterval(0)
        self.horizontalSliderGValue.setObjectName("horizontalSliderGValue")
        self.horizontalSliderBValue = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderBValue.hide()
        self.horizontalSliderBValue.setGeometry(QtCore.QRect(350, 210, 261, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.horizontalSliderBValue.setFont(font)
        self.horizontalSliderBValue.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalSliderBValue.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.horizontalSliderBValue.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.horizontalSliderBValue.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalSliderBValue.setAutoFillBackground(False)
        self.horizontalSliderBValue.setMinimum(-99)
        self.horizontalSliderBValue.setSliderPosition(0)
        self.horizontalSliderBValue.setTracking(True)
        self.horizontalSliderBValue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderBValue.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSliderBValue.setTickInterval(0)
        self.horizontalSliderBValue.setObjectName("horizontalSliderBValue")

        self.lineFunction = QtWidgets.QLineEdit(self.centralwidget)
        self.lineFunction.setGeometry(QtCore.QRect(200, 40, 651, 41))
        self.lineFunction.show()
        sizePolicyLine = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicyLine.setHorizontalStretch(0)
        sizePolicyLine.setVerticalStretch(0)
        sizePolicyLine.setHeightForWidth(self.lineFunction.sizePolicy().hasHeightForWidth())
        self.lineFunction.setSizePolicy(sizePolicyLine)
        self.lineFunction.setAlignment(QtCore.Qt.AlignCenter)
        self.lineFunction.setReadOnly(True)
        self.lineFunction.setObjectName("lineFunction")

        self.lineRValue = QtWidgets.QLineEdit(self.centralwidget)
        self.lineRValue.setGeometry(QtCore.QRect(270, 120, 61, 21))
        self.lineRValue.setObjectName("lineRValue")
        self.lineRValue.hide()

        self.lineGValue = QtWidgets.QLineEdit(self.centralwidget)
        self.lineGValue.setGeometry(QtCore.QRect(270, 170, 61, 21))
        self.lineGValue.setObjectName("lineGValue")
        self.lineGValue.hide()

        self.lineBValue = QtWidgets.QLineEdit(self.centralwidget)
        self.lineBValue.setGeometry(QtCore.QRect(270, 220, 61, 21))
        self.lineBValue.setObjectName("lineBValue")
        self.lineBValue.hide()

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

        self.reset = QtWidgets.QAction(MainWindow)
        self.reset.setObjectName("reset")
        self.reset.triggered.connect(self.resetImgClick)

        self.horizontalSlider.valueChanged.connect(lambda: self.sliderHandler(self.toolType))
        self.horizontalSliderRValue.valueChanged.connect(lambda: self.sliderHandler('colorbalance_R'))
        self.horizontalSliderGValue.valueChanged.connect(lambda: self.sliderHandler('colorbalance_G'))
        self.horizontalSliderBValue.valueChanged.connect(lambda: self.sliderHandler('colorbalance_B'))

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
        self.menuTools.addAction(self.reset)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.original_image_label.setText(_translate("MainWindow", "Original Image"))
        self.edited_image_label.setText(_translate("MainWindow", "Edited Image"))
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
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.lineFunction.setText(_translate("MainWindow", "Image Editor"))
        self.lineRValue.setText(_translate("MainWindow", "R Value:"))
        self.lineGValue.setText(_translate("MainWindow", "G Value:"))
        self.lineBValue.setText(_translate("MainWindow", "B Value:"))

    def openImgClick(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files(*);;PNG(*.png);;JPG(*.jpg)")
        if fname[0] != '':
            self.original_image_cv2 = cv2.imread(fname[0])
            self.edited_image_cv2 = cv2.imread(fname[0])
            self.edited_image_copy_cv2 = cv2.imread(fname[0])
            self.showImage(self.original_image_cv2, self.original_image_label)
            self.showItemsHandler('Image opened. You can start to edit your image now.', False, False)
            self.isGrayScaled = False

    def saveImgClick(self):
        if not self.checkInit():
            return
        dir_name = QFileDialog.getSaveFileName(self, "Save File", "", "All Files(*);;PNG(*.png);;JPG(*.jpg)")
        if dir_name[0] != '':
            fileName = dir_name[0]
            if not (('.png' in fileName) or ('.jpg' in fileName) or ('.jpeg' in fileName)):
                fileName = fileName + '.png'
            cv2.imwrite(fileName, self.edited_image_cv2)
            self.showItemsHandler(f'Your edited image saved successfully to {fileName}', False, False)

    def blurImgClick(self):
        if not self.checkInit():
            return
        self.toolType = 'blur'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setSliderPosition(0)
        self.showItemsHandler('Blur Image', True, False)

    def blurImg(self, val):
        self.edited_image_cv2 = cv2.blur(self.edited_image_copy_cv2, (val, val))
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def deblurImgClick(self):
        if not self.checkInit():
            return

        self.toolType = 'deblur'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setSliderPosition(0)
        self.showItemsHandler('Deblur Image', True, False)

    def deblurImg(self, val):
        pil_img = self.cv2_to_pil(self.edited_image_copy_cv2)
        enhancer = ImageEnhance.Sharpness(pil_img)
        factor = 1 + val
        im_output = enhancer.enhance(factor)
        self.edited_image_cv2 = self.pil_to_cv2(im_output)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def grayscaleImgClick(self):
        if not self.checkInit():
            return

        self.isGrayScaled = True
        self.edited_image_cv2 = cv2.cvtColor(self.edited_image_cv2, cv2.cv2.COLOR_BGR2GRAY)
        self.edited_image_cv2 = cv2.cvtColor(self.edited_image_cv2, cv2.cv2.COLOR_RGB2BGR)
        self.showImage(self.edited_image_cv2, self.edited_image_label)
        self.isGrayScaled = True
        self.showItemsHandler('Grayscaled Image', False, False)

    def flipImgClick(self):
        if not self.checkInit():
            return

        self.edited_image_cv2 = cv2.flip(self.edited_image_cv2, 0)
        self.showImage(self.edited_image_cv2, self.edited_image_label)
        self.showItemsHandler('Flipped Image', False, False)

    def mirrorImgClick(self):
        if not self.checkInit():
            return

        self.edited_image_cv2 = cv2.flip(self.edited_image_cv2, 1)
        self.showImage(self.edited_image_cv2, self.edited_image_label)
        self.showItemsHandler('Mirrored Image', False, False)

    def rotateImgClick(self):
        if not self.checkInit():
            return

        self.edited_image_cv2 = cv2.rotate(self.edited_image_cv2, cv2.ROTATE_90_CLOCKWISE)
        self.showImage(self.edited_image_cv2, self.edited_image_label)
        self.showItemsHandler('Rotated Image', False, False)

    def reversecolorImgClick(self):
        if not self.checkInit():
            return

        self.edited_image_cv2 = cv2.bitwise_not(self.edited_image_cv2)
        self.showImage(self.edited_image_cv2, self.edited_image_label)
        self.showItemsHandler('Reverse Color Image', False, False)

    def cropImgClick(self):
        if not self.checkInit():
            return

        r = cv2.selectROI(self.edited_image_cv2)
        cv2.destroyAllWindows()
        self.edited_image_cv2 = self.edited_image_cv2[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])].copy()
        self.showImage(self.edited_image_cv2, self.edited_image_label)
        self.showItemsHandler('Cropped Image', False, False)

    def resetImgClick(self):
        if not self.checkInit():
            return

        self.edited_image_cv2 = self.original_image_cv2.copy()
        self.showImage(self.edited_image_cv2, self.edited_image_label)
        self.showItemsHandler('Reset Image', False, False)

    def detectEdgeImgClick(self):
        if not self.checkInit():
            return

        grayscale = cv2.cvtColor(self.edited_image_cv2, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(grayscale, (5, 5), 1)
        self.edited_image_cv2 = cv2.Canny(blurred_image, threshold1=100, threshold2=100)
        self.showImage(self.edited_image_cv2, self.edited_image_label)
        self.showItemsHandler('Detect Edge Image', False, False)

    def saturationImgClick(self):
        if not self.checkInit():
            return

        if self.isGrayScaled:
            self.showItemsHandler('You can not do saturation on grayscaled image.', False, False)
            return

        self.toolType = 'saturation'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSlider.setMinimum(-99)
        self.horizontalSlider.setSliderPosition(0)
        self.showItemsHandler('Adjust Saturation Image', True, False)

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
        if not self.checkInit():
            return

        if self.isGrayScaled:
            self.showItemsHandler('You can not do color balance on grayscaled image.', False, False)
            return

        self.toolType = 'colorbalance'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSliderRValue.setMinimum(-99)
        self.horizontalSliderRValue.setSliderPosition(0)

        self.horizontalSliderGValue.setMinimum(-99)
        self.horizontalSliderGValue.setSliderPosition(0)

        self.horizontalSliderBValue.setMinimum(-99)
        self.horizontalSliderBValue.setSliderPosition(0)

        self.showItemsHandler('Color Balance Image', True, True)

    def colorBalanceImg(self, val, ch):
        if ch == 'R':
            self.edited_image_cv2[:, :, 2] = cv2.add(self.edited_image_copy_cv2[:, :, 2], val)
        elif ch == 'G':
            self.edited_image_cv2[:, :, 1] = cv2.add(self.edited_image_copy_cv2[:, :, 1], val)
        elif ch == 'B':
            self.edited_image_cv2[:, :, 0] = cv2.add(self.edited_image_copy_cv2[:, :, 0], val)

        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def noiseImgClick(self):
        if not self.checkInit():
            return

        self.toolType = 'noise'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setSliderPosition(0)
        self.showItemsHandler('Adjust Noise Image', True, False)

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

    def brightnessImgClick(self):
        if not self.checkInit():
            return

        self.toolType = 'brightness'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSlider.setMinimum(-99)
        self.horizontalSlider.setSliderPosition(0)
        self.showItemsHandler('Adjust Brightness Image', True, False)

    def brightnessImg(self, sliderVal):
        pil_img = self.cv2_to_pil(self.edited_image_copy_cv2)
        enhancer = ImageEnhance.Brightness(pil_img)
        factor = 1 + sliderVal
        im_output = enhancer.enhance(factor)
        self.edited_image_cv2 = self.pil_to_cv2(im_output)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

    def contrastImgClick(self):
        if not self.checkInit():
            return

        self.toolType = 'contrast'
        self.edited_image_copy_cv2 = self.edited_image_cv2.copy()
        self.horizontalSlider.setMinimum(-99)
        self.horizontalSlider.setSliderPosition(0)
        self.showItemsHandler('Adjust Contrast Image', True, False)

    def contrastImg(self, val):
        pil_img = self.cv2_to_pil(self.edited_image_copy_cv2)
        enhancer = ImageEnhance.Contrast(pil_img)
        factor = 1 + val
        im_output = enhancer.enhance(factor)
        self.edited_image_cv2 = self.pil_to_cv2(im_output)
        self.showImage(self.edited_image_cv2, self.edited_image_label)

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

        elif 'colorbalance' in toolType:
            ch = toolType[-1]
            val = 0
            if ch == 'R':
                val = self.horizontalSliderRValue.value()
            elif ch == 'G':
                val = self.horizontalSliderGValue.value()
            elif ch == 'B':
                val = self.horizontalSliderBValue.value()

            self.colorBalanceImg(val, ch)

        return val

    def showItemsHandler(self, funcType, withSlider, isColorBalance):
        self.lineFunction.setText(funcType)
        if withSlider:
            self.horizontalSlider.show()
            self.horizontalSliderRValue.hide()
            self.horizontalSliderGValue.hide()
            self.horizontalSliderBValue.hide()
            self.lineRValue.hide()
            self.lineGValue.hide()
            self.lineBValue.hide()
            if isColorBalance:
                self.horizontalSlider.hide()
                self.horizontalSliderRValue.show()
                self.horizontalSliderGValue.show()
                self.horizontalSliderBValue.show()
                self.lineRValue.show()
                self.lineGValue.show()
                self.lineBValue.show()
        else:
            self.horizontalSlider.hide()
            self.horizontalSliderRValue.hide()
            self.horizontalSliderGValue.hide()
            self.horizontalSliderBValue.hide()
            self.lineRValue.hide()
            self.lineGValue.hide()
            self.lineBValue.hide()

        pass

    def checkInit(self):
        if self.original_image_cv2 is None:
            self.lineFunction.setText('You must load an image before making operations!')
            return False
        return True


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
