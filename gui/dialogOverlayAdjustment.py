# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\dialogOverlayAdjustment.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogOverlayAdjustment(object):
    def setupUi(self, dialogOverlayAdjustment):
        dialogOverlayAdjustment.setObjectName("dialogOverlayAdjustment")
        dialogOverlayAdjustment.resize(358, 290)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogOverlayAdjustment.setWindowIcon(icon)
        self.gridLayout_3 = QtWidgets.QGridLayout(dialogOverlayAdjustment)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupRotationFlip = QtWidgets.QGroupBox(dialogOverlayAdjustment)
        self.groupRotationFlip.setObjectName("groupRotationFlip")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupRotationFlip)
        self.horizontalLayout.setContentsMargins(5, 3, 5, 3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushRotateACW = QtWidgets.QPushButton(self.groupRotationFlip)
        self.pushRotateACW.setMinimumSize(QtCore.QSize(34, 34))
        self.pushRotateACW.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushRotateACW.setFont(font)
        self.pushRotateACW.setObjectName("pushRotateACW")
        self.horizontalLayout.addWidget(self.pushRotateACW)
        self.pushRotateCW = QtWidgets.QPushButton(self.groupRotationFlip)
        self.pushRotateCW.setMinimumSize(QtCore.QSize(34, 34))
        self.pushRotateCW.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushRotateCW.setFont(font)
        self.pushRotateCW.setObjectName("pushRotateCW")
        self.horizontalLayout.addWidget(self.pushRotateCW)
        self.pushFlipHorizontal = QtWidgets.QPushButton(self.groupRotationFlip)
        self.pushFlipHorizontal.setMinimumSize(QtCore.QSize(34, 34))
        self.pushFlipHorizontal.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushFlipHorizontal.setFont(font)
        self.pushFlipHorizontal.setObjectName("pushFlipHorizontal")
        self.horizontalLayout.addWidget(self.pushFlipHorizontal)
        self.pushFlipVertical = QtWidgets.QPushButton(self.groupRotationFlip)
        self.pushFlipVertical.setMinimumSize(QtCore.QSize(34, 34))
        self.pushFlipVertical.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushFlipVertical.setFont(font)
        self.pushFlipVertical.setObjectName("pushFlipVertical")
        self.horizontalLayout.addWidget(self.pushFlipVertical)
        self.gridLayout_3.addWidget(self.groupRotationFlip, 2, 2, 1, 2)
        self.groupValues = QtWidgets.QGroupBox(dialogOverlayAdjustment)
        self.groupValues.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupValues.setFont(font)
        self.groupValues.setObjectName("groupValues")
        self.gridLayout = QtWidgets.QGridLayout(self.groupValues)
        self.gridLayout.setContentsMargins(10, 7, 10, 7)
        self.gridLayout.setObjectName("gridLayout")
        self.labelPixels = QtWidgets.QLabel(self.groupValues)
        self.labelPixels.setObjectName("labelPixels")
        self.gridLayout.addWidget(self.labelPixels, 0, 0, 1, 1)
        self.spinPixels = QtWidgets.QSpinBox(self.groupValues)
        self.spinPixels.setMinimum(1)
        self.spinPixels.setMaximum(5000)
        self.spinPixels.setObjectName("spinPixels")
        self.gridLayout.addWidget(self.spinPixels, 0, 1, 1, 1)
        self.spinDegrees = QtWidgets.QDoubleSpinBox(self.groupValues)
        self.spinDegrees.setMinimum(0.0)
        self.spinDegrees.setMaximum(360.0)
        self.spinDegrees.setProperty("value", 1.0)
        self.spinDegrees.setObjectName("spinDegrees")
        self.gridLayout.addWidget(self.spinDegrees, 1, 1, 1, 1)
        self.labelDegrees = QtWidgets.QLabel(self.groupValues)
        self.labelDegrees.setObjectName("labelDegrees")
        self.gridLayout.addWidget(self.labelDegrees, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupValues, 0, 0, 1, 1)
        self.groupTranslation = QtWidgets.QGroupBox(dialogOverlayAdjustment)
        self.groupTranslation.setObjectName("groupTranslation")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupTranslation)
        self.gridLayout_2.setContentsMargins(5, 3, 5, 3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushTranslateUp = QtWidgets.QPushButton(self.groupTranslation)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushTranslateUp.setFont(font)
        self.pushTranslateUp.setObjectName("pushTranslateUp")
        self.gridLayout_2.addWidget(self.pushTranslateUp, 0, 0, 1, 1)
        self.pushTranslateDown = QtWidgets.QPushButton(self.groupTranslation)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushTranslateDown.setFont(font)
        self.pushTranslateDown.setObjectName("pushTranslateDown")
        self.gridLayout_2.addWidget(self.pushTranslateDown, 1, 0, 1, 1)
        self.pushTranslateLeft = QtWidgets.QPushButton(self.groupTranslation)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushTranslateLeft.setFont(font)
        self.pushTranslateLeft.setObjectName("pushTranslateLeft")
        self.gridLayout_2.addWidget(self.pushTranslateLeft, 2, 0, 1, 1)
        self.pushTranslateRight = QtWidgets.QPushButton(self.groupTranslation)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushTranslateRight.setFont(font)
        self.pushTranslateRight.setObjectName("pushTranslateRight")
        self.gridLayout_2.addWidget(self.pushTranslateRight, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupTranslation, 0, 3, 2, 1)
        self.groupGeneral = QtWidgets.QGroupBox(dialogOverlayAdjustment)
        self.groupGeneral.setObjectName("groupGeneral")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupGeneral)
        self.gridLayout_5.setContentsMargins(5, 3, 5, 3)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushReset = QtWidgets.QPushButton(self.groupGeneral)
        self.pushReset.setEnabled(True)
        self.pushReset.setMinimumSize(QtCore.QSize(34, 34))
        self.pushReset.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushReset.setFont(font)
        self.pushReset.setObjectName("pushReset")
        self.gridLayout_5.addWidget(self.pushReset, 0, 0, 1, 1)
        self.pushUndo = QtWidgets.QPushButton(self.groupGeneral)
        self.pushUndo.setMinimumSize(QtCore.QSize(34, 34))
        self.pushUndo.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushUndo.setFont(font)
        self.pushUndo.setCheckable(True)
        self.pushUndo.setObjectName("pushUndo")
        self.gridLayout_5.addWidget(self.pushUndo, 0, 1, 1, 1)
        self.pushSave = QtWidgets.QPushButton(self.groupGeneral)
        self.pushSave.setMinimumSize(QtCore.QSize(34, 34))
        self.pushSave.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushSave.setFont(font)
        self.pushSave.setObjectName("pushSave")
        self.gridLayout_5.addWidget(self.pushSave, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupGeneral, 0, 1, 1, 2)
        self.groupStretchPull = QtWidgets.QGroupBox(dialogOverlayAdjustment)
        self.groupStretchPull.setObjectName("groupStretchPull")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupStretchPull)
        self.gridLayout_4.setContentsMargins(5, 3, 5, 3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushStretchLeftUp = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchLeftUp.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchLeftUp.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchLeftUp.setFont(font)
        self.pushStretchLeftUp.setCheckable(True)
        self.pushStretchLeftUp.setObjectName("pushStretchLeftUp")
        self.gridLayout_4.addWidget(self.pushStretchLeftUp, 0, 1, 1, 1)
        self.pushStretchRightUp = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchRightUp.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchRightUp.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchRightUp.setFont(font)
        self.pushStretchRightUp.setCheckable(True)
        self.pushStretchRightUp.setObjectName("pushStretchRightUp")
        self.gridLayout_4.addWidget(self.pushStretchRightUp, 0, 3, 1, 1)
        self.pushStretchUpLeft = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchUpLeft.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchUpLeft.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchUpLeft.setFont(font)
        self.pushStretchUpLeft.setCheckable(True)
        self.pushStretchUpLeft.setObjectName("pushStretchUpLeft")
        self.gridLayout_4.addWidget(self.pushStretchUpLeft, 1, 0, 1, 1)
        self.pushStretchNW = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchNW.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchNW.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchNW.setFont(font)
        self.pushStretchNW.setCheckable(True)
        self.pushStretchNW.setObjectName("pushStretchNW")
        self.gridLayout_4.addWidget(self.pushStretchNW, 1, 1, 1, 1)
        self.pushStretchN = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchN.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchN.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchN.setFont(font)
        self.pushStretchN.setCheckable(True)
        self.pushStretchN.setObjectName("pushStretchN")
        self.gridLayout_4.addWidget(self.pushStretchN, 1, 2, 1, 1)
        self.pushStretchNE = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchNE.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchNE.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchNE.setFont(font)
        self.pushStretchNE.setCheckable(True)
        self.pushStretchNE.setObjectName("pushStretchNE")
        self.gridLayout_4.addWidget(self.pushStretchNE, 1, 3, 1, 1)
        self.pushStretchUpRight = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchUpRight.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchUpRight.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchUpRight.setFont(font)
        self.pushStretchUpRight.setCheckable(True)
        self.pushStretchUpRight.setObjectName("pushStretchUpRight")
        self.gridLayout_4.addWidget(self.pushStretchUpRight, 1, 4, 1, 1)
        self.pushStretchW = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchW.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchW.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchW.setFont(font)
        self.pushStretchW.setCheckable(True)
        self.pushStretchW.setObjectName("pushStretchW")
        self.gridLayout_4.addWidget(self.pushStretchW, 2, 1, 1, 1)
        self.pushResetStretch = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushResetStretch.setMinimumSize(QtCore.QSize(34, 34))
        self.pushResetStretch.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushResetStretch.setFont(font)
        self.pushResetStretch.setCheckable(True)
        self.pushResetStretch.setObjectName("pushResetStretch")
        self.gridLayout_4.addWidget(self.pushResetStretch, 2, 2, 1, 1)
        self.pushStretchE = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchE.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchE.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchE.setFont(font)
        self.pushStretchE.setCheckable(True)
        self.pushStretchE.setObjectName("pushStretchE")
        self.gridLayout_4.addWidget(self.pushStretchE, 2, 3, 1, 1)
        self.pushStretchDownLeft = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchDownLeft.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchDownLeft.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchDownLeft.setFont(font)
        self.pushStretchDownLeft.setCheckable(True)
        self.pushStretchDownLeft.setObjectName("pushStretchDownLeft")
        self.gridLayout_4.addWidget(self.pushStretchDownLeft, 3, 0, 1, 1)
        self.pushStretchSW = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchSW.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchSW.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchSW.setFont(font)
        self.pushStretchSW.setCheckable(True)
        self.pushStretchSW.setObjectName("pushStretchSW")
        self.gridLayout_4.addWidget(self.pushStretchSW, 3, 1, 1, 1)
        self.pushStretchS = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchS.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchS.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchS.setFont(font)
        self.pushStretchS.setCheckable(True)
        self.pushStretchS.setObjectName("pushStretchS")
        self.gridLayout_4.addWidget(self.pushStretchS, 3, 2, 1, 1)
        self.pushStretchSE = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchSE.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchSE.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchSE.setFont(font)
        self.pushStretchSE.setCheckable(True)
        self.pushStretchSE.setObjectName("pushStretchSE")
        self.gridLayout_4.addWidget(self.pushStretchSE, 3, 3, 1, 1)
        self.pushStretchDownRight = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchDownRight.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchDownRight.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchDownRight.setFont(font)
        self.pushStretchDownRight.setCheckable(True)
        self.pushStretchDownRight.setObjectName("pushStretchDownRight")
        self.gridLayout_4.addWidget(self.pushStretchDownRight, 3, 4, 1, 1)
        self.pushStretchLeftDown = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchLeftDown.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchLeftDown.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchLeftDown.setFont(font)
        self.pushStretchLeftDown.setCheckable(True)
        self.pushStretchLeftDown.setObjectName("pushStretchLeftDown")
        self.gridLayout_4.addWidget(self.pushStretchLeftDown, 4, 1, 1, 1)
        self.pushStretchRightDown = QtWidgets.QPushButton(self.groupStretchPull)
        self.pushStretchRightDown.setMinimumSize(QtCore.QSize(34, 34))
        self.pushStretchRightDown.setMaximumSize(QtCore.QSize(34, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushStretchRightDown.setFont(font)
        self.pushStretchRightDown.setCheckable(True)
        self.pushStretchRightDown.setObjectName("pushStretchRightDown")
        self.gridLayout_4.addWidget(self.pushStretchRightDown, 4, 3, 1, 1)
        self.gridLayout_3.addWidget(self.groupStretchPull, 1, 0, 3, 2)
        self.pushDone = QtWidgets.QPushButton(dialogOverlayAdjustment)
        self.pushDone.setObjectName("pushDone")
        self.gridLayout_3.addWidget(self.pushDone, 3, 2, 1, 2)

        self.retranslateUi(dialogOverlayAdjustment)
        self.pushDone.clicked.connect(dialogOverlayAdjustment.close)
        QtCore.QMetaObject.connectSlotsByName(dialogOverlayAdjustment)
        dialogOverlayAdjustment.setTabOrder(self.pushDone, self.spinPixels)
        dialogOverlayAdjustment.setTabOrder(self.spinPixels, self.spinDegrees)
        dialogOverlayAdjustment.setTabOrder(self.spinDegrees, self.pushReset)
        dialogOverlayAdjustment.setTabOrder(self.pushReset, self.pushUndo)
        dialogOverlayAdjustment.setTabOrder(self.pushUndo, self.pushSave)
        dialogOverlayAdjustment.setTabOrder(self.pushSave, self.pushTranslateUp)
        dialogOverlayAdjustment.setTabOrder(self.pushTranslateUp, self.pushTranslateDown)
        dialogOverlayAdjustment.setTabOrder(self.pushTranslateDown, self.pushTranslateLeft)
        dialogOverlayAdjustment.setTabOrder(self.pushTranslateLeft, self.pushTranslateRight)
        dialogOverlayAdjustment.setTabOrder(self.pushTranslateRight, self.pushStretchLeftUp)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchLeftUp, self.pushStretchRightUp)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchRightUp, self.pushStretchUpLeft)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchUpLeft, self.pushStretchNW)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchNW, self.pushStretchN)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchN, self.pushStretchNE)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchNE, self.pushStretchUpRight)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchUpRight, self.pushStretchW)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchW, self.pushResetStretch)
        dialogOverlayAdjustment.setTabOrder(self.pushResetStretch, self.pushStretchE)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchE, self.pushStretchDownLeft)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchDownLeft, self.pushStretchSW)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchSW, self.pushStretchS)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchS, self.pushStretchSE)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchSE, self.pushStretchDownRight)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchDownRight, self.pushStretchLeftDown)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchLeftDown, self.pushStretchRightDown)
        dialogOverlayAdjustment.setTabOrder(self.pushStretchRightDown, self.pushRotateACW)
        dialogOverlayAdjustment.setTabOrder(self.pushRotateACW, self.pushRotateCW)
        dialogOverlayAdjustment.setTabOrder(self.pushRotateCW, self.pushFlipHorizontal)
        dialogOverlayAdjustment.setTabOrder(self.pushFlipHorizontal, self.pushFlipVertical)

    def retranslateUi(self, dialogOverlayAdjustment):
        _translate = QtCore.QCoreApplication.translate
        dialogOverlayAdjustment.setWindowTitle(_translate("dialogOverlayAdjustment", "Overlay Adjustment"))
        self.groupRotationFlip.setTitle(_translate("dialogOverlayAdjustment", "Rotation / Flip"))
        self.pushRotateACW.setToolTip(_translate("dialogOverlayAdjustment", "Rotates the overlay anti-clockwise by the entered degrees."))
        self.pushRotateACW.setText(_translate("dialogOverlayAdjustment", "ACW"))
        self.pushRotateCW.setToolTip(_translate("dialogOverlayAdjustment", "Rotates the overlay clockwise by the entered degrees."))
        self.pushRotateCW.setText(_translate("dialogOverlayAdjustment", "CW"))
        self.pushFlipHorizontal.setToolTip(_translate("dialogOverlayAdjustment", "Flips the overlay along the horizontal axis."))
        self.pushFlipHorizontal.setText(_translate("dialogOverlayAdjustment", "H"))
        self.pushFlipVertical.setToolTip(_translate("dialogOverlayAdjustment", "Flips the overlay along the vertical axis."))
        self.pushFlipVertical.setText(_translate("dialogOverlayAdjustment", "V"))
        self.groupValues.setTitle(_translate("dialogOverlayAdjustment", "Values"))
        self.labelPixels.setText(_translate("dialogOverlayAdjustment", "Pixels"))
        self.labelDegrees.setText(_translate("dialogOverlayAdjustment", "Degrees"))
        self.groupTranslation.setTitle(_translate("dialogOverlayAdjustment", "Translation"))
        self.pushTranslateUp.setToolTip(_translate("dialogOverlayAdjustment", "Shifts the overlay up by the entered pixels."))
        self.pushTranslateUp.setText(_translate("dialogOverlayAdjustment", "UP"))
        self.pushTranslateDown.setToolTip(_translate("dialogOverlayAdjustment", "Shifts the overlay down by the entered pixels."))
        self.pushTranslateDown.setText(_translate("dialogOverlayAdjustment", "DOWN"))
        self.pushTranslateLeft.setToolTip(_translate("dialogOverlayAdjustment", "Shifts the overlay left by the entered pixels."))
        self.pushTranslateLeft.setText(_translate("dialogOverlayAdjustment", "LEFT"))
        self.pushTranslateRight.setToolTip(_translate("dialogOverlayAdjustment", "Shifts the overlay right by the entered pixels."))
        self.pushTranslateRight.setText(_translate("dialogOverlayAdjustment", "RIGHT"))
        self.groupGeneral.setTitle(_translate("dialogOverlayAdjustment", "General"))
        self.pushReset.setToolTip(_translate("dialogOverlayAdjustment", "Resets the overlay."))
        self.pushReset.setText(_translate("dialogOverlayAdjustment", "RE"))
        self.pushUndo.setToolTip(_translate("dialogOverlayAdjustment", "Undoes the most recent action."))
        self.pushUndo.setText(_translate("dialogOverlayAdjustment", "UN"))
        self.pushSave.setToolTip(_translate("dialogOverlayAdjustment", "Saves the current adjustment parameters to be used for part contour drawing."))
        self.pushSave.setText(_translate("dialogOverlayAdjustment", "SA"))
        self.groupStretchPull.setTitle(_translate("dialogOverlayAdjustment", "Stretch / Pull"))
        self.pushStretchLeftUp.setToolTip(_translate("dialogOverlayAdjustment", "Pulls the overlay up from the left by the entered pixels."))
        self.pushStretchLeftUp.setText(_translate("dialogOverlayAdjustment", "LU"))
        self.pushStretchRightUp.setToolTip(_translate("dialogOverlayAdjustment", "Pulls the overlay up from the right by the entered pixels."))
        self.pushStretchRightUp.setText(_translate("dialogOverlayAdjustment", "RU"))
        self.pushStretchUpLeft.setToolTip(_translate("dialogOverlayAdjustment", "Pulls the overlay left from the top by the entered pixels."))
        self.pushStretchUpLeft.setText(_translate("dialogOverlayAdjustment", "UL"))
        self.pushStretchNW.setToolTip(_translate("dialogOverlayAdjustment", "Stretches the overlay up-left by the entered pixels."))
        self.pushStretchNW.setText(_translate("dialogOverlayAdjustment", "NW"))
        self.pushStretchN.setToolTip(_translate("dialogOverlayAdjustment", "Stretches the overlay up by the entered pixels."))
        self.pushStretchN.setText(_translate("dialogOverlayAdjustment", "N"))
        self.pushStretchNE.setToolTip(_translate("dialogOverlayAdjustment", "Stretches the overlay up-right by the entered pixels."))
        self.pushStretchNE.setText(_translate("dialogOverlayAdjustment", "NE"))
        self.pushStretchUpRight.setToolTip(_translate("dialogOverlayAdjustment", "Pulls the overlay right from the top by the entered pixels."))
        self.pushStretchUpRight.setText(_translate("dialogOverlayAdjustment", "UR"))
        self.pushStretchW.setToolTip(_translate("dialogOverlayAdjustment", "Stretches the overlay left by the entered pixels."))
        self.pushStretchW.setText(_translate("dialogOverlayAdjustment", "W"))
        self.pushResetStretch.setToolTip(_translate("dialogOverlayAdjustment", "Resets any stretching or pulling of the overlay."))
        self.pushResetStretch.setText(_translate("dialogOverlayAdjustment", "RE"))
        self.pushStretchE.setToolTip(_translate("dialogOverlayAdjustment", "Stretches the overlay right by the entered pixels."))
        self.pushStretchE.setText(_translate("dialogOverlayAdjustment", "E"))
        self.pushStretchDownLeft.setToolTip(_translate("dialogOverlayAdjustment", "Pulls the overlay left from the bottom by the entered pixels."))
        self.pushStretchDownLeft.setText(_translate("dialogOverlayAdjustment", "DL"))
        self.pushStretchSW.setToolTip(_translate("dialogOverlayAdjustment", "Stretches the overlay down-left by the entered pixels."))
        self.pushStretchSW.setText(_translate("dialogOverlayAdjustment", "SW"))
        self.pushStretchS.setToolTip(_translate("dialogOverlayAdjustment", "Stretches the overlay down by the entered pixels."))
        self.pushStretchS.setText(_translate("dialogOverlayAdjustment", "S"))
        self.pushStretchSE.setToolTip(_translate("dialogOverlayAdjustment", "Stretches the overlay down-right by the entered pixels."))
        self.pushStretchSE.setText(_translate("dialogOverlayAdjustment", "SE"))
        self.pushStretchDownRight.setToolTip(_translate("dialogOverlayAdjustment", "Pulls the overlay right from the bottom by the entered pixels."))
        self.pushStretchDownRight.setText(_translate("dialogOverlayAdjustment", "DR"))
        self.pushStretchLeftDown.setToolTip(_translate("dialogOverlayAdjustment", "Pulls the overlay down from the left by the entered pixels."))
        self.pushStretchLeftDown.setText(_translate("dialogOverlayAdjustment", "LD"))
        self.pushStretchRightDown.setToolTip(_translate("dialogOverlayAdjustment", "Pulls the overlay down from the right by the entered pixels."))
        self.pushStretchRightDown.setText(_translate("dialogOverlayAdjustment", "RD"))
        self.pushDone.setText(_translate("dialogOverlayAdjustment", "Done"))

import icons_rc
