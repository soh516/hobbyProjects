import sys
from PySide6.QtGui import *
from PySide6.QtCore import *  
from PySide6.QtWidgets import *
from processAlgorithm1 import *
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        self.setGeometry(100, 100, 200, 80)
        self.setWindowTitle('Cartoon')
  
        # creating a vertical layout
        layout = QVBoxLayout()

        self.inputFileButton = QPushButton("Select file for processing", self)
        self.inputFileButton.clicked.connect(self.inputFileDialog)

        self.processButton = QPushButton("Process Image", self)
        self.processButton.setStyleSheet("QPushButton"
                                                                "{"
                                                                "color : red;"
                                                                "}")
        self.processButton.clicked.connect(self.processImage)

        layout.addWidget(self.inputFileButton)
        layout.addWidget(self.processButton)
  
        self.widget = QWidget(self)
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

        self.show()

    def inputFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.inputFileStr, check = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if check:
            print(self.inputFileStr)

    def processImage(self):
        algorithm1(self.inputFileStr)


# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())
