import sys
import os
from PySide6.QtGui import *
from PySide6.QtCore import *  
from PySide6.QtWidgets import *
from processAlgorithm import *
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        self.setGeometry(100, 100, 200, 80)
        self.setWindowTitle('Cartoonize Image')
  
        # creating a vertical layout
        layout = QVBoxLayout()

        self.inputFileButton = QPushButton("Select image for processing", self)
        self.inputFileButton.clicked.connect(self.inputFileDialog)

        self.algorithem1Group()
        self.algorithem2Group()

        self.inputFileLabel = QLabel(self)
        self.inputFileLabel.setAlignment(Qt.AlignLeft)
        self.inputFileLabel.setStyleSheet("QLabel"
                                                                "{"
                                                                "color : green;"
                                                                "}")
        

        self.outputFileLabel1 = QLabel(self)
        self.outputFileLabel1.setAlignment(Qt.AlignLeft)

        self.outputFileLabel2 = QLabel(self)
        self.outputFileLabel2.setAlignment(Qt.AlignLeft)

        layout.addWidget(self.inputFileButton)
        layout.addWidget(self.inputFileLabel)
        layout.addLayout(self.algorithm1Layout)
        layout.addLayout(self.algorithm2Layout)
        layout.addWidget(self.outputFileLabel1)
        layout.addWidget(self.outputFileLabel2)
        
        self.widget = QWidget(self)
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

        self.show()

    def outputLabelColor(self, colorSelection):
        self.outputFileLabel1.setStyleSheet("QLabel { color : %s;}" % (colorSelection))
        self.outputFileLabel2.setStyleSheet("QLabel { color : %s;}" % (colorSelection))

    def algorithem1Group(self):
        self.processButton1 = QPushButton("Process Image With Algorithm 1",self)
        self.processButton1.setStyleSheet("QPushButton"
                                                                "{"
                                                                "color : red;"
                                                                "}")
        self.processButton1.clicked.connect(self.processImage1)
        
        self.saveButton1 = QPushButton("Save results", self)
        self.saveButton1.clicked.connect(self.saveImage1)

        self.algorithm1Layout = QHBoxLayout()
        self.algorithm1Layout.addWidget(self.processButton1)
        self.algorithm1Layout.addWidget(self.saveButton1)

    def algorithem2Group(self):
        self.processButton2 = QPushButton("Process Image With Algorithm 2",self)
        self.processButton2.setStyleSheet("QPushButton"
                                                                "{"
                                                                "color : red;"
                                                                "}")
        self.processButton2.clicked.connect(self.processImage2)
        
        self.saveButton2 = QPushButton("Save results", self)
        self.saveButton2.clicked.connect(self.saveImage2)

        self.inputFileLabel = QLabel(self)
        self.inputFileLabel.setAlignment(Qt.AlignCenter)


        self.algorithm2Layout = QHBoxLayout()
        self.algorithm2Layout.addWidget(self.processButton2)
        self.algorithm2Layout.addWidget(self.saveButton2)

    def inputFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.inputFileStr, check = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Image Files (*.jpg)", options=options)
        if check:
            self.inputFileLabel.setText("Input file: " + self.inputFileStr)
            #print(self.inputFileStr)

    def processImage1(self):
        try:
            self.algo1_edge, self.algo1_cartoon = algorithm1(self.inputFileStr)
        except:
            self.outputLabelColor("red")
            self.outputFileLabel1.setText("Select image first!!!!")
            self.outputFileLabel2.clear()




    def processImage2(self):
        try:
            self.algo2_edge, self.algo2_cartoon = algorithm2(self.inputFileStr)
        except:
            self.outputLabelColor("red")
            self.outputFileLabel1.setText("Select image first!!!!")
            self.outputFileLabel2.clear()

    def saveImage1(self):
        try:
            path, baseFileName = os.path.split(self.inputFileStr)
            # -1 index will point at the last element of the list
            fileExtension = baseFileName.split(".")[-1]
            baseFileNameOnly = baseFileName.split(".")[0]
            saveFileStr1 = path + "/" + baseFileNameOnly + "_algo1_edge." + fileExtension
            saveFileStr2 = path + "/" + baseFileNameOnly + "_algo1_cartoon." + fileExtension
            cv2.imwrite(saveFileStr1, self.algo1_edge)
            cv2.imwrite(saveFileStr2, self.algo1_cartoon)
            self.outputLabelColor("green")
            self.outputFileLabel1.setText(saveFileStr1)
            self.outputFileLabel2.setText(saveFileStr2)
        except:
            self.outputLabelColor("red")
            self.outputFileLabel1.setText("Process image first!!!!")
            self.outputFileLabel2.clear()


    def saveImage2(self):
        try:
            path, baseFileName = os.path.split(self.inputFileStr)
            # -1 index will point at the last element of the list
            fileExtension = baseFileName.split(".")[-1]
            baseFileNameOnly = baseFileName.split(".")[0]
            saveFileStr1 = path + "/" + baseFileNameOnly + "_algo2_edge." + fileExtension
            saveFileStr2 = path + "/" + baseFileNameOnly + "_algo2_cartoon." + fileExtension
            cv2.imwrite(saveFileStr1, self.algo2_edge)
            cv2.imwrite(saveFileStr2, self.algo2_cartoon)
            self.outputLabelColor("green")
            self.outputFileLabel1.setText(saveFileStr1)
            self.outputFileLabel2.setText(saveFileStr2)
        except:
            self.outputLabelColor("red")
            self.outputFileLabel1.setText("Process image first!!!!")
            self.outputFileLabel2.clear()

# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())
