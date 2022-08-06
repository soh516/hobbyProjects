import sys
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
        

        layout.addWidget(self.inputFileButton)
        layout.addWidget(self.inputFileLabel)
        layout.addLayout(self.algorithm1Layout)
        layout.addLayout(self.algorithm2Layout)
        
        self.widget = QWidget(self)
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

        self.show()

    def algorithem1Group(self):
        self.processButton1 = QPushButton("Process Image With Algorithm 1",self)
        self.processButton1.setStyleSheet("QPushButton"
                                                                "{"
                                                                "color : red;"
                                                                "}")
        self.processButton1.clicked.connect(self.processImage1)
        self.saveButton1 = QPushButton("Save results", self)

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
        algorithm1(self.inputFileStr)

    def processImage2(self):
        algorithm2(self.inputFileStr)




# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())
