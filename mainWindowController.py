from PyQt5 import QtWidgets
from UI.mainWindow import Ui_MainWindow
import numpy as np
import cv2
import sys
import imghdr


class MainWindowController(object):
    def __init__(self):
        self.image = None
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.__setup()  

    def __setup(self):
        pass

        
if __name__ == "__main__":
    ctr = MainWindowController()
    ctr.MainWindow.show()
    sys.exit(ctr.app.exec_()) 