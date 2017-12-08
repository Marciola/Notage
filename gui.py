''' Brandon Polonia bp13d '''

import sys
import notepage
from PyQt5 import QtWidgets, QtCore, QtGui


imageName = ""

class Window(QtWidgets.QMainWindow):

	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.setup()

	def setup(self):
		self.setGeometry(600,600,700,700)
		Image = QtGui.QImage("background.png")
		sImage = Image.scaled(QtCore.QSize(800,800))
		palette = QtGui.QPalette()
		palette.setBrush(10, QtGui.QBrush(sImage))
		self.setPalette(palette)

		central_widget = QtWidgets.QWidget(self)
		pictureLayout(central_widget)
		self.setCentralWidget(central_widget)

		exitbutton = QtWidgets.QAction("Exit", self)
		exitbutton.setStatusTip("Exit Application")
		exitbutton.triggered.connect(QtWidgets.qApp.quit)
		uploadbutton = QtWidgets.QAction("Upload", self)
		uploadbutton.triggered.connect(self.uploadImage)
		mainMenu = self.menuBar()
		mainMenu.setNativeMenuBar(False)
		mfile = mainMenu.addMenu("File")
		mfile.addAction(uploadbutton)
		mfile.addAction(exitbutton)
		self.setMenuBar(mainMenu)

		eicon = QtGui.QIcon("index.png")
		eButton = QtWidgets.QPushButton("Encode",EncodeButton(self))
		eButton.setIcon(eicon)
		eButton.clicked.connect(self.getText)
		dicon = QtGui.QIcon("index.jpeg")
		dButton = QtWidgets.QPushButton("Decode",DecodeButton(self))
		dButton.setIcon(dicon)
		dButton.clicked.connect(self.decodeAction)
		self.show()

	def getText(self):
		text, okPressed = QtWidgets.QInputDialog.getText(self," ", "Message to be encoded:", QtWidgets.QLineEdit.Normal, "")
		File = open(imageName)
		notepage.encodeMessage(File,text)

	def decodeAction(self):
		File = open(imageName)
		notepage.decodeMessage(File)

	def uploadImage(self):
		filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open File"," ","*.png")
		a, b = filename
		label = QtWidgets.QLabel(self)
		pixmap = QtGui.QPixmap(a)
		global imageName
		imageName= parseDir(a)
		label.setPixmap(pixmap)
		label.setFixedSize(500,500)
		label.move(100,50)
		self.setCentralWidget(label)

class EncodeButton(QtWidgets.QPushButton):
	def __init__(self,parent):
		QtWidgets.QPushButton.__init__(self,parent)
		self.move(150,600)
		self.resize(87,29)

class DecodeButton(QtWidgets.QPushButton):
	def __init__(self,parent):
		QtWidgets.QPushButton.__init__(self,parent)
		self.move(450,600)
		self.resize(87,29)

class pictureLayout(QtWidgets.QWidget):
	def __init__(self,parent):
		QtWidgets.QWidget.__init__(self,parent)
		self.setFixedSize(500,500)
		p = self.palette()
		p.setColor(self.backgroundRole(),QtCore.Qt.white)
		self.setPalette(p)
		self.setAutoFillBackground(True)
		self.move(100,50)

def parseDir(directory):
	splitDirectory = directory.split("/")
	for names in splitDirectory:
		if ".png" in names:
			return names

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	main_window = Window()
	app.exec_()
