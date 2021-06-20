# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FilterytMchQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Filter(object):
    def setupUi(self, Filter):
        if Filter.objectName():
            Filter.setObjectName(u"Filter")
        Filter.resize(666, 497)
        self.verticalLayout = QVBoxLayout(Filter)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ImagePreview = QGraphicsView(Filter)
        self.ImagePreview.setObjectName(u"ImagePreview")

        self.verticalLayout.addWidget(self.ImagePreview)

        self.frameWidget = QWidget(Filter)
        self.frameWidget.setObjectName(u"frameWidget")
        self.frameWidget.setEnabled(True)
        self.horizontalLayout_3 = QHBoxLayout(self.frameWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frameSlider = QSlider(self.frameWidget)
        self.frameSlider.setObjectName(u"frameSlider")
        self.frameSlider.setSliderPosition(50)
        self.frameSlider.setTracking(False)
        self.frameSlider.setOrientation(Qt.Horizontal)
        self.frameSlider.setInvertedAppearance(False)
        self.frameSlider.setInvertedControls(False)
        self.frameSlider.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_3.addWidget(self.frameSlider)

        self.frameLabel = QLabel(self.frameWidget)
        self.frameLabel.setObjectName(u"frameLabel")

        self.horizontalLayout_3.addWidget(self.frameLabel)

        self.frameSpinBox = QSpinBox(self.frameWidget)
        self.frameSpinBox.setObjectName(u"frameSpinBox")
        self.frameSpinBox.setWrapping(True)
        self.frameSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.frameSpinBox.setKeyboardTracking(False)

        self.horizontalLayout_3.addWidget(self.frameSpinBox)


        self.verticalLayout.addWidget(self.frameWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.previewOriginalButton = QPushButton(Filter)
        self.previewOriginalButton.setObjectName(u"previewOriginalButton")

        self.horizontalLayout.addWidget(self.previewOriginalButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.inputTypeComboBox = QComboBox(Filter)
        self.inputTypeComboBox.addItem("")
        self.inputTypeComboBox.addItem("")
        self.inputTypeComboBox.setObjectName(u"inputTypeComboBox")

        self.horizontalLayout.addWidget(self.inputTypeComboBox)

        self.openButton = QPushButton(Filter)
        self.openButton.setObjectName(u"openButton")

        self.horizontalLayout.addWidget(self.openButton)

        self.saveButton = QPushButton(Filter)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.optionsGroupBox = QGroupBox(Filter)
        self.optionsGroupBox.setObjectName(u"optionsGroupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.optionsGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.strokeWidthLabel = QLabel(self.optionsGroupBox)
        self.strokeWidthLabel.setObjectName(u"strokeWidthLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.strokeWidthLabel)

        self.strokeWidthSlider = QSlider(self.optionsGroupBox)
        self.strokeWidthSlider.setObjectName(u"strokeWidthSlider")
        self.strokeWidthSlider.setMaximum(15)
        self.strokeWidthSlider.setPageStep(2)
        self.strokeWidthSlider.setValue(2)
        self.strokeWidthSlider.setTracking(False)
        self.strokeWidthSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.strokeWidthSlider)

        self.noColorsLabel = QLabel(self.optionsGroupBox)
        self.noColorsLabel.setObjectName(u"noColorsLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.noColorsLabel)

        self.noColorsSpinBox = QSpinBox(self.optionsGroupBox)
        self.noColorsSpinBox.setObjectName(u"noColorsSpinBox")
        self.noColorsSpinBox.setKeyboardTracking(False)
        self.noColorsSpinBox.setMinimum(1)
        self.noColorsSpinBox.setValue(8)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.noColorsSpinBox)

        self.noShadesLabel = QLabel(self.optionsGroupBox)
        self.noShadesLabel.setObjectName(u"noShadesLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.noShadesLabel)

        self.noShadesSpinBox = QSpinBox(self.optionsGroupBox)
        self.noShadesSpinBox.setObjectName(u"noShadesSpinBox")
        self.noShadesSpinBox.setKeyboardTracking(False)
        self.noShadesSpinBox.setMinimum(1)
        self.noShadesSpinBox.setValue(2)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.noShadesSpinBox)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.horizontalLayout_4.addWidget(self.optionsGroupBox)

        self.edgeDetectionGroupBox = QGroupBox(Filter)
        self.edgeDetectionGroupBox.setObjectName(u"edgeDetectionGroupBox")
        self.formLayout_2 = QFormLayout(self.edgeDetectionGroupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.highEdgeDetectionLabel = QLabel(self.edgeDetectionGroupBox)
        self.highEdgeDetectionLabel.setObjectName(u"highEdgeDetectionLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.highEdgeDetectionLabel)

        self.highEdgeDetectionSlider = QSlider(self.edgeDetectionGroupBox)
        self.highEdgeDetectionSlider.setObjectName(u"highEdgeDetectionSlider")
        self.highEdgeDetectionSlider.setMaximum(255)
        self.highEdgeDetectionSlider.setValue(200)
        self.highEdgeDetectionSlider.setTracking(False)
        self.highEdgeDetectionSlider.setOrientation(Qt.Horizontal)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.highEdgeDetectionSlider)

        self.lowEdgeDetectionLabel = QLabel(self.edgeDetectionGroupBox)
        self.lowEdgeDetectionLabel.setObjectName(u"lowEdgeDetectionLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lowEdgeDetectionLabel)

        self.lowEdgeDetectionSlider = QSlider(self.edgeDetectionGroupBox)
        self.lowEdgeDetectionSlider.setObjectName(u"lowEdgeDetectionSlider")
        self.lowEdgeDetectionSlider.setMaximum(255)
        self.lowEdgeDetectionSlider.setValue(100)
        self.lowEdgeDetectionSlider.setTracking(False)
        self.lowEdgeDetectionSlider.setOrientation(Qt.Horizontal)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lowEdgeDetectionSlider)

        self.colorThresholdLabel = QLabel(self.edgeDetectionGroupBox)
        self.colorThresholdLabel.setObjectName(u"colorThresholdLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.colorThresholdLabel)

        self.colorThresholdSlider = QSlider(self.edgeDetectionGroupBox)
        self.colorThresholdSlider.setObjectName(u"colorThresholdSlider")
        self.colorThresholdSlider.setMaximum(255)
        self.colorThresholdSlider.setValue(128)
        self.colorThresholdSlider.setTracking(False)
        self.colorThresholdSlider.setOrientation(Qt.Horizontal)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.colorThresholdSlider)

        self.highEdgeDetectionSlider.raise_()
        self.lowEdgeDetectionSlider.raise_()
        self.highEdgeDetectionLabel.raise_()
        self.lowEdgeDetectionLabel.raise_()
        self.colorThresholdSlider.raise_()
        self.colorThresholdLabel.raise_()

        self.horizontalLayout_4.addWidget(self.edgeDetectionGroupBox)

        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 10)

        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Filter)

        QMetaObject.connectSlotsByName(Filter)
    # setupUi

    def retranslateUi(self, Filter):
        Filter.setWindowTitle(QCoreApplication.translate("Filter", u"Filter", None))
        self.frameLabel.setText(QCoreApplication.translate("Filter", u"Frame:", None))
        self.frameSpinBox.setSuffix(QCoreApplication.translate("Filter", u"/0", None))
        self.previewOriginalButton.setText(QCoreApplication.translate("Filter", u"Preview Original", None))
        self.inputTypeComboBox.setItemText(0, QCoreApplication.translate("Filter", u"Image", None))
        self.inputTypeComboBox.setItemText(1, QCoreApplication.translate("Filter", u"Video", None))

        self.openButton.setText(QCoreApplication.translate("Filter", u"Open", None))
        self.saveButton.setText(QCoreApplication.translate("Filter", u"Save", None))
        self.optionsGroupBox.setTitle(QCoreApplication.translate("Filter", u"Options", None))
        self.strokeWidthLabel.setText(QCoreApplication.translate("Filter", u"Stroke Width:", None))
        self.noColorsLabel.setText(QCoreApplication.translate("Filter", u"No. of colors:", None))
        self.noShadesLabel.setText(QCoreApplication.translate("Filter", u"No. of shades:", None))
        self.edgeDetectionGroupBox.setTitle(QCoreApplication.translate("Filter", u"Edge Detection Levels", None))
        self.highEdgeDetectionLabel.setText(QCoreApplication.translate("Filter", u"High:", None))
        self.lowEdgeDetectionLabel.setText(QCoreApplication.translate("Filter", u"Low:", None))
        self.colorThresholdLabel.setText(QCoreApplication.translate("Filter", u"Color Thresh.", None))
    # retranslateUi

