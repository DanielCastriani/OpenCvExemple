from UI.mainWindow import Ui_MainWindow

from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage,QPixmap
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
        #Files          
        self.ui.actionOpen.triggered.connect(self.onTriggerd_actionOpen)
        self.ui.actionSave.triggered.connect(self.onTriggerd_actionSave)
        self.ui.actionExit.triggered.connect(self.trigger_actionExit)
        #Colorspace
        self.ui.actionRGB.triggered.connect(self.RGB)
        self.ui.actionHSV.triggered.connect(self.HSV)
        self.ui.actionGrayscale.triggered.connect(self.Grayscale)

    def onTriggerd_actionOpen(self):        
        dialog = QtWidgets.QFileDialog()        
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode())        
        file = dialog.getOpenFileName(None,'Open an image')
        if file and len(file[0]) > 0:
            filePath = file[0]
            isImage = imghdr.what(filePath)           
            print("File Infos:",len(file))
            print("path: ",filePath)
            print("Type: ",file[1])            
            if isImage is not None:
                self.image = cv2.imread(filePath,cv2.IMREAD_UNCHANGED)
                if self.image is None:
                    print("Error")
                else:
                    self.show_image()
            else:
                print("isn't an image")     
        else:
            print("Open a file")

    def onTriggerd_actionSave(self):
        if self.image is not None:
            dialog = QtWidgets.QFileDialog()        
            dialog.setFileMode(QtWidgets.QFileDialog.FileMode())        
            file = dialog.getSaveFileName(None,'Save an image')
            if file and len(file[0]) > 0:
                cv2.imwrite(file[0] +".png",self.image)
        else:
            print("Open an image")

    def trigger_actionExit(self):        
        sys.exit()

    def show_image(self):
        size = self.image.shape
        step = self.image.size / size[0]
        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        else:                    
            qformat = QImage.Format_Indexed8
        img = QImage(self.image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()
        pixMap = QPixmap.fromImage(img)
        self.ui.lbImage.setPixmap(pixMap)
        
    #Show colorspace
    def RGB(self):
        if self.image is not None:                       
            b = self.image.copy()
            b[:,:,0],b[:,:,1],b[:,:,2] = b[:,:,0],0,0
            g = self.image.copy()
            g[:,:,0],g[:,:,1],g[:,:,2] = 0,g[:,:,1],0
            r = self.image.copy()
            r[:,:,0],r[:,:,1],r[:,:,2] = 0,0,r[:,:,2]            
            cv2.imshow('R',r)
            cv2.imshow('G',g)
            cv2.imshow('B',b)

    def HSV(self):
        if self.image is not None:
            hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
            cv2.imshow('HUE',hsv[:,:,0])
            cv2.imshow('SAT',hsv[:,:,1])
            cv2.imshow('VAL',hsv[:,:,2])

    def Grayscale(self):
        if self.image is not None:    
            gs = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)             
            cv2.imshow('Grayscale',gs)
    

if __name__ == "__main__":
    ctr = MainWindowController()
    ctr.MainWindow.show()
    sys.exit(ctr.app.exec_()) 