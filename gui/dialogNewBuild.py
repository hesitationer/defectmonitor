# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\dialogNewBuild.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogNewBuild(object):
    def setupUi(self, dialogNewBuild):
        dialogNewBuild.setObjectName("dialogNewBuild")
        dialogNewBuild.resize(361, 260)
        font = QtGui.QFont()
        font.setPointSize(9)
        dialogNewBuild.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(dialogNewBuild)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.labelImageFolder = QtWidgets.QLabel(dialogNewBuild)
        self.labelImageFolder.setObjectName("labelImageFolder")
        self.gridLayout.addWidget(self.labelImageFolder, 3, 0, 1, 1)
        self.labelMachine = QtWidgets.QLabel(dialogNewBuild)
        self.labelMachine.setObjectName("labelMachine")
        self.gridLayout.addWidget(self.labelMachine, 1, 0, 1, 1)
        self.labelEmailAddress = QtWidgets.QLabel(dialogNewBuild)
        self.labelEmailAddress.setObjectName("labelEmailAddress")
        self.gridLayout.addWidget(self.labelEmailAddress, 7, 0, 1, 1)
        self.labelUsername = QtWidgets.QLabel(dialogNewBuild)
        self.labelUsername.setObjectName("labelUsername")
        self.gridLayout.addWidget(self.labelUsername, 6, 0, 1, 1)
        self.pushCreate = QtWidgets.QPushButton(dialogNewBuild)
        self.pushCreate.setObjectName("pushCreate")
        self.gridLayout.addWidget(self.pushCreate, 9, 3, 1, 1)
        self.pushCancel = QtWidgets.QPushButton(dialogNewBuild)
        self.pushCancel.setObjectName("pushCancel")
        self.gridLayout.addWidget(self.pushCancel, 10, 3, 1, 1)
        self.lineImageFolder = QtWidgets.QLineEdit(dialogNewBuild)
        self.lineImageFolder.setReadOnly(True)
        self.lineImageFolder.setObjectName("lineImageFolder")
        self.gridLayout.addWidget(self.lineImageFolder, 3, 1, 1, 2)
        self.comboMachine = QtWidgets.QComboBox(dialogNewBuild)
        self.comboMachine.setObjectName("comboMachine")
        self.comboMachine.addItem("")
        self.gridLayout.addWidget(self.comboMachine, 1, 1, 1, 3)
        self.labelBuildName = QtWidgets.QLabel(dialogNewBuild)
        self.labelBuildName.setObjectName("labelBuildName")
        self.gridLayout.addWidget(self.labelBuildName, 0, 0, 1, 1)
        self.pushBrowseIF = QtWidgets.QPushButton(dialogNewBuild)
        self.pushBrowseIF.setObjectName("pushBrowseIF")
        self.gridLayout.addWidget(self.pushBrowseIF, 3, 3, 1, 1)
        self.lineBuildName = QtWidgets.QLineEdit(dialogNewBuild)
        self.lineBuildName.setClearButtonEnabled(True)
        self.lineBuildName.setObjectName("lineBuildName")
        self.gridLayout.addWidget(self.lineBuildName, 0, 1, 1, 3)
        self.comboCamera = QtWidgets.QComboBox(dialogNewBuild)
        self.comboCamera.setObjectName("comboCamera")
        self.comboCamera.addItem("")
        self.gridLayout.addWidget(self.comboCamera, 2, 1, 1, 3)
        self.lineUsername = QtWidgets.QLineEdit(dialogNewBuild)
        self.lineUsername.setClearButtonEnabled(True)
        self.lineUsername.setObjectName("lineUsername")
        self.gridLayout.addWidget(self.lineUsername, 6, 1, 1, 3)
        self.pushSendTestEmail = QtWidgets.QPushButton(dialogNewBuild)
        self.pushSendTestEmail.setEnabled(False)
        self.pushSendTestEmail.setObjectName("pushSendTestEmail")
        self.gridLayout.addWidget(self.pushSendTestEmail, 9, 0, 1, 2)
        self.lineEmailAddress = QtWidgets.QLineEdit(dialogNewBuild)
        self.lineEmailAddress.setClearButtonEnabled(True)
        self.lineEmailAddress.setObjectName("lineEmailAddress")
        self.gridLayout.addWidget(self.lineEmailAddress, 7, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 2, 1, 1)
        self.checkAddAttachment = QtWidgets.QCheckBox(dialogNewBuild)
        self.checkAddAttachment.setEnabled(False)
        self.checkAddAttachment.setObjectName("checkAddAttachment")
        self.gridLayout.addWidget(self.checkAddAttachment, 10, 0, 1, 2)
        self.labelCamera = QtWidgets.QLabel(dialogNewBuild)
        self.labelCamera.setObjectName("labelCamera")
        self.gridLayout.addWidget(self.labelCamera, 2, 0, 1, 1)
        self.labelBuildFile = QtWidgets.QLabel(dialogNewBuild)
        self.labelBuildFile.setObjectName("labelBuildFile")
        self.gridLayout.addWidget(self.labelBuildFile, 4, 0, 1, 1)
        self.pushSaveAsBF = QtWidgets.QPushButton(dialogNewBuild)
        self.pushSaveAsBF.setObjectName("pushSaveAsBF")
        self.gridLayout.addWidget(self.pushSaveAsBF, 4, 3, 1, 1)
        self.lineBuildFile = QtWidgets.QLineEdit(dialogNewBuild)
        self.lineBuildFile.setReadOnly(True)
        self.lineBuildFile.setObjectName("lineBuildFile")
        self.gridLayout.addWidget(self.lineBuildFile, 4, 1, 1, 2)
        self.labelMachine.setBuddy(self.comboMachine)
        self.labelEmailAddress.setBuddy(self.lineEmailAddress)
        self.labelUsername.setBuddy(self.lineUsername)
        self.labelBuildName.setBuddy(self.lineBuildName)

        self.retranslateUi(dialogNewBuild)
        self.pushCancel.clicked.connect(dialogNewBuild.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogNewBuild)
        dialogNewBuild.setTabOrder(self.lineBuildName, self.comboMachine)
        dialogNewBuild.setTabOrder(self.comboMachine, self.comboCamera)
        dialogNewBuild.setTabOrder(self.comboCamera, self.lineImageFolder)
        dialogNewBuild.setTabOrder(self.lineImageFolder, self.pushBrowseIF)
        dialogNewBuild.setTabOrder(self.pushBrowseIF, self.lineBuildFile)
        dialogNewBuild.setTabOrder(self.lineBuildFile, self.pushSaveAsBF)
        dialogNewBuild.setTabOrder(self.pushSaveAsBF, self.lineUsername)
        dialogNewBuild.setTabOrder(self.lineUsername, self.lineEmailAddress)
        dialogNewBuild.setTabOrder(self.lineEmailAddress, self.pushSendTestEmail)
        dialogNewBuild.setTabOrder(self.pushSendTestEmail, self.checkAddAttachment)
        dialogNewBuild.setTabOrder(self.checkAddAttachment, self.pushCreate)
        dialogNewBuild.setTabOrder(self.pushCreate, self.pushCancel)

    def retranslateUi(self, dialogNewBuild):
        _translate = QtCore.QCoreApplication.translate
        dialogNewBuild.setWindowTitle(_translate("dialogNewBuild", "New Build"))
        self.labelImageFolder.setText(_translate("dialogNewBuild", "Image Folder"))
        self.labelMachine.setText(_translate("dialogNewBuild", "Machine"))
        self.labelEmailAddress.setText(_translate("dialogNewBuild", "Email Address"))
        self.labelUsername.setText(_translate("dialogNewBuild", "Username"))
        self.pushCreate.setText(_translate("dialogNewBuild", "Create"))
        self.pushCancel.setText(_translate("dialogNewBuild", "Cancel"))
        self.comboMachine.setItemText(0, _translate("dialogNewBuild", "Concept Laser Xline 1000R"))
        self.labelBuildName.setText(_translate("dialogNewBuild", "Build Name"))
        self.pushBrowseIF.setToolTip(_translate("dialogNewBuild", "Select where the captured images for the current build will be stored."))
        self.pushBrowseIF.setText(_translate("dialogNewBuild", "Browse..."))
        self.comboCamera.setItemText(0, _translate("dialogNewBuild", "Basler Ace acA3800-10gm GigE"))
        self.pushSendTestEmail.setText(_translate("dialogNewBuild", "Send Test Email"))
        self.checkAddAttachment.setToolTip(_translate("dialogNewBuild", "Check this box to add an attachment (a test picture) to the test email notification."))
        self.checkAddAttachment.setText(_translate("dialogNewBuild", "Add Test Attachment"))
        self.labelCamera.setText(_translate("dialogNewBuild", "Camera"))
        self.labelBuildFile.setText(_translate("dialogNewBuild", "Build File"))
        self.pushSaveAsBF.setToolTip(_translate("dialogNewBuild", "Select where the settings file for the current build will be stored."))
        self.pushSaveAsBF.setText(_translate("dialogNewBuild", "Save As..."))

