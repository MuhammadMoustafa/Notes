from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from gui import Ui_MainWindow
import sys
from time import sleep
import random

class ApplicationWindow(QtWidgets.QMainWindow):

    onNumberGenerated = pyqtSignal(int)

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.onNumberGenerated.connect(self.updateAll)
        self.ui.pushButton.clicked.connect(self.generateNumber)

    def generateNumber(self):
        number = random.randint(0, 100)
        self.onNumberGenerated.emit(number)

    def updateAll(self, number):
        self.ui.progressBar.setValue(number)
        self.ui.spinBox.setValue(number)
        self.ui.verticalSlider.setValue(number)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
