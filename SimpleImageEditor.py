from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

import sys


class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		uic.loadUi("openfile.ui", self)


		self.button = self.findChild(QPushButton, 'pushButton')
		self.label = self.findChild(QLabel, 'label')


		self.button.clicked.connect(self.openFileClick)


		self.show()

	def openFileClick(self):
		fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;PNG (*.png);;JPG (*.jpg)")

		if fname:
			self.pixmap = QPixmap(fname[0])
			self.label.setPixmap(self.pixmap)

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()