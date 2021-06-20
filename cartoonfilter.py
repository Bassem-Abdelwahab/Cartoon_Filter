# This Python file uses the following encoding: utf-8
import sys
from sklearn.cluster import MiniBatchKMeans
# import os
from Filter import Ui_Filter
from PySide2.QtWidgets import QApplication , QWidget , QFileDialog , QGraphicsScene , QMessageBox
#from PySide2.QtWidgets import *
from PySide2.QtCore import Qt , QFile, QDir , QIODevice ,QObject , Slot , QPointF
from PySide2.QtGui import QImage , QColor, QPixmap , QPainter
#from PySide2.QtUiTools import QUiLoader
#from PySide2.QtSql import QSqlDatabase , QSqlQuery
import cv2
import numpy as np


class CartoonFilter(QWidget):
    def __init__(self):
        super(CartoonFilter,self).__init__()
        self.ui = Ui_Filter()
        self.ui.setupUi(self)
        self.ui.frameWidget.hide()
        self.ui.frameSlider.valueChanged.connect(self.on_frameSlider_valueChanged)
        self.ui.frameSpinBox.valueChanged.connect(self.on_frameSpinBox_valueChanged)
        self.ui.inputTypeComboBox.currentIndexChanged.connect(self.on_inputTypeComboBox_currentIndexChanged)
        self.ui.openButton.clicked.connect(self.on_openButton_clicked)
        self.ui.saveButton.clicked.connect(self.on_saveButton_clicked)
        self.ui.previewOriginalButton.released.connect(self.on_previewOriginalButton_released)
        self.ui.noColorsSpinBox.valueChanged.connect(self.on_noColorsSpinBox_valueChanged)
        self.ui.noShadesSpinBox.valueChanged.connect(self.on_noShadesSpinBox_valueChanged)
        self.ui.strokeWidthSlider.valueChanged.connect(self.on_strokeWidthSlider_valueChanged)
        self.ui.highEdgeDetectionSlider.valueChanged.connect(self.on_highEdgeDetectionSlider_valueChanged)
        self.ui.lowEdgeDetectionSlider.valueChanged.connect(self.on_lowEdgeDetectionSlider_valueChanged)
        self.ui.previewOriginalButton.pressed.connect(self.on_previewOriginalButton_pressed)
        self.ui.colorThresholdSlider.valueChanged.connect(self.on_colorThresholdSlider_valueChanged)

        self.ui.inputTypeComboBox.hide()
        self.scene = QGraphicsScene()
        self.ui.ImagePreview.setScene(self.scene)
        self.kernel = 0
        self.cannyEdges =0
        self.dilatedEdges = 0
        self.imageHues = 0
        self.imageVals = 0
        self.hsv_image =0
        self.filteredImage = 0
        self.previewImage = 0
        self.inputExists=False
        self.fileName=""
        self.inputTypeIndex=0
        self.originalImage=0
        self.originalVideo=0
        self.cannyMinVal = 100
        self.cannyMaxVal = 200
        self.strokeWidth = 2
        self.noColors = 8
        self.noShades = 2
        self.colorThresh = 128
        self.strokeChanged = False
        self.cannyChanged = False
        self.colorChanged = False
        self.shadeChanged = False
        self.threshChanged = False

    def on_frameSlider_valueChanged(self , value):
        self.ui.frameSpinBox.setValue(value)
        self.originalVideo.set(cv2.CAP_PROP_POS_FRAMES , value)
        ret , frm = self.originalVideo.read()
        if ret == True:
            self.originalImage = frm.copy()
            self.apply_filter()

    def on_frameSpinBox_valueChanged(self , value):
        self.ui.frameSlider.setValue(value)
        self.on_frameSlider_valueChanged(value)

    def on_inputTypeComboBox_currentIndexChanged(self , index):
        self.inputTypeIndex = index

    def on_openButton_clicked(self):
        if self.inputTypeIndex == 0:
            temp = QFileDialog.getOpenFileName(self, "Open File",".","Images (*.png *.jpg)")
            self.fileName = temp[0]
        else :
            temp = QFileDialog.getOpenFileName(self,"Open File",".","Videos (*.mp4 *.mkv)")
            self.fileName = temp[0]
        self.openFile()

    def on_saveButton_clicked(self):
        path = self.fileName.split('/')
        file = path[-1].split('.')
        output_path = ""
        for i in range(len(path)-1):
            output_path += path[i]
            output_path += '/'
        output_path+=file[0]
        output_path+="_cartoon"
        output_path+='.'
        
        if self.ui.frameWidget.isVisible() and self.inputTypeIndex == 1:
            output_path+='mp4'
            savefileName =  QFileDialog.getSaveFileName(self, "Save File",output_path,"Videos (*.mp4)")
            if savefileName :
                frameRate = self.originalVideo.get(cv2.CAP_PROP_FPS)
                hght = self.originalVideo.get(cv2.CAP_PROP_FRAME_HEIGHT)
                wdth = self.originalVideo.get(cv2.CAP_PROP_FRAME_WIDTH)
                fourcc = cv2.VideoWriter_fourcc('M','P','4','A') 
                out = cv2.videoWriter(savefileName , fourcc , frameRate , (hght,wdth))
        else :
            output_path+=file[1]
            savefileName =  QFileDialog.getSaveFileName(self, "Save File",output_path,"Images (*.png *.jpg)")
            if savefileName :
                status = cv2.imwrite(savefileName[0] , self.filteredImage)
                msgBox = QMessageBox()
                if status :
                    msgBox.setText("Image saved successfully")
                else :
                    msgBox.setText("Image saving failed")
                msgBox.exec()

    def on_previewOriginalButton_pressed(self):
        self.previewImage = self.originalImage
        self.updatePreview()

    def on_previewOriginalButton_released(self):
        self.previewImage = self.filteredImage
        self.updatePreview()

    def on_noColorsSpinBox_valueChanged(self , value):
        self.noColors = value
        self.colorChanged = True
        self.apply_filter()

    def on_noShadesSpinBox_valueChanged(self , value):
        self.noShades = value
        self.shadeChanged = True
        self.apply_filter()

    def on_strokeWidthSlider_valueChanged(self , value):
        self.strokeWidth = value
        self.strokeChanged = True
        self.apply_filter()

    def on_highEdgeDetectionSlider_valueChanged(self , value):
        self.cannyMaxVal = value
        self.cannyChanged = True
        self.apply_filter()

    def on_lowEdgeDetectionSlider_valueChanged(self , value):
        self.cannyMinVal = value
        self.cannyChanged = True
        self.apply_filter()

    def on_colorThresholdSlider_valueChanged(self , value):
        self.colorThresh = value
        self.threshChanged = True
        self.apply_filter()

    def resizeEvent(self , ev):
        self.updatePreview()

    def openFile(self):
        if self.fileName:
            self.inputExists = True
            self.strokeChanged = True
            self.colorChanged = True
            self.shadeChanged = True
            self.cannyChanged = True
            self.threshChanged = True
            if self.inputTypeIndex == 0:
                self.ui.frameWidget.hide()
                self.originalVideo=0
                self.originalImage = cv2.imread(self.fileName)
                self.hsv_image = cv2.cvtColor(self.originalImage, cv2.COLOR_BGR2HSV)
            else :
                self.ui.frameWidget.show()
                self.originalVideo = cv2.VideoCapture(self.fileName)
                self.totalFrames = self.originalVideo.get(cv2.CAP_PROP_FRAME_COUNT)
                self.ui.frameSlider.setMaximum(self.totalFrames-1)
                self.ui.frameSlider.setValue(int(self.totalFrames/2))
                self.ui.frameSpinBox.setSuffix("/"+str(self.totalFrames))
                self.ui.frameSpinBox.setValue(int(self.totalFrames/2))
                self.originalVideo.set(cv2.CAP_PROP_POS_FRAMES , int(self.totalFrames/2))
                ret, frm = self.originalVideo.read()
                self.originalVideo.set(cv2.CAP_PROP_POS_FRAMES , 0)
                self.originalImage = frm
            
            self.apply_filter()

    def apply_filter(self):
        if self.inputExists == True:
            if self.cannyChanged == True:
                self.cannyChanged = False
                self.cannyEdges = cv2.Canny(self.originalImage,self.cannyMinVal , self.cannyMaxVal)
            if self.strokeChanged == True:
                self.strokeChanged = False
                self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(self.strokeWidth+1,self.strokeWidth+1))
                
            if self.colorChanged == True:
                self.colorChanged =False
                hues = self.hsv_image[:,:,0]
                hues_lab = cv2.cvtColor( hues , cv2.COLOR_GRAY2BGR)
                hues_lab = cv2.cvtColor( hues_lab , cv2.COLOR_BGR2LAB)
                hues_lab = hues_lab.reshape((self.originalImage.shape[0] * self.originalImage.shape[1],3))
                clt = MiniBatchKMeans(n_clusters = self.noColors)
                labels = clt.fit_predict(hues_lab)
                quant_h = clt.cluster_centers_.astype("uint8")[labels]
                quant_h = quant_h.reshape((self.originalImage.shape[0], self.originalImage.shape[1],3))
                self.imageHues = cv2.cvtColor(cv2.cvtColor(quant_h, cv2.COLOR_LAB2BGR), cv2.COLOR_BGR2GRAY)

            if self.shadeChanged == True:
                self.shadeChanged =False
                vals = self.hsv_image[:,:,2]
                vals_lab = cv2.cvtColor( vals , cv2.COLOR_GRAY2BGR)
                vals_lab = cv2.cvtColor( vals_lab , cv2.COLOR_BGR2LAB)
                vals_lab = vals_lab.reshape((self.originalImage.shape[0] * self.originalImage.shape[1],3))
                clt = MiniBatchKMeans(n_clusters = self.noShades)
                labels = clt.fit_predict(vals_lab)
                quant_v = clt.cluster_centers_.astype("uint8")[labels]
                quant_v = quant_v.reshape((self.originalImage.shape[0], self.originalImage.shape[1],3))
                self.imageVals = cv2.cvtColor(cv2.cvtColor(quant_v, cv2.COLOR_LAB2BGR),cv2.COLOR_BGR2GRAY)

            if self.threshChanged == True:
                self.threshChanged =False
                higher_white = np.array([179 , 90 , 255])
                lower_white = np.array([0,0,215])
                mask = cv2.inRange(self.hsv_image ,lower_white,higher_white)
                self.hsv_image[mask == 0 , 1] = self.colorThresh

            self.filteredImage = self.hsv_image.copy()
            self.filteredImage[:,:,0] = self.imageHues
            self.filteredImage[:,:,2] = self.imageVals
            self.filteredImage = cv2.cvtColor(self.filteredImage, cv2.COLOR_HSV2BGR)
            self.dilatedEdges = cv2.dilate(self.cannyEdges,self.kernel,iterations = 1)
            self.filteredImage[self.dilatedEdges != 0]=  [0,0,0]
            self.previewImage = self.filteredImage
            self.updatePreview()

    def updatePreview(self):
        if self.inputExists == True:
            if len(self.previewImage.shape) == 2:
                height, width = self.previewImage.shape
                bytesPerLine = width
                qImg = QImage(self.previewImage.data, width, height, bytesPerLine, QImage.Format_Grayscale8)
            elif len(self.previewImage.shape) == 3:
                height, width, channel = self.previewImage.shape
                bytesPerLine = 3*width
                qImg = QImage(self.previewImage.data, width, height, bytesPerLine, QImage.Format_BGR888)
            tempPreview = QPixmap.fromImage(qImg)
            tempPreview = tempPreview.scaled(int(self.ui.ImagePreview.width()*99/100), int(self.ui.ImagePreview.height()*99/100),Qt.KeepAspectRatio)
            self.scene.clear()
            self.scene.addPixmap(tempPreview)

        else:
            self.scene.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = CartoonFilter()
    window.show()
    sys.exit(app.exec_())
