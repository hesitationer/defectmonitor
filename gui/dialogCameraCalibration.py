# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogCameraCalibration.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dialogCameraCalibration(object):
    def setupUi(self, dialogCameraCalibration):
        dialogCameraCalibration.setObjectName(_fromUtf8("dialogCameraCalibration"))
        dialogCameraCalibration.resize(411, 646)
        dialogCameraCalibration.setMinimumSize(QtCore.QSize(411, 646))
        dialogCameraCalibration.setMaximumSize(QtCore.QSize(411, 646))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogCameraCalibration.setWindowIcon(icon)
        self.labelInformation = QtGui.QLabel(dialogCameraCalibration)
        self.labelInformation.setGeometry(QtCore.QRect(10, 10, 391, 81))
        self.labelInformation.setScaledContents(False)
        self.labelInformation.setWordWrap(True)
        self.labelInformation.setObjectName(_fromUtf8("labelInformation"))
        self.buttonBrowseF = QtGui.QPushButton(dialogCameraCalibration)
        self.buttonBrowseF.setGeometry(QtCore.QRect(310, 99, 91, 28))
        self.buttonBrowseF.setObjectName(_fromUtf8("buttonBrowseF"))
        self.buttonStart = QtGui.QPushButton(dialogCameraCalibration)
        self.buttonStart.setEnabled(False)
        self.buttonStart.setGeometry(QtCore.QRect(10, 608, 91, 28))
        self.buttonStart.setObjectName(_fromUtf8("buttonStart"))
        self.buttonDone = QtGui.QPushButton(dialogCameraCalibration)
        self.buttonDone.setGeometry(QtCore.QRect(310, 608, 91, 28))
        self.buttonDone.setObjectName(_fromUtf8("buttonDone"))
        self.progressBar = QtGui.QProgressBar(dialogCameraCalibration)
        self.progressBar.setGeometry(QtCore.QRect(10, 438, 391, 28))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.labelStatus = QtGui.QLabel(dialogCameraCalibration)
        self.labelStatus.setGeometry(QtCore.QRect(10, 404, 391, 28))
        self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.labelImages = QtGui.QLabel(dialogCameraCalibration)
        self.labelImages.setGeometry(QtCore.QRect(10, 130, 221, 21))
        self.labelImages.setObjectName(_fromUtf8("labelImages"))
        self.listImages = QtGui.QListWidget(dialogCameraCalibration)
        self.listImages.setGeometry(QtCore.QRect(10, 150, 391, 181))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.listImages.setFont(font)
        self.listImages.setObjectName(_fromUtf8("listImages"))
        self.label1 = QtGui.QLabel(dialogCameraCalibration)
        self.label1.setGeometry(QtCore.QRect(11, 472, 391, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.label2 = QtGui.QLabel(dialogCameraCalibration)
        self.label2.setGeometry(QtCore.QRect(11, 506, 141, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.label3 = QtGui.QLabel(dialogCameraCalibration)
        self.label3.setGeometry(QtCore.QRect(11, 540, 141, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.label4 = QtGui.QLabel(dialogCameraCalibration)
        self.label4.setGeometry(QtCore.QRect(11, 574, 141, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label4.setFont(font)
        self.label4.setObjectName(_fromUtf8("label4"))
        self.spinWidth = QtGui.QSpinBox(dialogCameraCalibration)
        self.spinWidth.setGeometry(QtCore.QRect(160, 507, 41, 26))
        self.spinWidth.setMinimum(1)
        self.spinWidth.setMaximum(20)
        self.spinWidth.setProperty("value", 9)
        self.spinWidth.setObjectName(_fromUtf8("spinWidth"))
        self.spinHeight = QtGui.QSpinBox(dialogCameraCalibration)
        self.spinHeight.setGeometry(QtCore.QRect(160, 541, 41, 26))
        self.spinHeight.setMinimum(1)
        self.spinHeight.setMaximum(20)
        self.spinHeight.setProperty("value", 7)
        self.spinHeight.setObjectName(_fromUtf8("spinHeight"))
        self.spinRatio = QtGui.QSpinBox(dialogCameraCalibration)
        self.spinRatio.setGeometry(QtCore.QRect(160, 575, 41, 26))
        self.spinRatio.setMinimum(1)
        self.spinRatio.setMaximum(4)
        self.spinRatio.setProperty("value", 2)
        self.spinRatio.setObjectName(_fromUtf8("spinRatio"))
        self.lineCalibrationFolder = QtGui.QLineEdit(dialogCameraCalibration)
        self.lineCalibrationFolder.setGeometry(QtCore.QRect(10, 100, 291, 26))
        self.lineCalibrationFolder.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineCalibrationFolder.setReadOnly(True)
        self.lineCalibrationFolder.setObjectName(_fromUtf8("lineCalibrationFolder"))
        self.checkSaveC = QtGui.QCheckBox(dialogCameraCalibration)
        self.checkSaveC.setGeometry(QtCore.QRect(210, 506, 191, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkSaveC.setFont(font)
        self.checkSaveC.setObjectName(_fromUtf8("checkSaveC"))
        self.checkApply = QtGui.QCheckBox(dialogCameraCalibration)
        self.checkApply.setGeometry(QtCore.QRect(210, 574, 191, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkApply.setFont(font)
        self.checkApply.setObjectName(_fromUtf8("checkApply"))
        self.checkSaveU = QtGui.QCheckBox(dialogCameraCalibration)
        self.checkSaveU.setGeometry(QtCore.QRect(210, 540, 191, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkSaveU.setFont(font)
        self.checkSaveU.setObjectName(_fromUtf8("checkSaveU"))
        self.buttonResults = QtGui.QPushButton(dialogCameraCalibration)
        self.buttonResults.setGeometry(QtCore.QRect(110, 608, 91, 28))
        self.buttonResults.setObjectName(_fromUtf8("buttonResults"))
        self.buttonBrowseHI = QtGui.QPushButton(dialogCameraCalibration)
        self.buttonBrowseHI.setGeometry(QtCore.QRect(310, 335, 91, 28))
        self.buttonBrowseHI.setObjectName(_fromUtf8("buttonBrowseHI"))
        self.lineHomographyImage = QtGui.QLineEdit(dialogCameraCalibration)
        self.lineHomographyImage.setGeometry(QtCore.QRect(100, 336, 201, 26))
        self.lineHomographyImage.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineHomographyImage.setReadOnly(True)
        self.lineHomographyImage.setObjectName(_fromUtf8("lineHomographyImage"))
        self.label5 = QtGui.QLabel(dialogCameraCalibration)
        self.label5.setGeometry(QtCore.QRect(10, 336, 91, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label5.setFont(font)
        self.label5.setObjectName(_fromUtf8("label5"))
        self.label6 = QtGui.QLabel(dialogCameraCalibration)
        self.label6.setGeometry(QtCore.QRect(10, 370, 91, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label6.setFont(font)
        self.label6.setObjectName(_fromUtf8("label6"))
        self.lineTestImage = QtGui.QLineEdit(dialogCameraCalibration)
        self.lineTestImage.setGeometry(QtCore.QRect(100, 370, 201, 26))
        self.lineTestImage.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineTestImage.setReadOnly(True)
        self.lineTestImage.setObjectName(_fromUtf8("lineTestImage"))
        self.buttonBrowseTI = QtGui.QPushButton(dialogCameraCalibration)
        self.buttonBrowseTI.setGeometry(QtCore.QRect(310, 369, 91, 28))
        self.buttonBrowseTI.setObjectName(_fromUtf8("buttonBrowseTI"))
        self.buttonSave = QtGui.QPushButton(dialogCameraCalibration)
        self.buttonSave.setEnabled(False)
        self.buttonSave.setGeometry(QtCore.QRect(210, 608, 91, 28))
        self.buttonSave.setObjectName(_fromUtf8("buttonSave"))

        self.retranslateUi(dialogCameraCalibration)
        QtCore.QObject.connect(self.buttonDone, QtCore.SIGNAL(_fromUtf8("clicked()")), dialogCameraCalibration.close)
        QtCore.QMetaObject.connectSlotsByName(dialogCameraCalibration)
        dialogCameraCalibration.setTabOrder(self.buttonBrowseF, self.listImages)
        dialogCameraCalibration.setTabOrder(self.listImages, self.spinWidth)
        dialogCameraCalibration.setTabOrder(self.spinWidth, self.spinHeight)
        dialogCameraCalibration.setTabOrder(self.spinHeight, self.spinRatio)
        dialogCameraCalibration.setTabOrder(self.spinRatio, self.checkSaveC)
        dialogCameraCalibration.setTabOrder(self.checkSaveC, self.checkSaveU)
        dialogCameraCalibration.setTabOrder(self.checkSaveU, self.checkApply)
        dialogCameraCalibration.setTabOrder(self.checkApply, self.buttonStart)
        dialogCameraCalibration.setTabOrder(self.buttonStart, self.buttonResults)
        dialogCameraCalibration.setTabOrder(self.buttonResults, self.buttonDone)

    def retranslateUi(self, dialogCameraCalibration):
        dialogCameraCalibration.setWindowTitle(_translate("dialogCameraCalibration", "Camera Calibration", None))
        self.labelInformation.setText(_translate("dialogCameraCalibration", "To calibrate the camera, please select the folder containing your checkboard images. To determine the most accurate camera parameters, please provide at least 10 images. Calibration images must contain the word \"image_calibration\" in the file name, and will be displayed below.", None))
        self.buttonBrowseF.setText(_translate("dialogCameraCalibration", "Browse...", None))
        self.buttonStart.setText(_translate("dialogCameraCalibration", "Start", None))
        self.buttonDone.setText(_translate("dialogCameraCalibration", "Done", None))
        self.labelStatus.setText(_translate("dialogCameraCalibration", "Waiting to start process.", None))
        self.labelImages.setText(_translate("dialogCameraCalibration", "List of images:", None))
        self.label1.setText(_translate("dialogCameraCalibration", "Calibration Settings", None))
        self.label2.setToolTip(_translate("dialogCameraCalibration", "Sets the number of square corners the width of the chessboard has.", None))
        self.label2.setText(_translate("dialogCameraCalibration", "Chessboard Width", None))
        self.label3.setToolTip(_translate("dialogCameraCalibration", "Sets the number of square corners the height of the chessboard has.", None))
        self.label3.setText(_translate("dialogCameraCalibration", "Chessboard Height", None))
        self.label4.setToolTip(_translate("dialogCameraCalibration", "Sets the downscaling ratio to use to speed up calibration.", None))
        self.label4.setText(_translate("dialogCameraCalibration", "Downscaling Ratio", None))
        self.spinWidth.setToolTip(_translate("dialogCameraCalibration", "1 - 20", None))
        self.spinHeight.setToolTip(_translate("dialogCameraCalibration", "1 - 20", None))
        self.spinRatio.setToolTip(_translate("dialogCameraCalibration", "1 - 4", None))
        self.checkSaveC.setToolTip(_translate("dialogCameraCalibration", "Check to save drawn chessboard corner calibration images to the corners folder.", None))
        self.checkSaveC.setText(_translate("dialogCameraCalibration", "Save Chessboard Images", None))
        self.checkApply.setToolTip(_translate("dialogCameraCalibration", "Check to apply found camera matrix, distortion coefficient and homography matrix processing to the sample image.", None))
        self.checkApply.setText(_translate("dialogCameraCalibration", "Apply to Test Image", None))
        self.checkSaveU.setToolTip(_translate("dialogCameraCalibration", "Check to save undistorted calibration images to the undistorted folder.", None))
        self.checkSaveU.setText(_translate("dialogCameraCalibration", "Save Undistorted Images", None))
        self.buttonResults.setText(_translate("dialogCameraCalibration", "View Results", None))
        self.buttonBrowseHI.setText(_translate("dialogCameraCalibration", "Browse...", None))
        self.label5.setToolTip(_translate("dialogCameraCalibration", "Select the image to be used to calculate the homography image.", None))
        self.label5.setText(_translate("dialogCameraCalibration", "Homography", None))
        self.label6.setToolTip(_translate("dialogCameraCalibration", "Select the image to be used to test the calculated calibration results.", None))
        self.label6.setText(_translate("dialogCameraCalibration", "Test Image", None))
        self.buttonBrowseTI.setText(_translate("dialogCameraCalibration", "Browse...", None))
        self.buttonSave.setText(_translate("dialogCameraCalibration", "Save Results", None))

import icons_rc
