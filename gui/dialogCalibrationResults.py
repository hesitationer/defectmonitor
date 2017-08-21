# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogCalibrationResults.ui'
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

class Ui_dialogCalibrationResults(object):
    def setupUi(self, dialogCalibrationResults):
        dialogCalibrationResults.setObjectName(_fromUtf8("dialogCalibrationResults"))
        dialogCalibrationResults.resize(411, 408)
        dialogCalibrationResults.setMinimumSize(QtCore.QSize(411, 408))
        dialogCalibrationResults.setMaximumSize(QtCore.QSize(411, 408))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogCalibrationResults.setWindowIcon(icon)
        self.buttonDone = QtGui.QPushButton(dialogCalibrationResults)
        self.buttonDone.setGeometry(QtCore.QRect(280, 370, 121, 28))
        self.buttonDone.setObjectName(_fromUtf8("buttonDone"))
        self.labelRMS = QtGui.QLabel(dialogCalibrationResults)
        self.labelRMS.setGeometry(QtCore.QRect(10, 370, 271, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelRMS.setFont(font)
        self.labelRMS.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelRMS.setObjectName(_fromUtf8("labelRMS"))
        self.tableCameraMatrix = QtGui.QTableWidget(dialogCalibrationResults)
        self.tableCameraMatrix.setEnabled(True)
        self.tableCameraMatrix.setGeometry(QtCore.QRect(10, 40, 391, 91))
        self.tableCameraMatrix.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableCameraMatrix.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableCameraMatrix.setAutoScroll(False)
        self.tableCameraMatrix.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableCameraMatrix.setShowGrid(True)
        self.tableCameraMatrix.setWordWrap(True)
        self.tableCameraMatrix.setCornerButtonEnabled(True)
        self.tableCameraMatrix.setRowCount(3)
        self.tableCameraMatrix.setColumnCount(3)
        self.tableCameraMatrix.setObjectName(_fromUtf8("tableCameraMatrix"))
        item = QtGui.QTableWidgetItem()
        self.tableCameraMatrix.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableCameraMatrix.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableCameraMatrix.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableCameraMatrix.setItem(0, 0, item)
        self.tableCameraMatrix.horizontalHeader().setVisible(False)
        self.tableCameraMatrix.horizontalHeader().setDefaultSectionSize(130)
        self.tableCameraMatrix.verticalHeader().setVisible(False)
        self.labelCameraMatrix = QtGui.QLabel(dialogCalibrationResults)
        self.labelCameraMatrix.setGeometry(QtCore.QRect(10, 0, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelCameraMatrix.setFont(font)
        self.labelCameraMatrix.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCameraMatrix.setObjectName(_fromUtf8("labelCameraMatrix"))
        self.labelDistortionCoefficients = QtGui.QLabel(dialogCalibrationResults)
        self.labelDistortionCoefficients.setGeometry(QtCore.QRect(10, 130, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelDistortionCoefficients.setFont(font)
        self.labelDistortionCoefficients.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDistortionCoefficients.setObjectName(_fromUtf8("labelDistortionCoefficients"))
        self.tableDistortionCoefficients = QtGui.QTableWidget(dialogCalibrationResults)
        self.tableDistortionCoefficients.setEnabled(True)
        self.tableDistortionCoefficients.setGeometry(QtCore.QRect(10, 170, 391, 61))
        self.tableDistortionCoefficients.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableDistortionCoefficients.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableDistortionCoefficients.setAutoScroll(False)
        self.tableDistortionCoefficients.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableDistortionCoefficients.setShowGrid(True)
        self.tableDistortionCoefficients.setWordWrap(True)
        self.tableDistortionCoefficients.setCornerButtonEnabled(True)
        self.tableDistortionCoefficients.setRowCount(2)
        self.tableDistortionCoefficients.setColumnCount(3)
        self.tableDistortionCoefficients.setObjectName(_fromUtf8("tableDistortionCoefficients"))
        item = QtGui.QTableWidgetItem()
        self.tableDistortionCoefficients.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableDistortionCoefficients.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableDistortionCoefficients.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableDistortionCoefficients.setItem(0, 0, item)
        self.tableDistortionCoefficients.horizontalHeader().setVisible(False)
        self.tableDistortionCoefficients.horizontalHeader().setDefaultSectionSize(130)
        self.tableDistortionCoefficients.verticalHeader().setVisible(False)
        self.labelHomographyMatrix = QtGui.QLabel(dialogCalibrationResults)
        self.labelHomographyMatrix.setGeometry(QtCore.QRect(10, 230, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelHomographyMatrix.setFont(font)
        self.labelHomographyMatrix.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHomographyMatrix.setObjectName(_fromUtf8("labelHomographyMatrix"))
        self.tableHomographyMatrix = QtGui.QTableWidget(dialogCalibrationResults)
        self.tableHomographyMatrix.setEnabled(True)
        self.tableHomographyMatrix.setGeometry(QtCore.QRect(10, 270, 391, 91))
        self.tableHomographyMatrix.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableHomographyMatrix.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableHomographyMatrix.setAutoScroll(False)
        self.tableHomographyMatrix.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableHomographyMatrix.setShowGrid(True)
        self.tableHomographyMatrix.setWordWrap(True)
        self.tableHomographyMatrix.setCornerButtonEnabled(True)
        self.tableHomographyMatrix.setRowCount(3)
        self.tableHomographyMatrix.setColumnCount(3)
        self.tableHomographyMatrix.setObjectName(_fromUtf8("tableHomographyMatrix"))
        item = QtGui.QTableWidgetItem()
        self.tableHomographyMatrix.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableHomographyMatrix.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableHomographyMatrix.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableHomographyMatrix.setItem(0, 0, item)
        self.tableHomographyMatrix.horizontalHeader().setVisible(False)
        self.tableHomographyMatrix.horizontalHeader().setDefaultSectionSize(130)
        self.tableHomographyMatrix.verticalHeader().setVisible(False)

        self.retranslateUi(dialogCalibrationResults)
        QtCore.QObject.connect(self.buttonDone, QtCore.SIGNAL(_fromUtf8("clicked()")), dialogCalibrationResults.accept)
        QtCore.QMetaObject.connectSlotsByName(dialogCalibrationResults)

    def retranslateUi(self, dialogCalibrationResults):
        dialogCalibrationResults.setWindowTitle(_translate("dialogCalibrationResults", "Calibration Results", None))
        self.buttonDone.setText(_translate("dialogCalibrationResults", "Done", None))
        self.labelRMS.setToolTip(_translate("dialogCalibrationResults", "An acceptable error should be less than 1 pixel.", None))
        self.labelRMS.setText(_translate("dialogCalibrationResults", "Re-Projection Error: 0.000000000", None))
        item = self.tableCameraMatrix.horizontalHeaderItem(0)
        item.setText(_translate("dialogCalibrationResults", "1", None))
        item = self.tableCameraMatrix.horizontalHeaderItem(1)
        item.setText(_translate("dialogCalibrationResults", "2", None))
        item = self.tableCameraMatrix.horizontalHeaderItem(2)
        item.setText(_translate("dialogCalibrationResults", "3", None))
        __sortingEnabled = self.tableCameraMatrix.isSortingEnabled()
        self.tableCameraMatrix.setSortingEnabled(False)
        self.tableCameraMatrix.setSortingEnabled(__sortingEnabled)
        self.labelCameraMatrix.setText(_translate("dialogCalibrationResults", "Camera Matrix", None))
        self.labelDistortionCoefficients.setText(_translate("dialogCalibrationResults", "Distortion Coefficients", None))
        item = self.tableDistortionCoefficients.horizontalHeaderItem(0)
        item.setText(_translate("dialogCalibrationResults", "1", None))
        item = self.tableDistortionCoefficients.horizontalHeaderItem(1)
        item.setText(_translate("dialogCalibrationResults", "2", None))
        item = self.tableDistortionCoefficients.horizontalHeaderItem(2)
        item.setText(_translate("dialogCalibrationResults", "3", None))
        __sortingEnabled = self.tableDistortionCoefficients.isSortingEnabled()
        self.tableDistortionCoefficients.setSortingEnabled(False)
        self.tableDistortionCoefficients.setSortingEnabled(__sortingEnabled)
        self.labelHomographyMatrix.setText(_translate("dialogCalibrationResults", "Homography Matrix", None))
        item = self.tableHomographyMatrix.horizontalHeaderItem(0)
        item.setText(_translate("dialogCalibrationResults", "1", None))
        item = self.tableHomographyMatrix.horizontalHeaderItem(1)
        item.setText(_translate("dialogCalibrationResults", "2", None))
        item = self.tableHomographyMatrix.horizontalHeaderItem(2)
        item.setText(_translate("dialogCalibrationResults", "3", None))
        __sortingEnabled = self.tableHomographyMatrix.isSortingEnabled()
        self.tableHomographyMatrix.setSortingEnabled(False)
        self.tableHomographyMatrix.setSortingEnabled(__sortingEnabled)

import icons_rc
