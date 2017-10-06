# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\dialogDefectReports.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogDefectReports(object):
    def setupUi(self, dialogDefectReports):
        dialogDefectReports.setObjectName("dialogDefectReports")
        dialogDefectReports.resize(488, 695)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogDefectReports.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(dialogDefectReports)
        self.gridLayout.setObjectName("gridLayout")
        self.labelParts = QtWidgets.QLabel(dialogDefectReports)
        self.labelParts.setObjectName("labelParts")
        self.gridLayout.addWidget(self.labelParts, 0, 0, 1, 1)
        self.groupThresholdValues = QtWidgets.QGroupBox(dialogDefectReports)
        self.groupThresholdValues.setObjectName("groupThresholdValues")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupThresholdValues)
        self.gridLayout_4.setContentsMargins(9, 3, 9, 6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frameLeft = QtWidgets.QFrame(self.groupThresholdValues)
        self.frameLeft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLeft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLeft.setObjectName("frameLeft")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frameLeft)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelOccurrences = QtWidgets.QLabel(self.frameLeft)
        self.labelOccurrences.setObjectName("labelOccurrences")
        self.gridLayout_5.addWidget(self.labelOccurrences, 1, 0, 1, 1)
        self.spinPixelSize = QtWidgets.QDoubleSpinBox(self.frameLeft)
        self.spinPixelSize.setDecimals(4)
        self.spinPixelSize.setMaximum(100.0)
        self.spinPixelSize.setSingleStep(0.001)
        self.spinPixelSize.setObjectName("spinPixelSize")
        self.gridLayout_5.addWidget(self.spinPixelSize, 0, 1, 1, 1)
        self.labelPixelSize = QtWidgets.QLabel(self.frameLeft)
        self.labelPixelSize.setObjectName("labelPixelSize")
        self.gridLayout_5.addWidget(self.labelPixelSize, 0, 0, 1, 1)
        self.spinOccurrences = QtWidgets.QSpinBox(self.frameLeft)
        self.spinOccurrences.setMaximum(1000)
        self.spinOccurrences.setObjectName("spinOccurrences")
        self.gridLayout_5.addWidget(self.spinOccurrences, 1, 1, 1, 1)
        self.labelOverlay = QtWidgets.QLabel(self.frameLeft)
        self.labelOverlay.setObjectName("labelOverlay")
        self.gridLayout_5.addWidget(self.labelOverlay, 2, 0, 1, 1)
        self.spinOverlay = QtWidgets.QDoubleSpinBox(self.frameLeft)
        self.spinOverlay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinOverlay.setDecimals(4)
        self.spinOverlay.setMaximum(100.0)
        self.spinOverlay.setSingleStep(0.1)
        self.spinOverlay.setObjectName("spinOverlay")
        self.gridLayout_5.addWidget(self.spinOverlay, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frameLeft, 1, 4, 1, 1)
        self.frameRight = QtWidgets.QFrame(self.groupThresholdValues)
        self.frameRight.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRight.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameRight.setObjectName("frameRight")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frameRight)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.labelHistogramCoat = QtWidgets.QLabel(self.frameRight)
        self.labelHistogramCoat.setObjectName("labelHistogramCoat")
        self.gridLayout_6.addWidget(self.labelHistogramCoat, 1, 0, 1, 1)
        self.spinHistogramCoat = QtWidgets.QSpinBox(self.frameRight)
        self.spinHistogramCoat.setMaximum(50000)
        self.spinHistogramCoat.setSingleStep(100)
        self.spinHistogramCoat.setObjectName("spinHistogramCoat")
        self.gridLayout_6.addWidget(self.spinHistogramCoat, 1, 1, 1, 1)
        self.labelHistogramScan = QtWidgets.QLabel(self.frameRight)
        self.labelHistogramScan.setObjectName("labelHistogramScan")
        self.gridLayout_6.addWidget(self.labelHistogramScan, 2, 0, 2, 1)
        self.spinHistogramScan = QtWidgets.QSpinBox(self.frameRight)
        self.spinHistogramScan.setMaximum(50000)
        self.spinHistogramScan.setSingleStep(100)
        self.spinHistogramScan.setObjectName("spinHistogramScan")
        self.gridLayout_6.addWidget(self.spinHistogramScan, 2, 1, 1, 1)
        self.pushSet = QtWidgets.QPushButton(self.frameRight)
        self.pushSet.setObjectName("pushSet")
        self.gridLayout_6.addWidget(self.pushSet, 4, 0, 1, 2)
        self.gridLayout_4.addWidget(self.frameRight, 1, 5, 1, 1)
        self.gridLayout.addWidget(self.groupThresholdValues, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(dialogDefectReports)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)
        self.widgetReports = QtWidgets.QTabWidget(dialogDefectReports)
        self.widgetReports.setObjectName("widgetReports")
        self.tabCoat = QtWidgets.QWidget()
        self.tabCoat.setObjectName("tabCoat")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabCoat)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableCoat = QtWidgets.QTableWidget(self.tabCoat)
        self.tableCoat.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableCoat.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableCoat.setObjectName("tableCoat")
        self.tableCoat.setColumnCount(6)
        self.tableCoat.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableCoat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCoat.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCoat.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCoat.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCoat.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCoat.setHorizontalHeaderItem(5, item)
        self.tableCoat.horizontalHeader().setMinimumSectionSize(32)
        self.tableCoat.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableCoat, 0, 0, 1, 1)
        self.widgetReports.addTab(self.tabCoat, "")
        self.tabScan = QtWidgets.QWidget()
        self.tabScan.setObjectName("tabScan")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabScan)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableScan = QtWidgets.QTableWidget(self.tabScan)
        self.tableScan.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableScan.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableScan.setObjectName("tableScan")
        self.tableScan.setColumnCount(5)
        self.tableScan.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableScan.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableScan.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableScan.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableScan.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableScan.setHorizontalHeaderItem(4, item)
        self.tableScan.horizontalHeader().setMinimumSectionSize(32)
        self.tableScan.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tableScan, 0, 0, 1, 1)
        self.widgetReports.addTab(self.tabScan, "")
        self.gridLayout.addWidget(self.widgetReports, 4, 0, 1, 2)
        self.pushPrint = QtWidgets.QPushButton(dialogDefectReports)
        self.pushPrint.setEnabled(False)
        self.pushPrint.setObjectName("pushPrint")
        self.gridLayout.addWidget(self.pushPrint, 5, 0, 1, 1)
        self.pushDone = QtWidgets.QPushButton(dialogDefectReports)
        self.pushDone.setObjectName("pushDone")
        self.gridLayout.addWidget(self.pushDone, 5, 1, 1, 1)
        self.comboParts = QtWidgets.QComboBox(dialogDefectReports)
        self.comboParts.setObjectName("comboParts")
        self.gridLayout.addWidget(self.comboParts, 1, 0, 1, 2)

        self.retranslateUi(dialogDefectReports)
        self.widgetReports.setCurrentIndex(0)
        self.pushDone.clicked.connect(dialogDefectReports.close)
        QtCore.QMetaObject.connectSlotsByName(dialogDefectReports)
        dialogDefectReports.setTabOrder(self.comboParts, self.spinPixelSize)
        dialogDefectReports.setTabOrder(self.spinPixelSize, self.spinOccurrences)
        dialogDefectReports.setTabOrder(self.spinOccurrences, self.spinOverlay)
        dialogDefectReports.setTabOrder(self.spinOverlay, self.spinHistogramCoat)
        dialogDefectReports.setTabOrder(self.spinHistogramCoat, self.spinHistogramScan)
        dialogDefectReports.setTabOrder(self.spinHistogramScan, self.pushSet)
        dialogDefectReports.setTabOrder(self.pushSet, self.widgetReports)
        dialogDefectReports.setTabOrder(self.widgetReports, self.tableCoat)
        dialogDefectReports.setTabOrder(self.tableCoat, self.pushPrint)
        dialogDefectReports.setTabOrder(self.pushPrint, self.pushDone)
        dialogDefectReports.setTabOrder(self.pushDone, self.tableScan)

    def retranslateUi(self, dialogDefectReports):
        _translate = QtCore.QCoreApplication.translate
        dialogDefectReports.setWindowTitle(_translate("dialogDefectReports", "Defect Reports"))
        self.labelParts.setText(_translate("dialogDefectReports", "Part Selection"))
        self.groupThresholdValues.setTitle(_translate("dialogDefectReports", "Threshold Values"))
        self.labelOccurrences.setToolTip(_translate("dialogDefectReports", "Integer amount specifying the number of blade streaks and blade chatter."))
        self.labelOccurrences.setText(_translate("dialogDefectReports", "Defect Occurrences"))
        self.spinPixelSize.setToolTip(_translate("dialogDefectReports", "0 - 100"))
        self.labelPixelSize.setToolTip(_translate("dialogDefectReports", "Percentage amount specifying the number of defect bright spots and contrast difference pixels."))
        self.labelPixelSize.setText(_translate("dialogDefectReports", "Pixel Size (%)"))
        self.spinOccurrences.setToolTip(_translate("dialogDefectReports", "0 - 1000"))
        self.labelOverlay.setToolTip(_translate("dialogDefectReports", "Percentage amount specifying the similarity between the detected scan pattern and the part contours."))
        self.labelOverlay.setText(_translate("dialogDefectReports", "Overlay Compare (%)"))
        self.spinOverlay.setToolTip(_translate("dialogDefectReports", "0 - 100"))
        self.labelHistogramCoat.setText(_translate("dialogDefectReports", "Histogram Compare (Coat)"))
        self.spinHistogramCoat.setToolTip(_translate("dialogDefectReports", "0 - 50000"))
        self.labelHistogramScan.setText(_translate("dialogDefectReports", "Histogram Compare (Scan)"))
        self.spinHistogramScan.setToolTip(_translate("dialogDefectReports", "0 - 50000"))
        self.pushSet.setToolTip(_translate("dialogDefectReports", "Click to set modified threshold values and/or reload the reports."))
        self.pushSet.setText(_translate("dialogDefectReports", "Set / Reload"))
        self.label.setText(_translate("dialogDefectReports", "Double click on a row\'s cell to display that layer\'s defect image."))
        self.tableCoat.setSortingEnabled(True)
        item = self.tableCoat.horizontalHeaderItem(0)
        item.setText(_translate("dialogDefectReports", "#"))
        item = self.tableCoat.horizontalHeaderItem(1)
        item.setText(_translate("dialogDefectReports", "Streaks"))
        item = self.tableCoat.horizontalHeaderItem(2)
        item.setText(_translate("dialogDefectReports", "Chatter"))
        item = self.tableCoat.horizontalHeaderItem(3)
        item.setText(_translate("dialogDefectReports", "Spots"))
        item = self.tableCoat.horizontalHeaderItem(4)
        item.setText(_translate("dialogDefectReports", "Contrast"))
        item = self.tableCoat.horizontalHeaderItem(5)
        item.setText(_translate("dialogDefectReports", "Histogram"))
        self.widgetReports.setTabText(self.widgetReports.indexOf(self.tabCoat), _translate("dialogDefectReports", "Coat Explorer"))
        self.tableScan.setSortingEnabled(True)
        item = self.tableScan.horizontalHeaderItem(0)
        item.setText(_translate("dialogDefectReports", "#"))
        item = self.tableScan.horizontalHeaderItem(1)
        item.setText(_translate("dialogDefectReports", "Streaks"))
        item = self.tableScan.horizontalHeaderItem(2)
        item.setText(_translate("dialogDefectReports", "Chatter"))
        item = self.tableScan.horizontalHeaderItem(3)
        item.setText(_translate("dialogDefectReports", "Histogram"))
        item = self.tableScan.horizontalHeaderItem(4)
        item.setText(_translate("dialogDefectReports", "Overlay"))
        self.widgetReports.setTabText(self.widgetReports.indexOf(self.tabScan), _translate("dialogDefectReports", "Scan Explorer"))
        self.pushPrint.setText(_translate("dialogDefectReports", "Print Report"))
        self.pushDone.setText(_translate("dialogDefectReports", "Done"))

import icons_rc
