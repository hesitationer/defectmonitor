# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\dialogSliceConverter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogSliceConverter(object):
    def setupUi(self, dialogSliceConverter):
        dialogSliceConverter.setObjectName("dialogSliceConverter")
        dialogSliceConverter.resize(749, 674)
        self.gridLayout = QtWidgets.QGridLayout(dialogSliceConverter)
        self.gridLayout.setObjectName("gridLayout")
        self.labelLayerNumber = QtWidgets.QLabel(dialogSliceConverter)
        self.labelLayerNumber.setObjectName("labelLayerNumber")
        self.gridLayout.addWidget(self.labelLayerNumber, 6, 5, 2, 1)
        self.label = QtWidgets.QLabel(dialogSliceConverter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 2)
        self.checkRange = QtWidgets.QCheckBox(dialogSliceConverter)
        self.checkRange.setEnabled(False)
        self.checkRange.setObjectName("checkRange")
        self.gridLayout.addWidget(self.checkRange, 10, 0, 1, 2)
        self.spinRangeLow = QtWidgets.QSpinBox(dialogSliceConverter)
        self.spinRangeLow.setEnabled(False)
        self.spinRangeLow.setMinimum(1)
        self.spinRangeLow.setMaximum(99999)
        self.spinRangeLow.setObjectName("spinRangeLow")
        self.gridLayout.addWidget(self.spinRangeLow, 11, 0, 1, 2)
        self.pushAddSF = QtWidgets.QPushButton(dialogSliceConverter)
        self.pushAddSF.setObjectName("pushAddSF")
        self.gridLayout.addWidget(self.pushAddSF, 3, 0, 1, 2)
        self.labelStatusSlice = QtWidgets.QLabel(dialogSliceConverter)
        self.labelStatusSlice.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatusSlice.setObjectName("labelStatusSlice")
        self.gridLayout.addWidget(self.labelStatusSlice, 13, 0, 1, 2)
        self.pushBrowseOF = QtWidgets.QPushButton(dialogSliceConverter)
        self.pushBrowseOF.setObjectName("pushBrowseOF")
        self.gridLayout.addWidget(self.pushBrowseOF, 9, 0, 1, 1)
        self.spinRangeHigh = QtWidgets.QSpinBox(dialogSliceConverter)
        self.spinRangeHigh.setEnabled(False)
        self.spinRangeHigh.setMinimum(1)
        self.spinRangeHigh.setMaximum(99999)
        self.spinRangeHigh.setObjectName("spinRangeHigh")
        self.gridLayout.addWidget(self.spinRangeHigh, 12, 0, 1, 2)
        self.labelLayerPreview = QtWidgets.QLabel(dialogSliceConverter)
        self.labelLayerPreview.setObjectName("labelLayerPreview")
        self.gridLayout.addWidget(self.labelLayerPreview, 0, 2, 1, 4)
        self.label_2 = QtWidgets.QLabel(dialogSliceConverter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(dialogSliceConverter)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 5, 0, 2, 2)
        self.lineFolder = QtWidgets.QLineEdit(dialogSliceConverter)
        self.lineFolder.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineFolder.setReadOnly(True)
        self.lineFolder.setObjectName("lineFolder")
        self.gridLayout.addWidget(self.lineFolder, 8, 0, 1, 2)
        self.pushRemoveSF = QtWidgets.QPushButton(dialogSliceConverter)
        self.pushRemoveSF.setObjectName("pushRemoveSF")
        self.gridLayout.addWidget(self.pushRemoveSF, 4, 0, 1, 2)
        self.spinPreviewLayer = QtWidgets.QSpinBox(dialogSliceConverter)
        self.spinPreviewLayer.setMinimum(1)
        self.spinPreviewLayer.setObjectName("spinPreviewLayer")
        self.gridLayout.addWidget(self.spinPreviewLayer, 8, 3, 1, 1)
        self.pushPreviewLayer = QtWidgets.QPushButton(dialogSliceConverter)
        self.pushPreviewLayer.setObjectName("pushPreviewLayer")
        self.gridLayout.addWidget(self.pushPreviewLayer, 8, 2, 1, 1)
        self.labelLayerNumberTitle = QtWidgets.QLabel(dialogSliceConverter)
        self.labelLayerNumberTitle.setObjectName("labelLayerNumberTitle")
        self.gridLayout.addWidget(self.labelLayerNumberTitle, 6, 4, 2, 1)
        self.listSliceFiles = QtWidgets.QListWidget(dialogSliceConverter)
        self.listSliceFiles.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listSliceFiles.setObjectName("listSliceFiles")
        self.gridLayout.addWidget(self.listSliceFiles, 2, 0, 1, 2)
        self.buttonDone = QtWidgets.QPushButton(dialogSliceConverter)
        self.buttonDone.setMinimumSize(QtCore.QSize(95, 0))
        self.buttonDone.setObjectName("buttonDone")
        self.gridLayout.addWidget(self.buttonDone, 15, 5, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(dialogSliceConverter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelXPosition = QtWidgets.QLabel(self.groupBox)
        self.labelXPosition.setObjectName("labelXPosition")
        self.verticalLayout.addWidget(self.labelXPosition)
        self.labelYPosition = QtWidgets.QLabel(self.groupBox)
        self.labelYPosition.setObjectName("labelYPosition")
        self.verticalLayout.addWidget(self.labelYPosition)
        self.gridLayout.addWidget(self.groupBox, 11, 4, 3, 1)
        self.frame = QtWidgets.QFrame(dialogSliceConverter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsLayerPreview = ImageViewer(self.frame)
        self.graphicsLayerPreview.setObjectName("graphicsLayerPreview")
        self.gridLayout_2.addWidget(self.graphicsLayerPreview, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 2, 2, 5, 4)
        self.groupBox_2 = QtWidgets.QGroupBox(dialogSliceConverter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.gridLayout.addWidget(self.groupBox_2, 8, 4, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(dialogSliceConverter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.spinBox_6 = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout_4.addWidget(self.spinBox_6, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout_4.addWidget(self.spinBox_5, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 3, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 9, 5, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(dialogSliceConverter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 4, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_3.addWidget(self.spinBox_3, 2, 1, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_3.addWidget(self.spinBox_2, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 4, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_3.addWidget(self.spinBox_4, 2, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 3, 0, 1, 5)
        self.gridLayout.addWidget(self.groupBox_3, 8, 5, 1, 1)
        self.labelStatus = QtWidgets.QLabel(dialogSliceConverter)
        self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatus.setObjectName("labelStatus")
        self.gridLayout.addWidget(self.labelStatus, 11, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(dialogSliceConverter)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 12, 2, 1, 1)

        self.retranslateUi(dialogSliceConverter)
        self.buttonDone.clicked.connect(dialogSliceConverter.close)
        self.checkRange.toggled['bool'].connect(self.spinRangeLow.setEnabled)
        self.checkRange.toggled['bool'].connect(self.spinRangeHigh.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(dialogSliceConverter)

    def retranslateUi(self, dialogSliceConverter):
        _translate = QtCore.QCoreApplication.translate
        dialogSliceConverter.setWindowTitle(_translate("dialogSliceConverter", "Slice Converter"))
        self.labelLayerNumber.setText(_translate("dialogSliceConverter", "0000 / 0000"))
        self.label.setText(_translate("dialogSliceConverter", "Output Folder"))
        self.checkRange.setText(_translate("dialogSliceConverter", "Draw Range"))
        self.pushAddSF.setText(_translate("dialogSliceConverter", "Add Slice Files"))
        self.labelStatusSlice.setText(_translate("dialogSliceConverter", "Current Part: None"))
        self.pushBrowseOF.setText(_translate("dialogSliceConverter", "Browse..."))
        self.labelLayerPreview.setText(_translate("dialogSliceConverter", "Layer Preview"))
        self.label_2.setText(_translate("dialogSliceConverter", "Slice Files"))
        self.pushButton_3.setText(_translate("dialogSliceConverter", "Draw Contours"))
        self.pushRemoveSF.setText(_translate("dialogSliceConverter", "Remove Selected Files"))
        self.pushPreviewLayer.setText(_translate("dialogSliceConverter", "Preview Layer"))
        self.labelLayerNumberTitle.setText(_translate("dialogSliceConverter", "Layer Number"))
        self.buttonDone.setText(_translate("dialogSliceConverter", "Done"))
        self.groupBox.setTitle(_translate("dialogSliceConverter", "Mouse Position"))
        self.labelXPosition.setText(_translate("dialogSliceConverter", "X - 000"))
        self.labelYPosition.setText(_translate("dialogSliceConverter", "Y - 000"))
        self.groupBox_2.setTitle(_translate("dialogSliceConverter", "Display Options"))
        self.checkBox.setText(_translate("dialogSliceConverter", "Centrelines"))
        self.checkBox_2.setText(_translate("dialogSliceConverter", "Gridlines"))
        self.groupBox_4.setTitle(_translate("dialogSliceConverter", "Rotate"))
        self.label_11.setText(_translate("dialogSliceConverter", "Incremental"))
        self.label_12.setText(_translate("dialogSliceConverter", "Absolute"))
        self.pushButton_5.setText(_translate("dialogSliceConverter", "Rotate"))
        self.label_13.setText(_translate("dialogSliceConverter", "Angle"))
        self.groupBox_3.setTitle(_translate("dialogSliceConverter", "Translation"))
        self.label_3.setText(_translate("dialogSliceConverter", "Incremental"))
        self.label_4.setText(_translate("dialogSliceConverter", "X"))
        self.label_5.setText(_translate("dialogSliceConverter", "px"))
        self.label_7.setText(_translate("dialogSliceConverter", "Y"))
        self.label_6.setText(_translate("dialogSliceConverter", "px"))
        self.label_8.setText(_translate("dialogSliceConverter", "Absolute"))
        self.label_10.setText(_translate("dialogSliceConverter", "px"))
        self.label_9.setText(_translate("dialogSliceConverter", "px"))
        self.pushButton_4.setText(_translate("dialogSliceConverter", "Translate"))
        self.labelStatus.setText(_translate("dialogSliceConverter", "Please select a .cli file(s) to convert."))

from ui_elements import ImageViewer
