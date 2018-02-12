# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\dialogCameraCalibration.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogCameraCalibration(object):
    def setupUi(self, dialogCameraCalibration):
        dialogCameraCalibration.setObjectName("dialogCameraCalibration")
        dialogCameraCalibration.resize(395, 406)
        self.gridLayout = QtWidgets.QGridLayout(dialogCameraCalibration)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(dialogCameraCalibration)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 4)
        self.labelStatus = QtWidgets.QLabel(dialogCameraCalibration)
        self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatus.setObjectName("labelStatus")
        self.gridLayout.addWidget(self.labelStatus, 6, 0, 1, 4)
        self.pushAdd = QtWidgets.QPushButton(dialogCameraCalibration)
        self.pushAdd.setObjectName("pushAdd")
        self.gridLayout.addWidget(self.pushAdd, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        self.listImages = QtWidgets.QListWidget(dialogCameraCalibration)
        self.listImages.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listImages.setObjectName("listImages")
        self.gridLayout.addWidget(self.listImages, 0, 0, 3, 3)
        self.pushRemove = QtWidgets.QPushButton(dialogCameraCalibration)
        self.pushRemove.setObjectName("pushRemove")
        self.gridLayout.addWidget(self.pushRemove, 1, 3, 1, 1)
        self.frameButtons = QtWidgets.QFrame(dialogCameraCalibration)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameButtons.sizePolicy().hasHeightForWidth())
        self.frameButtons.setSizePolicy(sizePolicy)
        self.frameButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameButtons.setObjectName("frameButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameButtons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushStart = QtWidgets.QPushButton(self.frameButtons)
        self.pushStart.setEnabled(False)
        self.pushStart.setObjectName("pushStart")
        self.horizontalLayout.addWidget(self.pushStart)
        self.pushDone = QtWidgets.QPushButton(self.frameButtons)
        self.pushDone.setObjectName("pushDone")
        self.horizontalLayout.addWidget(self.pushDone)
        self.gridLayout.addWidget(self.frameButtons, 13, 0, 1, 4)
        self.frameImages = QtWidgets.QFrame(dialogCameraCalibration)
        self.frameImages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameImages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameImages.setObjectName("frameImages")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frameImages)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineTestImage = QtWidgets.QLineEdit(self.frameImages)
        self.lineTestImage.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineTestImage.setReadOnly(True)
        self.lineTestImage.setObjectName("lineTestImage")
        self.gridLayout_4.addWidget(self.lineTestImage, 1, 1, 1, 1)
        self.labelTestImage = QtWidgets.QLabel(self.frameImages)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelTestImage.setFont(font)
        self.labelTestImage.setObjectName("labelTestImage")
        self.gridLayout_4.addWidget(self.labelTestImage, 1, 0, 1, 1)
        self.labelHomographyImage = QtWidgets.QLabel(self.frameImages)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelHomographyImage.setFont(font)
        self.labelHomographyImage.setObjectName("labelHomographyImage")
        self.gridLayout_4.addWidget(self.labelHomographyImage, 0, 0, 1, 1)
        self.lineHomographyImage = QtWidgets.QLineEdit(self.frameImages)
        self.lineHomographyImage.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineHomographyImage.setReadOnly(True)
        self.lineHomographyImage.setObjectName("lineHomographyImage")
        self.gridLayout_4.addWidget(self.lineHomographyImage, 0, 1, 1, 1)
        self.pushBrowseHI = QtWidgets.QPushButton(self.frameImages)
        self.pushBrowseHI.setObjectName("pushBrowseHI")
        self.gridLayout_4.addWidget(self.pushBrowseHI, 0, 2, 1, 1)
        self.pushBrowseTI = QtWidgets.QPushButton(self.frameImages)
        self.pushBrowseTI.setObjectName("pushBrowseTI")
        self.gridLayout_4.addWidget(self.pushBrowseTI, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.frameImages, 3, 0, 2, 4)
        self.groupCalibrationSettings = QtWidgets.QGroupBox(dialogCameraCalibration)
        self.groupCalibrationSettings.setObjectName("groupCalibrationSettings")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupCalibrationSettings)
        self.gridLayout_3.setContentsMargins(-1, 3, -1, 6)
        self.gridLayout_3.setVerticalSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelWidth = QtWidgets.QLabel(self.groupCalibrationSettings)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelWidth.setFont(font)
        self.labelWidth.setObjectName("labelWidth")
        self.gridLayout_3.addWidget(self.labelWidth, 1, 0, 1, 1)
        self.labelHeight = QtWidgets.QLabel(self.groupCalibrationSettings)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelHeight.setFont(font)
        self.labelHeight.setObjectName("labelHeight")
        self.gridLayout_3.addWidget(self.labelHeight, 2, 0, 1, 1)
        self.checkSaveU = QtWidgets.QCheckBox(self.groupCalibrationSettings)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkSaveU.setFont(font)
        self.checkSaveU.setObjectName("checkSaveU")
        self.gridLayout_3.addWidget(self.checkSaveU, 5, 0, 1, 3)
        self.checkApply = QtWidgets.QCheckBox(self.groupCalibrationSettings)
        self.checkApply.setObjectName("checkApply")
        self.gridLayout_3.addWidget(self.checkApply, 7, 0, 1, 4)
        self.spinWidth = QtWidgets.QSpinBox(self.groupCalibrationSettings)
        self.spinWidth.setMinimum(1)
        self.spinWidth.setMaximum(20)
        self.spinWidth.setObjectName("spinWidth")
        self.gridLayout_3.addWidget(self.spinWidth, 1, 1, 1, 1)
        self.checkSaveC = QtWidgets.QCheckBox(self.groupCalibrationSettings)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkSaveC.setFont(font)
        self.checkSaveC.setObjectName("checkSaveC")
        self.gridLayout_3.addWidget(self.checkSaveC, 4, 0, 1, 3)
        self.spinHeight = QtWidgets.QSpinBox(self.groupCalibrationSettings)
        self.spinHeight.setMinimum(1)
        self.spinHeight.setMaximum(20)
        self.spinHeight.setObjectName("spinHeight")
        self.gridLayout_3.addWidget(self.spinHeight, 2, 1, 1, 1)
        self.spinHeightHI = QtWidgets.QSpinBox(self.groupCalibrationSettings)
        self.spinHeightHI.setMinimum(1)
        self.spinHeightHI.setMaximum(20)
        self.spinHeightHI.setObjectName("spinHeightHI")
        self.gridLayout_3.addWidget(self.spinHeightHI, 2, 2, 1, 1)
        self.labelHeightHI = QtWidgets.QLabel(self.groupCalibrationSettings)
        self.labelHeightHI.setObjectName("labelHeightHI")
        self.gridLayout_3.addWidget(self.labelHeightHI, 0, 2, 1, 1)
        self.labelWidthHI = QtWidgets.QLabel(self.groupCalibrationSettings)
        self.labelWidthHI.setObjectName("labelWidthHI")
        self.gridLayout_3.addWidget(self.labelWidthHI, 0, 1, 1, 1)
        self.spinWidthHI = QtWidgets.QSpinBox(self.groupCalibrationSettings)
        self.spinWidthHI.setMinimum(1)
        self.spinWidthHI.setMaximum(20)
        self.spinWidthHI.setObjectName("spinWidthHI")
        self.gridLayout_3.addWidget(self.spinWidthHI, 1, 2, 1, 1)
        self.spinRatio = QtWidgets.QSpinBox(self.groupCalibrationSettings)
        self.spinRatio.setMinimum(1)
        self.spinRatio.setMaximum(4)
        self.spinRatio.setObjectName("spinRatio")
        self.gridLayout_3.addWidget(self.spinRatio, 3, 2, 1, 1)
        self.labelRatio = QtWidgets.QLabel(self.groupCalibrationSettings)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelRatio.setFont(font)
        self.labelRatio.setObjectName("labelRatio")
        self.gridLayout_3.addWidget(self.labelRatio, 3, 0, 1, 2)
        self.gridLayout.addWidget(self.groupCalibrationSettings, 9, 0, 4, 1)
        self.pushViewResults = QtWidgets.QPushButton(dialogCameraCalibration)
        self.pushViewResults.setObjectName("pushViewResults")
        self.gridLayout.addWidget(self.pushViewResults, 11, 1, 1, 3)
        self.groupCropSettings = QtWidgets.QGroupBox(dialogCameraCalibration)
        self.groupCropSettings.setObjectName("groupCropSettings")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupCropSettings)
        self.gridLayout_2.setContentsMargins(-1, 3, -1, 6)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelXCrop = QtWidgets.QLabel(self.groupCropSettings)
        self.labelXCrop.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXCrop.setObjectName("labelXCrop")
        self.gridLayout_2.addWidget(self.labelXCrop, 0, 1, 1, 1)
        self.labelResolution = QtWidgets.QLabel(self.groupCropSettings)
        self.labelResolution.setObjectName("labelResolution")
        self.gridLayout_2.addWidget(self.labelResolution, 2, 0, 1, 1)
        self.labelTL = QtWidgets.QLabel(self.groupCropSettings)
        self.labelTL.setObjectName("labelTL")
        self.gridLayout_2.addWidget(self.labelTL, 1, 0, 1, 1)
        self.spinTLX = QtWidgets.QSpinBox(self.groupCropSettings)
        self.spinTLX.setMaximum(9999)
        self.spinTLX.setObjectName("spinTLX")
        self.gridLayout_2.addWidget(self.spinTLX, 1, 1, 1, 1)
        self.labelYCrop = QtWidgets.QLabel(self.groupCropSettings)
        self.labelYCrop.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYCrop.setObjectName("labelYCrop")
        self.gridLayout_2.addWidget(self.labelYCrop, 0, 2, 1, 1)
        self.spinTLY = QtWidgets.QSpinBox(self.groupCropSettings)
        self.spinTLY.setMaximum(9999)
        self.spinTLY.setObjectName("spinTLY")
        self.gridLayout_2.addWidget(self.spinTLY, 1, 2, 1, 1)
        self.spinResolutionY = QtWidgets.QSpinBox(self.groupCropSettings)
        self.spinResolutionY.setMaximum(9999)
        self.spinResolutionY.setObjectName("spinResolutionY")
        self.gridLayout_2.addWidget(self.spinResolutionY, 2, 2, 1, 1)
        self.spinResolutionX = QtWidgets.QSpinBox(self.groupCropSettings)
        self.spinResolutionX.setMaximum(9999)
        self.spinResolutionX.setObjectName("spinResolutionX")
        self.gridLayout_2.addWidget(self.spinResolutionX, 2, 1, 1, 1)
        self.labelTLpx = QtWidgets.QLabel(self.groupCropSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTLpx.sizePolicy().hasHeightForWidth())
        self.labelTLpx.setSizePolicy(sizePolicy)
        self.labelTLpx.setObjectName("labelTLpx")
        self.gridLayout_2.addWidget(self.labelTLpx, 1, 3, 1, 1)
        self.labelRespx = QtWidgets.QLabel(self.groupCropSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRespx.sizePolicy().hasHeightForWidth())
        self.labelRespx.setSizePolicy(sizePolicy)
        self.labelRespx.setObjectName("labelRespx")
        self.gridLayout_2.addWidget(self.labelRespx, 2, 3, 1, 1)
        self.pushCropImage = QtWidgets.QPushButton(self.groupCropSettings)
        self.pushCropImage.setEnabled(False)
        self.pushCropImage.setObjectName("pushCropImage")
        self.gridLayout_2.addWidget(self.pushCropImage, 3, 0, 1, 4)
        self.gridLayout.addWidget(self.groupCropSettings, 9, 1, 2, 3)
        self.pushSaveResults = QtWidgets.QPushButton(dialogCameraCalibration)
        self.pushSaveResults.setEnabled(False)
        self.pushSaveResults.setObjectName("pushSaveResults")
        self.gridLayout.addWidget(self.pushSaveResults, 12, 1, 1, 3)

        self.retranslateUi(dialogCameraCalibration)
        self.pushDone.clicked.connect(dialogCameraCalibration.close)
        QtCore.QMetaObject.connectSlotsByName(dialogCameraCalibration)
        dialogCameraCalibration.setTabOrder(self.listImages, self.pushAdd)
        dialogCameraCalibration.setTabOrder(self.pushAdd, self.pushRemove)
        dialogCameraCalibration.setTabOrder(self.pushRemove, self.pushDone)

    def retranslateUi(self, dialogCameraCalibration):
        _translate = QtCore.QCoreApplication.translate
        dialogCameraCalibration.setWindowTitle(_translate("dialogCameraCalibration", "Camera Calibration"))
        self.labelStatus.setText(_translate("dialogCameraCalibration", "Add calibration images."))
        self.pushAdd.setText(_translate("dialogCameraCalibration", "Add..."))
        self.listImages.setToolTip(_translate("dialogCameraCalibration", "List of calibration images found in the above folder."))
        self.pushRemove.setText(_translate("dialogCameraCalibration", "Remove"))
        self.pushStart.setText(_translate("dialogCameraCalibration", "Start"))
        self.pushDone.setText(_translate("dialogCameraCalibration", "Done"))
        self.lineTestImage.setToolTip(_translate("dialogCameraCalibration", "Image used to test the calculated calibration results."))
        self.labelTestImage.setToolTip(_translate("dialogCameraCalibration", "Image used to test the calculated calibration results."))
        self.labelTestImage.setText(_translate("dialogCameraCalibration", "Test Image"))
        self.labelHomographyImage.setToolTip(_translate("dialogCameraCalibration", "Image used to calculate the homography matrix."))
        self.labelHomographyImage.setText(_translate("dialogCameraCalibration", "Homography"))
        self.lineHomographyImage.setToolTip(_translate("dialogCameraCalibration", "Image used to calculate the homography matrix."))
        self.pushBrowseHI.setText(_translate("dialogCameraCalibration", "Browse..."))
        self.pushBrowseTI.setText(_translate("dialogCameraCalibration", "Browse..."))
        self.groupCalibrationSettings.setTitle(_translate("dialogCameraCalibration", "Calibration Settings"))
        self.labelWidth.setToolTip(_translate("dialogCameraCalibration", "Number of square corners along the width of the chessboard."))
        self.labelWidth.setText(_translate("dialogCameraCalibration", "Chessboard"))
        self.labelHeight.setToolTip(_translate("dialogCameraCalibration", "Number of square corners along the height of the chessboard."))
        self.labelHeight.setText(_translate("dialogCameraCalibration", "Homography"))
        self.checkSaveU.setToolTip(_translate("dialogCameraCalibration", "Undistorted calibration images will be saved to the original image\'s root folder."))
        self.checkSaveU.setText(_translate("dialogCameraCalibration", "Save Undistorted Images"))
        self.checkApply.setToolTip(_translate("dialogCameraCalibration", "The calculated calibration results will be applied on the selected test image."))
        self.checkApply.setText(_translate("dialogCameraCalibration", "Apply to Test Image"))
        self.spinWidth.setToolTip(_translate("dialogCameraCalibration", "1 - 20"))
        self.checkSaveC.setToolTip(_translate("dialogCameraCalibration", "Drawn chessboard corner calibration images will be saved to the original image\'s root folder."))
        self.checkSaveC.setText(_translate("dialogCameraCalibration", "Save Chessboard Images"))
        self.spinHeight.setToolTip(_translate("dialogCameraCalibration", "1 - 20"))
        self.spinHeightHI.setToolTip(_translate("dialogCameraCalibration", "1 - 20"))
        self.labelHeightHI.setToolTip(_translate("dialogCameraCalibration", "Number of square corners along the height of the chessboard in the homography image."))
        self.labelHeightHI.setText(_translate("dialogCameraCalibration", "Height"))
        self.labelWidthHI.setToolTip(_translate("dialogCameraCalibration", "Number of square corners along the width of the chessboard in the homography image."))
        self.labelWidthHI.setText(_translate("dialogCameraCalibration", "Width"))
        self.spinWidthHI.setToolTip(_translate("dialogCameraCalibration", "1 - 20"))
        self.spinRatio.setToolTip(_translate("dialogCameraCalibration", "1 - 4"))
        self.labelRatio.setToolTip(_translate("dialogCameraCalibration", "Ratio used to downscale the images in order to speed up calibration time at the cost of accuracy."))
        self.labelRatio.setText(_translate("dialogCameraCalibration", "Downscaling Ratio"))
        self.pushViewResults.setText(_translate("dialogCameraCalibration", "View Results"))
        self.groupCropSettings.setTitle(_translate("dialogCameraCalibration", "Crop Settings"))
        self.labelXCrop.setText(_translate("dialogCameraCalibration", "X"))
        self.labelResolution.setText(_translate("dialogCameraCalibration", "Resolution"))
        self.labelTL.setText(_translate("dialogCameraCalibration", "Top Left"))
        self.labelYCrop.setText(_translate("dialogCameraCalibration", "Y"))
        self.labelTLpx.setText(_translate("dialogCameraCalibration", "px"))
        self.labelRespx.setText(_translate("dialogCameraCalibration", "px"))
        self.pushCropImage.setText(_translate("dialogCameraCalibration", "Crop Test Image"))
        self.pushSaveResults.setText(_translate("dialogCameraCalibration", "Save Results"))

