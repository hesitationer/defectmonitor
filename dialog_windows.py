# Import libraries and modules
import os
import cv2
import numpy as np
import json
import csv
import shutil
from datetime import datetime
from validate_email import validate_email

# Import PyQt modules
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Import related modules
import slice_converter
import image_capture
import image_processing
import notifications
import camera_calibration
import qt_thread

# Import PyQt GUIs
from gui import dialogNewBuild, dialogPreferences, dialogCameraSettings, dialogCameraCalibration, \
    dialogCalibrationResults, dialogStressTest, dialogSliceConverter, dialogImageConverter, dialogDefectReports


class NewBuild(QDialog, dialogNewBuild.Ui_dialogNewBuild):
    """Module used to initiate the modal New Build/Open Build/Settings dialog window
    Allows the user to either setup a new build or open an existing build and change settings
    """

    def __init__(self, parent=None, build_file='', settings_flag=False):

        # Setup Dialog UI with MainWindow as parent
        super(NewBuild, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)

        # This line removes the What's This question mark from the dialog window title bar
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)

        # Flag to prevent additional image folders from being created
        self.open_flag = bool(build_file)
        self.settings_flag = settings_flag

        # Load from the build_default.json file unless window was opened by Open Build or Settings
        if not build_file:
            build_file = 'build_default.json'

        with open(build_file) as build:
            self.build = json.load(build)

        # Load from the config.json file
        with open('config.json') as config:
            self.config = json.load(config)

        # Setup event listeners for all the relevant UI components, and connect them to specific functions
        # Buttons
        self.pushBrowseIF.clicked.connect(self.browse_folder)
        self.pushSaveAsBF.clicked.connect(self.save_file)
        self.pushSendTestEmail.clicked.connect(self.send_test_email)
        self.pushCreate.clicked.connect(self.create)

        # Lines
        self.lineUsername.textChanged.connect(self.enable_test)
        self.lineEmailAddress.textChanged.connect(self.enable_test)

        # Set default placeholder text in some of the fields
        self.lineBuildName.setPlaceholderText(self.config['Defaults']['BuildName'])
        self.lineUsername.setPlaceholderText(self.config['Defaults']['Username'])
        self.lineEmailAddress.setPlaceholderText(self.config['Defaults']['EmailAddress'])

        # If this dialog window was opened as a result of the Open... action, then the following is executed
        # Set and display the relevant names/values of the following text boxes as outlined in the opened config file
        if self.open_flag:
            self.setWindowTitle('Open Build')
            self.pushCreate.setText('Load')
            self.lineBuildName.setText(self.build['BuildInfo']['Name'])
            self.lineImageFolder.setText(self.build['BuildInfo']['Folder'])
            self.lineBuildFile.setText(build_file)
            self.lineUsername.setText(self.build['BuildInfo']['Username'])
            self.lineEmailAddress.setText(self.build['BuildInfo']['EmailAddress'])
        else:
            # Otherwise do a few setup procedures for the New Build
            self.lineBuildName.textChanged.connect(self.folder_change)
            self.lineBuildName.textChanged.connect(self.file_change)

            # Set and display a default image folder name to save images for the current build
            # Generate a timestamp for folder labelling purposes
            time = datetime.now()
            self.image_folder = """%s/%s-%s-%s [%s''%s'%s]""" % \
                                (self.config['BuildFolder'], time.year, str(time.month).zfill(2), str(time.day).zfill(2),
                                 str(time.hour).zfill(2), str(time.minute).zfill(2), str(time.second).zfill(2))
            self.folder_change()
            self.file_change()

        # If this dialog window was opened as a result of the Build Settings... action, then the following is executed
        # Disable a few of the buttons to disallow changing of the slice files and build folder
        if settings_flag:
            self.pushBrowseIF.setEnabled(False)
            self.setWindowTitle('Build Settings')
            self.pushCreate.setText('OK')

        self.threadpool = QThreadPool()

    def browse_folder(self):
        """Prompts the user to select a folder to store the current build's image folder"""

        folder = QFileDialog.getExistingDirectory(self, 'Browse...', '')

        if folder:
            # Display just the folder name on the line box and disable the Build Name from changing the folder name
            self.lineImageFolder.setText(folder)

            # Disconnecting the signal connection needs to be in a try loop as this method can be called again
            try:
                self.lineBuildName.textChanged.disconnect(self.folder_change)
            except TypeError:
                pass

    def save_file(self):
        """Prompts the user to enter a file name to use to store the build's settings file"""

        # Use the placeholder text if the text box is empty
        if self.lineBuildName.text():
            build_name = self.lineBuildName.text()
        else:
            build_name = self.lineBuildName.placeholderText()

        filename = QFileDialog.getSaveFileName(self, 'Save As...', '%s/%s' % (self.config['BuildFolder'], build_name),
                                               'JSON File (*.json)')[0]

        if filename:
            self.lineBuildFile.setText(filename)
            try:
                self.lineBuildName.textChanged.disconnect(self.file_change)
            except TypeError:
                pass

    def folder_change(self):
        """Changes the prospective image folder name depending on the entered Build Name
        Otherwise the placeholder text in the Build Name is used if the Name field is empty
        """

        if self.lineBuildName.text():
            self.lineImageFolder.setText('%s %s' % (self.image_folder, self.lineBuildName.text()))
        else:
            self.lineImageFolder.setText('%s %s' % (self.image_folder, self.lineBuildName.placeholderText()))

    def file_change(self):
        """Same as the folder change method except for the build file name
        Methods had to be separated so the individual connections with the build name can be disconnected
        """

        if self.lineBuildName.text():
            self.lineBuildFile.setText('%s/%s.json' % (self.config['BuildFolder'], self.lineBuildName.text()))
        else:
            self.lineBuildFile.setText('%s/%s.json' % (self.config['BuildFolder'], self.lineBuildName.placeholderText()))

    def enable_test(self):
        """(Re-)Enables the Send Test Email button if the username and email address boxes have changed and not empty"""

        # Check if both the username and email addresses boxes have text in them, and if the email address is valid
        flag = bool(self.lineUsername.text()) and validate_email(self.lineEmailAddress.text())

        self.pushSendTestEmail.setEnabled(flag)
        self.checkAddAttachment.setEnabled(flag)

    def send_test_email(self):
        """Sends a test notification email to the entered email address"""

        # Open a message box with a send test email confirmation message so accidental emails don't get sent
        send_confirmation = QMessageBox(self)
        send_confirmation.setWindowTitle('Send Test Email')
        send_confirmation.setIcon(QMessageBox.Question)
        send_confirmation.setText('Are you sure you want to send a test notification email to %s at %s?\n\nNote that '
                                  'sending the notification email will take a while.' %
                                  (self.lineUsername.text(), self.lineEmailAddress.text()))
        send_confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = send_confirmation.exec_()

        # If the user clicked Yes
        # The email address doesn't need to be validated as it needs to be valid to enter this method in the first place
        if retval == 16384:
            # Disable the Send Test Email button to prevent SPAM and other buttons until the thread is finished
            self.pushSendTestEmail.setEnabled(False)
            self.pushCreate.setEnabled(False)
            self.pushCancel.setEnabled(False)

            # Check if a test image is to be sent or not
            if self.checkAddAttachment.isChecked():
                attachment = 'test_platform.png'
            else:
                attachment = ''

            worker = qt_thread.Worker(notifications.Notifications().send, self.lineEmailAddress.text(), 'test',
                                      attachment, self.lineUsername.text())
            worker.signals.finished.connect(self.send_test_email_finished)
            self.threadpool.start(worker)

    def send_test_email_finished(self):
        """Open a message box with a send test confirmation message"""

        self.pushCreate.setEnabled(True)
        self.pushCancel.setEnabled(True)

        send_test_confirmation = QMessageBox(self)
        send_test_confirmation.setWindowTitle('Send Test Email')
        send_test_confirmation.setIcon(QMessageBox.Information)
        send_test_confirmation.setText('A test notification email has been sent to %s at %s.' %
                                       (self.lineUsername.text(), self.lineEmailAddress.text()))
        send_test_confirmation.exec_()

    def create(self):
        """Saves important selection options to the build's settings file and closes the window"""

        # First check if the set build settings file already exists and open a message box if it does
        if os.path.isfile(self.lineBuildFile.text()) and not self.open_flag and not self.settings_flag:
            # Open an error message box and wait for user input
            exist_error = QMessageBox(self)
            exist_error.setWindowTitle('Confirm Save As')
            exist_error.setIcon(QMessageBox.Warning)
            exist_error.setText('%s already exists.\nDo you want to replace it?' % 
                                         os.path.basename(self.lineBuildFile.text()))
            exist_error.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            retval = exist_error.exec_()

            # If the user clicked No, open the Save As dialog to allow the user to change the name
            if retval != 16384:
                self.save_file()

        # Save all the entered information to the settings file
        # If the user didn't enter anything into the following fields, save the placeholder text instead
        if self.lineBuildName.text():
            self.build['BuildInfo']['Name'] = self.lineBuildName.text()
        else:
            self.build['BuildInfo']['Name'] = self.lineBuildName.placeholderText()

        if self.lineUsername.text():
            self.build['BuildInfo']['Username'] = self.lineUsername.text()
        else:
            self.build['BuildInfo']['Username'] = self.lineUsername.placeholderText()

        if self.lineEmailAddress.text():
            self.build['BuildInfo']['EmailAddress'] = self.lineEmailAddress.text()
        else:
            self.build['BuildInfo']['EmailAddress'] = self.lineEmailAddress.placeholderText()

        self.build['BuildInfo']['Folder'] = self.lineImageFolder.text()
        self.build['Filename'] = self.lineBuildFile.text()

        # Check if the entered email address is valid by using the external validation module
        if not validate_email(self.build['BuildInfo']['EmailAddress']):
            # Open an error message box and exit the method
            missing_folder_error = QMessageBox(self)
            missing_folder_error.setWindowTitle('Error')
            missing_folder_error.setIcon(QMessageBox.Critical)
            missing_folder_error.setText('Invalid email address. Please enter a valid email address.')
            missing_folder_error.exec_()
            return

        # If a New Build is being created (rather than Open Build or Settings), create folders to store images
        if not self.open_flag and not self.settings_flag:
            # Create respective sub-directories for images (and reports)
            os.makedirs('%s/raw/coat' % self.lineImageFolder.text())
            os.makedirs('%s/raw/scan' % self.lineImageFolder.text())
            os.makedirs('%s/raw/snapshot' % self.lineImageFolder.text())
            os.makedirs('%s/fixed/coat' % self.lineImageFolder.text())
            os.makedirs('%s/fixed/scan' % self.lineImageFolder.text())
            os.makedirs('%s/fixed/snapshot' % self.lineImageFolder.text())
            os.makedirs('%s/defects/coat/streaks' % self.lineImageFolder.text())
            os.makedirs('%s/defects/coat/chatter' % self.lineImageFolder.text())
            os.makedirs('%s/defects/coat/patches' % self.lineImageFolder.text())
            os.makedirs('%s/defects/coat/outliers' % self.lineImageFolder.text())
            os.makedirs('%s/defects/scan/streaks' % self.lineImageFolder.text())
            os.makedirs('%s/defects/scan/chatter' % self.lineImageFolder.text())
            os.makedirs('%s/defects/scan/pattern' % self.lineImageFolder.text())
            os.makedirs('%s/contours' % self.lineImageFolder.text())
            os.makedirs('%s/reports' % self.lineImageFolder.text())

            # Create combined and background blank json reports and save them to the build reports folder
            with open('%s/reports/combined_report.json' % self.lineImageFolder.text(), 'w+') as report:
                json.dump(dict(), report)
            with open('%s/reports/background_report.json' % self.lineImageFolder.text(), 'w+') as report:
                json.dump(dict(), report)
        else:
            # Check if the folder containing the images exist if a build was opened
            if not os.path.isdir(self.lineImageFolder.text()):
                missing_folder_error = QMessageBox(self)
                missing_folder_error.setWindowTitle('Error')
                missing_folder_error.setIcon(QMessageBox.Critical)
                missing_folder_error.setText('Image Folder not found.\nPlease reselect the correct image folder.\n\n'
                                             'Note: Selecting the wrong folder will result in incorrect behavior.')
                missing_folder_error.exec_()

                # Call the browse_folder method, allowing the user to reselect the correct image folder
                self.browse_folder()
                return

        # Save the newly created (or loaded) build to both the local build.json file and the set build file
        with open('build.json', 'w+') as build:
            json.dump(self.build, build, indent=4, sort_keys=True)
        with open(self.lineBuildFile.text(), 'w+') as build:
            json.dump(self.build, build, indent=4, sort_keys=True)

        # Close the dialog window and return True
        self.done(True)


class Preferences(QDialog, dialogPreferences.Ui_dialogPreferences):
    """Module used to initiate the modal Preferences dialog window
    Allows the user to change a bunch of settings in regards to the main interface and a few of the dialog windows
    """

    def __init__(self, parent=None):

        # Setup Dialog UI with MainWindow as parent and restore the previous window state
        super(Preferences, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)

        # Disallow the user from resizing the dialog window
        self.setFixedSize(self.size())
        self.window_settings = QSettings('MCAM', 'Defect Monitor')

        # Restoring the window state needs to go into a try loop as the first time the program is run on a new system
        # There won't be any stored settings and the function throws a TypeError
        try:
            self.restoreGeometry(self.window_settings.value('Preferences Geometry', ''))
        except TypeError:
            pass

        with open('config.json') as config:
            self.config = json.load(config)

        # Setup event listeners for all the relevant UI components, and connect them to specific functions
        self.pushBrowseBF.clicked.connect(self.browse_folder)
        self.pushApply.clicked.connect(self.apply)

        # Set all settings to to previously saved values
        self.lineBuildFolder.setText(self.config['BuildFolder'])
        self.spinSize.setValue(self.config['Gridlines']['Size'])
        self.spinThickness.setValue(self.config['Gridlines']['Thickness'])
        self.spinIdleTimeout.setValue(self.config['IdleTimeout'] / 60)
        self.spinContourT.setValue(self.config['SliceConverter']['ContourT'])
        self.spinCentrelineT.setValue(self.config['SliceConverter']['CentrelineT'])
        self.spinROIOffset.setValue(self.config['SliceConverter']['ROIOffset'])
        self.radioPixel.setChecked(self.config['SliceConverter']['Units'] == 'px')
        self.radioMillimetre.setChecked(self.config['SliceConverter']['Units'] == 'mm')
        self.checkKeepRaw.setChecked(self.config['KeepRaw'])
        self.doubleScaleFactor.setValue(self.config['ImageCorrection']['ScaleFactor'])
        self.lineSenderAddress.setText(self.config['Notifications']['Sender'])
        self.linePassword.setText(self.config['Notifications']['Password'])
        self.lineBuildName.setText(self.config['Defaults']['BuildName'])
        self.lineUsername.setText(self.config['Defaults']['Username'])
        self.lineEmailAddress.setText(self.config['Defaults']['EmailAddress'])

        # Set the maximum range of the grid size spinbox
        self.spinSize.setMaximum(int(self.config['ImageCorrection']['ImageResolution'][0] / 2))
        self.spinSize.setToolTip('5 - %s' % int(self.config['ImageCorrection']['ImageResolution'][0] / 2))

        # Setup event listeners for all the setting boxes to detect a change in an entered value
        for element in self.findChildren(QSpinBox):
            element.valueChanged.connect(self.apply_enable)
        for element in self.findChildren(QLineEdit):
            element.textChanged.connect(self.apply_enable)
        self.radioPixel.toggled.connect(self.apply_enable)
        self.doubleScaleFactor.valueChanged.connect(self.apply_enable)
        self.checkKeepRaw.toggled.connect(self.apply_enable)

        # Flag used to indicate whether to reload the config.json file within the Main Window
        self.reload_flag = False

    def browse_folder(self):
        """Prompts the user to select the folder containing all the build images"""

        folder = QFileDialog.getExistingDirectory(self, 'Browse...', '')

        if folder:
            self.lineBuildFolder.setText(folder)

    def redraw_gridlines(self, size, thickness):
        """Redraws the gridlines .png image with a new gridlines image using the updated settings"""

        # Grab the image resolution to be used for the gridlines
        width = self.config['ImageCorrection']['ImageResolution'][1]
        height = self.config['ImageCorrection']['ImageResolution'][0]

        # Create a blank black RGB image to draw the gridlines on
        image = np.zeros((height, width, 3), np.uint8)

        # Draw all the horizontal Lines
        for index in range(int(np.ceil(height / 2 / size))):
            cv2.line(image, (0, height // 2 + index * size), (width, height // 2 + index * size),
                     (255, 255, 255), thickness)
            cv2.line(image, (0, height // 2 - index * size), (width, height // 2 - index * size),
                     (255, 255, 255), thickness)

        # Draw all the vertical lines
        for index in range(int(np.ceil(width / 2 / size))):
            cv2.line(image, (width // 2 + index * size, 0), (width // 2 + index * size, height),
                     (255, 255, 255), thickness)
            cv2.line(image, (width // 2 - index * size, 0), (width // 2 - index * size, height),
                     (255, 255, 255), thickness)

        # Save the newly drawn gridlines image
        cv2.imwrite('gridlines.png', image)

    def apply_enable(self):
        """Enable the Apply button on any change of settings"""
        self.pushApply.setEnabled(True)

    def apply(self):
        """Executes when the Apply or OK button is clicked and saves the entered values to the config.json file"""

        size = self.spinSize.value()
        thickness = self.spinThickness.value()

        # If the either the gridlines size or thickness has changed, redraw the gridlines image
        if size != self.config['Gridlines']['Size'] or thickness != self.config['Gridlines']['Thickness']:
            self.redraw_gridlines(size, thickness)
            self.config['Gridlines']['Size'] = size
            self.config['Gridlines']['Thickness'] = thickness

        # Save the new values from the changed settings to the config dictionary
        self.config['BuildFolder'] = self.lineBuildFolder.text()
        self.config['IdleTimeout'] = self.spinIdleTimeout.value() * 60
        self.config['SliceConverter']['ContourT'] = self.spinContourT.value()
        self.config['SliceConverter']['CentrelineT'] = self.spinCentrelineT.value()
        self.config['SliceConverter']['ROIOffset'] = self.spinROIOffset.value()
        self.config['KeepRaw'] = self.checkKeepRaw.isChecked()
        self.config['ImageCorrection']['ScaleFactor'] = self.doubleScaleFactor.value()
        self.config['Notifications']['Sender'] = self.lineSenderAddress.text()
        self.config['Notifications']['Password'] = self.linePassword.text()
        self.config['Defaults']['BuildName'] = self.lineBuildName.text()
        self.config['Defaults']['Username'] = self.lineUsername.text()
        self.config['Defaults']['EmailAddress'] = self.lineEmailAddress.text()

        # Save the units depending on the checked radio box
        if self.radioPixel.isChecked():
            self.config['SliceConverter']['Units'] = 'px'
        else:
            self.config['SliceConverter']['Units'] = 'mm'

        with open('config.json', 'w+') as config:
            json.dump(self.config, config, indent=4, sort_keys=True)

        # Allow the Main Window to reload the config.json file
        self.reload_flag = True

        # Disable the Apply button until another setting is changed
        self.pushApply.setEnabled(False)

    def accept(self):
        """If the settings have changed, the apply function is executed before closing the window"""

        if self.pushApply.isEnabled():
            self.apply()

        # Close the dialog window and return the state of the reload flag
        self.done(self.reload_flag)

    def closeEvent(self, event):
        """Saves the current window position and size to the registry"""
        self.window_settings.setValue('Preferences Geometry', self.saveGeometry())


class CameraSettings(QDialog, dialogCameraSettings.Ui_dialogCameraSettings):
    """Module used to initiate the modal Camera Settings dialog window
    Allows the user to change camera settings which will be applied to the camera before images are captured
    """

    def __init__(self, parent=None):

        # Setup Dialog UI with MainWindow as parent and restore the previous window state
        super(CameraSettings, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)
        #self.setFixedSize(self.size())
        self.window_settings = QSettings('MCAM', 'Defect Monitor')

        try:
            self.restoreGeometry(self.window_settings.value('Camera Settings Geometry', ''))
        except TypeError:
            pass

        # Load from the config.json file
        with open('config.json') as config:
            self.config = json.load(config)

        # Setup event listeners for all the relevant UI components, and connect them to specific functions
        self.pushApply.clicked.connect(self.apply)

        # Set the combo box and settings to the previously saved values
        # Combo box settings are saved as their index values in the config.json file
        self.comboPixelFormat.setCurrentIndex(int(self.config['CameraSettings']['PixelFormat']))
        self.spinGain.setValue(self.config['CameraSettings']['Gain'])
        self.spinBlackLevel.setValue(self.config['CameraSettings']['BlackLevel'])
        self.spinExposureTime.setValue(int(self.config['CameraSettings']['ExposureTime']))
        self.spinPacketSize.setValue(int(self.config['CameraSettings']['PacketSize']))
        self.spinInterPacketDelay.setValue(int(self.config['CameraSettings']['InterPacketDelay']))
        self.spinFrameDelay.setValue(int(self.config['CameraSettings']['FrameDelay']))
        self.spinTriggerTimeout.setValue(int(self.config['CameraSettings']['TriggerTimeout']))

        # Setup event listeners for all the setting boxes to detect a change in an entered value
        self.comboPixelFormat.currentIndexChanged.connect(self.apply_enable)
        for element in self.findChildren(QSpinBox):
            element.valueChanged.connect(self.apply_enable)

    def apply_enable(self):
        """Enable the Apply button on any change of settings"""
        self.pushApply.setEnabled(True)

    def apply(self):
        """Executes when the Apply or OK button is clicked and saves the entered values to the config.json file"""

        # Save the new values from the changed settings to the config dictionary
        self.config['CameraSettings']['PixelFormat'] = self.comboPixelFormat.currentIndex()
        self.config['CameraSettings']['Gain'] = self.spinGain.value()
        self.config['CameraSettings']['BlackLevel'] = self.spinBlackLevel.value()
        self.config['CameraSettings']['ExposureTime'] = self.spinExposureTime.value()
        self.config['CameraSettings']['PacketSize'] = self.spinPacketSize.value()
        self.config['CameraSettings']['InterPacketDelay'] = self.spinInterPacketDelay.value()
        self.config['CameraSettings']['FrameTransmissionDelay'] = self.spinFrameDelay.value()
        self.config['CameraSettings']['TriggerTimeout'] = self.spinTriggerTimeout.value()

        with open('config.json', 'w+') as config:
            json.dump(self.config, config, indent=4, sort_keys=True)

        # Disable the Apply button until another setting is changed
        self.pushApply.setEnabled(False)

    def accept(self):
        """If the settings have changed, the apply function is executed before closing the window"""

        if self.pushApply.isEnabled():
            self.apply()

        self.done(True)

    def closeEvent(self, event):
        """Saves the current window position and size to the registry"""
        self.window_settings.setValue('Camera Settings Geometry', self.saveGeometry())


class CameraCalibration(QDialog, dialogCameraCalibration.Ui_dialogCameraCalibration):
    """Module used to initiate the modal Camera Calibration dialog window
    Allows the user to select a bunch of chessboard images to calculate the camera's intrinsic values
    These values are to be used to fix the distortion and perspective in the raw captured images
    """

    def __init__(self, parent=None):

        # Setup Dialog UI with MainWindow as parent and restore the previous window state
        super(CameraCalibration, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)
        self.window_settings = QSettings('MCAM', 'Defect Monitor')

        try:
            self.restoreGeometry(self.window_settings.value('Camera Calibration Geometry', ''))
        except TypeError:
            pass

        with open('config.json') as config:
            self.config = json.load(config)

        # Setup event listeners for all the relevant UI components, and connect them to specific functions
        self.pushAdd.clicked.connect(self.add_images)
        self.pushRemove.clicked.connect(self.remove_images)
        self.pushBrowseHI.clicked.connect(self.browse_homography)
        self.pushBrowseTI.clicked.connect(self.browse_test)
        self.pushCropImage.clicked.connect(self.crop_image)
        self.pushViewResults.clicked.connect(lambda: self.view_results(self.config['ImageCorrection']))
        self.pushSaveResults.clicked.connect(self.save_results)
        self.pushStart.clicked.connect(self.start)

        # Set the SpinBox settings to the previously saved values
        self.spinWidth.setValue(self.config['CameraCalibration']['Width'])
        self.spinHeight.setValue(self.config['CameraCalibration']['Height'])
        self.spinWidthHI.setValue(self.config['CameraCalibration']['WidthHI'])
        self.spinHeightHI.setValue(self.config['CameraCalibration']['HeightHI'])
        self.spinRatio.setValue(self.config['CameraCalibration']['DownscalingRatio'])
        self.spinTLX.setValue(self.config['ImageCorrection']['CropOffset'][1])
        self.spinTLY.setValue(self.config['ImageCorrection']['CropOffset'][0])
        self.spinResolutionX.setValue(self.config['ImageCorrection']['ImageResolution'][1])
        self.spinResolutionY.setValue(self.config['ImageCorrection']['ImageResolution'][0])

        # Set and display previously saved image path names if they exist, otherwise leave empty strings
        if os.path.isfile(self.config['CameraCalibration']['HomographyImage']):
            self.lineHomographyImage.setText(os.path.basename(self.config['CameraCalibration']['HomographyImage']))
        if os.path.isfile(self.config['CameraCalibration']['TestImage']):
            self.lineTestImage.setText(os.path.basename(self.config['CameraCalibration']['TestImage']))
            self.checkApply.setEnabled(True)

        # Initiate the image list
        self.image_list = list()

        self.threadpool = QThreadPool()

    def add_images(self):
        """Add additional selected images to the image list"""

        filenames = QFileDialog.getOpenFileNames(self, 'Add Images...', '', 'Image Files (*.png)')[0]

        if filenames:
            # Check if any of the selected files are already in the image list and only add the ones which aren't
            for file in filenames:
                if file not in self.image_list:
                    # Append the new images to the image list and the QListWidget
                    self.image_list.append(file)
                    self.listImages.addItem(os.path.basename(file).replace('.png', ''))

            # Enable the start button (if the other conditions are met)
            self.enable_start()

    def remove_images(self):
        """Remove selected images from the image list"""

        # Grab the list of selected images in the QListWidget
        for item in self.listImages.selectedItems():
            # Delete the corresponding image from the image list using the row index of the image
            # The internal list and the QListWidget should always have the exact same ordering of elements
            del self.image_list[self.listImages.row(item)]
            self.listImages.takeItem(self.listImages.row(item))

        self.enable_start()

    def browse_homography(self):
        """Prompts the user to select an homography image used to calculate the homography matrix"""

        filename = QFileDialog.getOpenFileName(self, 'Browse...', '', 'Image File (*.png)')[0]

        if filename:
            # Add the filename to the config.json file and set the name in the box
            self.config['CameraCalibration']['HomographyImage'] = filename
            self.lineHomographyImage.setText(os.path.basename(self.config['CameraCalibration']['HomographyImage']))
            self.enable_start()

    def browse_test(self):
        """Prompts the user to select a test image used to test calibration results"""

        filename = QFileDialog.getOpenFileName(self, 'Browse...', '', 'Image File (*.png)')[0]

        if filename:
            self.config['CameraCalibration']['TestImage'] = filename
            self.lineTestImage.setText(os.path.basename(self.config['CameraCalibration']['TestImage']))
            self.checkApply.setEnabled(True)

    def start(self):
        """Start the calibration process after saving the calibration settings to config.json file"""

        # Disable relevant UI elements to prevent concurrent processes
        self.toggle_control(False)
        self.pushStart.setEnabled(False)
        self.pushSaveResults.setEnabled(False)

        # Save calibration settings
        self.save_settings()

        # Reset the colours of the items in the QListWidget
        # Try exception causes this function to be skipped if the background of a line is already white
        for index in range(self.listImages.count()):
            try:
                self.listImages.item(index).setBackground(QColor('white'))
            except AttributeError:
                continue

        worker = qt_thread.Worker(camera_calibration.Calibration().calibrate, self.image_list,
                                  self.config['CameraCalibration'], self.config['ImageCorrection'])
        worker.signals.status.connect(self.update_status)
        worker.signals.progress.connect(self.update_progress)
        worker.signals.colour.connect(self.change_colour)
        worker.signals.result.connect(self.start_finished)
        self.threadpool.start(worker)

    def start_finished(self, parameters):
        """Executes when the CameraCalibration instance has finished"""

        # Re-enable relevant UI elements
        self.toggle_control(True)
        self.pushSaveResults.setEnabled(bool(parameters))

        # Open the Calibration Results window to display the results only if the entire calibration was successful
        if parameters:
            # Save the calculated parameters as instance variables to be used if the user wants to save the results
            self.parameters = parameters
            self.view_results(parameters)

            # Enable the Crop Test Image button only if the test image has been fixed
            if self.checkApply.isChecked():
                self.pushCropImage.setEnabled(True)

    def toggle_control(self, flag):
        """Enables or disables the following elements in one fell swoop depending on the received flag"""
        self.pushAdd.setEnabled(flag)
        self.pushRemove.setEnabled(flag)
        self.pushBrowseHI.setEnabled(flag)
        self.pushBrowseTI.setEnabled(flag)
        self.groupCalibrationSettings.setEnabled(flag)
        self.groupCropSettings.setEnabled(flag)
        self.pushDone.setEnabled(flag)

    def crop_image(self):
        """Crops the test image down to the entered region of interest"""

        image = cv2.imread(self.config['CameraCalibration']['TestImage'].replace('.png', '_DP.png'))

        offset = [self.spinTLY.value(), self.spinTLX.value()]
        resolution = [self.spinResolutionY.value(), self.spinResolutionX.value()]

        if type(image) is np.ndarray:
            image = image_processing.ImageFix().crop(image, offset, resolution)
            cv2.imwrite(self.config['CameraCalibration']['TestImage'].replace('.png', '_DPC.png'), image)
            os.startfile(self.config['CameraCalibration']['TestImage'].replace('.png', '_DPC.png'))
            self.update_status('Test image cropped.')
        else:
            self.update_status('Fixed test image cannot be found.')
            self.pushCropImage.setEnabled(False)

    def view_results(self, parameters):
        """Opens the Calibration Results window to displays the results of the camera calibration to the user"""

        try:
            self.CR_dialog.close()
        except (AttributeError, RuntimeError):
            pass

        self.CR_dialog = CalibrationResults(self, parameters)
        self.CR_dialog.show()

    def save_results(self):
        """Saves the calculated results including the crop area to the config.json file"""

        self.parameters['CropOffset'][1] = self.spinTLX.value()
        self.parameters['CropOffset'][0] = self.spinTLY.value()
        self.parameters['ImageResolution'][1] = self.spinResolutionX.value()
        self.parameters['ImageResolution'][0] = self.spinResolutionY.value()

        # Copy the results dictionary into the config dictionary
        self.config['ImageCorrection'] = self.parameters.copy()

        # Save to the config.json file and disable saving again
        self.save_settings()
        self.pushSaveResults.setEnabled(False)
        self.update_status('Calibration results saved to the config file.')

    def change_colour(self, index, valid):
        """Changes the background colour of the received item in the listImages box
        Changes to green if image is valid, red if image is invalid for calibration
        """

        if valid:
            self.listImages.item(index).setBackground(QColor('green'))
        else:
            self.listImages.item(index).setBackground(QColor('red'))

    def enable_start(self):
        """(Re-)Enables the Start button if valid calibration images and an homography image have been selected"""

        self.pushStart.setEnabled(bool(self.image_list) and bool(self.lineHomographyImage.text()))
        self.pushCropImage.setEnabled(False)

        # These conditionals just determine which status message to display
        if self.image_list and self.lineHomographyImage.text():
            self.update_status('Waiting to start process.')
        elif self.image_list:
            self.update_status('Select homography image.')
        else:
            self.update_status('Add calibration images.')

    def save_settings(self):
        """Saves the entered settings so that they persist across instances of the application"""

        self.config['CameraCalibration']['Width'] = self.spinWidth.value()
        self.config['CameraCalibration']['Height'] = self.spinHeight.value()
        self.config['CameraCalibration']['WidthHI'] = self.spinWidthHI.value()
        self.config['CameraCalibration']['HeightHI'] = self.spinHeightHI.value()
        self.config['CameraCalibration']['DownscalingRatio'] = self.spinRatio.value()
        self.config['CameraCalibration']['Chessboard'] = self.checkSaveC.isChecked()
        self.config['CameraCalibration']['Undistort'] = self.checkSaveU.isChecked()
        self.config['CameraCalibration']['Apply'] = self.checkApply.isChecked()

        with open('config.json', 'w+') as config:
            json.dump(self.config, config, indent=4, sort_keys=True)

    def update_status(self, string):
        self.labelStatus.setText(string)

    def update_progress(self, percentage):
        self.progressBar.setValue(int(percentage))

    def closeEvent(self, event):
        """Saves the settings and current window position and size to the registry"""
        self.save_settings()
        self.window_settings.setValue('Camera Calibration Geometry', self.saveGeometry())


class CalibrationResults(QDialog, dialogCalibrationResults.Ui_dialogCalibrationResults):
    """Module used to initiate the modeless Calibration Results dialog window
    Displays the calibration parameters and results in an easy to read window
    """

    def __init__(self, parent=None, parameters=None):

        # Setup Dialog UI with CameraCalibration as parent and restore the previous window state
        super(CalibrationResults, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)
        self.window_settings = QSettings('MCAM', 'Defect Monitor')

        try:
            self.restoreGeometry(self.window_settings.value('Calibration Results Geometry', ''))
        except TypeError:
            pass

        # Split camera parameters into their own respective values to be used in OpenCV functions
        camera_matrix = np.array(parameters['CameraMatrix'])
        distortion_coefficients = np.array(parameters['DistortionCoefficients'])
        homography_matrix = np.array(parameters['HomographyMatrix'])

        # Set all the table columns and rows to automatically resize appropriately
        for table in self.findChildren(QTableWidget):
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Nested for loops to access each of the table boxes in order
        for row in range(3):
            for column in range(3):
                # Setting the item using the corresponding index of the matrix arrays
                self.tableCM.setItem(row, column, QTableWidgetItem(format(camera_matrix[row][column], '.10g')))
                self.tableHM.setItem(row, column, QTableWidgetItem(format(homography_matrix[row][column], '.10g')))

                # Because the distortion coefficients matrix is a 1x5, a slight modification needs to be made
                # Exception used to ignore the 2x3 box and 3rd row of the matrix
                if row >= 1:
                    column += 3
                try:
                    self.tableDC.setItem(row, column % 3, QTableWidgetItem(
                        format(distortion_coefficients[0][column], '.10g')))
                except (ValueError, IndexError):
                    pass

        # Sets the row height to as small as possible to fit the text height
        self.tableCM.resizeRowsToContents()
        self.tableDC.resizeRowsToContents()
        self.tableHM.resizeRowsToContents()

        # Displaying the re-projection error on the appropriate text label
        self.labelRMS.setText('Re-Projection Error: ' + format(parameters['RMS'], '.10g'))

    def closeEvent(self, event):
        """Saves the current window position and size to the registry"""
        self.window_settings.setValue('Calibration Results Geometry', self.saveGeometry())


class StressTest(QDialog, dialogStressTest.Ui_dialogStressTest):
    """Module used to iniaite teh modal Stress Test dialog window
    Allows the user to stress test the attached camera by indefinitely capturing images repeatedly
    """

    def __init__(self, parent=None):

        super(StressTest, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)
        self.setFixedSize(self.size())
        self.window_settings = QSettings('MCAM', 'Defect Monitor')

        try:
            self.restoreGeometry(self.window_settings.value('Stress Test Geometry', ''))
        except TypeError:
            pass

        self.pushStart.clicked.connect(self.start_test)
        self.threadpool = QThreadPool()

    def start_test(self):

        if 'Start' in self.pushStart.text():
            # Disable UI elements to prevent concurrent processes
            self.spinInterval.setEnabled(False)
            self.pushDone.setEnabled(False)

            # Create a temporary folder within the root directory to store the captured images
            self.folder = os.getcwd().replace('\\', '/') + '/stress'
            if not os.path.isdir(self.folder):
                os.makedirs(self.folder)

            self.layer = 1
            self.interval = self.spinInterval.value()

            self.pushStart.setText('Stop')

            # Reset the elapsed time, initialize display time to 0 and create and start the QTimer
            self.stopwatch_elapsed = 0
            self.update_time()
            self.timer_stopwatch = QTimer()
            self.timer_stopwatch.timeout.connect(self.update_time)
            self.timer_stopwatch.start(1000)

            self.test_loop()
        elif 'Stop' in self.pushStart.text():
            self.pushStart.setText('Start')
            self.pushStart.setEnabled(False)

    def test_loop(self):
        worker = qt_thread.Worker(image_capture.ImageCapture().capture_snapshot, self.layer, self.folder,
                                  self.config['CameraSettings'])
        worker.signals.status_camera.connect(self.update_status)
        worker.signals.finished.connect(self.test_done)
        self.threadpool.start(worker)

    def test_done(self):

        self.labelNumber.setText(str(self.layer).zfill(4))
        self.layer += 1

        self.timer_interval = QTimer()
        self.timer_interval.timeout.connect(self.test_interval)
        self.timer_interval.start(1000)

    def test_interval(self):
        self.update_status('Timeout: %ss' % self.interval)
        self.interval -= 1

        if 'Start' in self.pushStart.text():
            self.timer_stopwatch.stop()
            self.timer_interval.stop()
            self.test_exit()
            return

        if self.interval < 0:
            self.timer_interval.stop()
            self.interval = self.spinInterval.value()
            self.test_loop()

    def test_exit(self):
        self.pushStart.setEnabled(True)
        self.spinInterval.setEnabled(True)
        self.pushDone.setEnabled(True)

        # Delete the entire temporary folder and all its contents
        shutil.rmtree('stress')

        self.update_status('Waiting')

    def update_time(self):
        self.stopwatch_elapsed += 1
        seconds = str(self.stopwatch_elapsed % 60).zfill(2)
        minutes = str(self.stopwatch_elapsed % 3600 // 60).zfill(2)
        hours = str(self.stopwatch_elapsed // 3600).zfill(2)
        self.labelElapsedTime.setText('%s:%s:%s' % (hours, minutes, seconds))

    def update_status(self, string):

        self.labelStatus.setText(string)

        if 'Error' in string:
            self.start_test()

            # Send a camera notification to the developer
            worker = qt_thread.Worker(notifications.Notifications().send, 'nicholascklee@gmail.com', 'camera')
            self.threadpool.start(worker)

    def closeEvent(self, event):
        """Saves the current window position and size to the registry"""
        self.window_settings.setValue('Stress Test Geometry', self.saveGeometry())


class SliceConverter(QDialog, dialogSliceConverter.Ui_dialogSliceConverter):
    """Module used to initiate the modal Slice Converter dialog window
    Allows the user to convert .cli files into ASCII encoded scaled contours and draws them using OpenCV
    Also contains a real-time preview and modification of said contours before drawing
    """

    def __init__(self, parent=None):

        super(SliceConverter, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.Window)
        self.setupUi(self)
        self.window_settings = QSettings('MCAM', 'Defect Monitor')

        try:
            self.restoreGeometry(self.window_settings.value('Slice Converter Geometry', ''))
        except TypeError:
            pass

        with open('build.json') as build:
            self.build = json.load(build)

        with open('config.json') as config:
            self.config = json.load(config)

        # Setup event listeners for all the relevant UI components, and connect them to specific functions
        # Buttons
        self.pushAddSF.clicked.connect(self.add_files)
        self.pushRemoveSF.clicked.connect(self.remove_files)
        self.pushDrawContours.clicked.connect(self.draw_setup)
        self.pushZoomIn.clicked.connect(self.zoom_in)
        self.pushZoomOut.clicked.connect(self.zoom_out)
        self.pushGo.clicked.connect(self.set_slice)
        self.pushSelect.clicked.connect(self.select_roi)
        self.pushRemove.clicked.connect(self.remove_roi)
        self.pushSet.clicked.connect(lambda: self.set_roi(0, True))
        self.pushRotate.clicked.connect(self.rotate)
        self.pushResetR.clicked.connect(self.rotate_reset)
        self.pushTranslate.clicked.connect(self.translate)
        self.pushResetT.clicked.connect(self.translate_reset)
        self.pushPause.clicked.connect(self.pause)
        self.pushBrowseCB.clicked.connect(self.browse_background)
        self.pushBrowseOF.clicked.connect(self.browse_output)

        # Checkboxes
        self.checkCentrelines.toggled.connect(lambda: self.preview_contours(0))
        self.checkFillContours.toggled.connect(lambda: self.preview_contours(0))
        self.checkBackground.toggled.connect(self.set_background)

        # Spinboxes
        self.spinRangeLow.valueChanged.connect(self.set_minimum)
        self.spinRangeHigh.valueChanged.connect(self.set_maximum)

        # Display
        self.listSliceFiles.itemSelectionChanged.connect(self.select_parts)
        self.graphicsDisplay.mouse_pos.connect(self.update_position)
        self.graphicsDisplay.zoom_done.connect(self.zoom_done)
        self.graphicsDisplay.roi_done.connect(self.set_roi)

        # Initiate a bunch of values
        self.contour_dict = dict()
        self.part_colours = dict()
        self.part_transform = dict()
        self.slice_list = list()
        self.selected_items = list()
        self.current_layer = 1
        self.convert_run_flag = False
        self.draw_run_flag = False
        self.millimetre_flag = 'mm' in self.config['SliceConverter']['Units']
        self.roi = self.build['ROI']

        # This value is used to indicate which process is active, used for the pause button and for exiting the window
        # 0 - None / 1 - Convert / 2 - Draw
        self.active_process = 0

        # Set the row height to fit the table size
        self.tableTransform.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Check if a build is open by checking for an image folder, otherwise set a 'default' output folder
        if self.build['BuildInfo']['Folder']:
            self.output_folder = self.build['BuildInfo']['Folder'] + '/contours'
            self.slice_list = self.build['SliceConverter']['Files'][:]
            self.part_transform = self.build['SliceConverter']['Transform'].copy()

            # Check if there are parts in the current build (if reopening a saved build)
            # Done by checking anything exists in the slice list, and disable the auto-set and display the stored ROI
            if self.slice_list:
                self.checkAutoSet.setChecked(False)
                self.set_roi_display(self.build['ROI'][1::])

            # Initialize the colour dictionary for the pre-selected parts
            for file in self.slice_list:
                self.part_colours[os.path.basename(file).replace('.cli', '')] = (255, 0, 0)
        else:
            self.output_folder = os.path.dirname(os.getcwd().replace('\\', '/')) + '/Contours'

        # Change the displayed units on the dialog window from pixel <-> millimetres depending on the config setting
        self.labelXUnits.setText(self.config['SliceConverter']['Units'])
        self.labelYUnits.setText(self.config['SliceConverter']['Units'])
        self.labelTLUnits.setText(self.config['SliceConverter']['Units'])
        self.labelResUnits.setText(self.config['SliceConverter']['Units'])
        self.labelUnits.setText(self.config['SliceConverter']['Units'])

        # Preset the Mouse Position numbers to millimetre format
        if self.millimetre_flag:
            self.labelXPosition.setText('X  000.00')
            self.labelYPosition.setText('Y  000.00')

        self.lineOutputFolder.setText(self.output_folder)

        self.threadpool = QThreadPool()

        # Set up the display with a 'blank' platform
        self.check_files()

    def add_files(self):
        """Add additional selected slice files to the slice file list"""

        filenames = QFileDialog.getOpenFileNames(self, 'Add Slice Files...', '', 'Slice Files (*.cli)')[0]

        if filenames:
            # Stop the selecting of files in the list from doing anything
            self.listSliceFiles.blockSignals(True)

            # Check if any of the selected files are already in the slice list and only add the ones which aren't
            for file in filenames:
                if file not in self.slice_list:
                    # Add the new parts to the slice list, colour dictionary and transform dictionary
                    self.slice_list.append(file)

                    # Part colours is a dictionary of each part's preview part colour
                    # Part transform is a dictionary of each part's transformation parameters
                    # Set all the preview part colours to blue for now
                    self.part_colours[os.path.basename(file).replace('.cli', '')] = (255, 0, 0)
                    self.part_transform[os.path.basename(file).replace('.cli', '')] = [0, 0, 0]

            # Check if all the slice files have been converted
            self.check_files()

    def check_files(self):
        """Check whether all the added slice files have been converted from .cli to ASCII contours"""

        # Sort the slice list and clear the QListWidget
        self.slice_list.sort()
        self.listSliceFiles.clear()

        self.index_list = list()
        self.slice_counter = 0
        self.max_layers = 1

        # Check if all of the selected .cli files have been converted
        for index, item in enumerate(self.slice_list):
            # Add the part names to the list window
            self.listSliceFiles.addItem(os.path.basename(item).replace('.cli', ''))
            if os.path.isfile(item.replace('.cli', '_contours.txt')):
                self.listSliceFiles.item(index).setBackground(QColor('yellow'))
            else:
                self.index_list.append(index)
                self.listSliceFiles.item(index).setBackground(QColor('red'))

        # Check if any of the slice files need to be converted at all
        if self.index_list:
            # Disable all the buttons to prevent the user from doing concurrent things
            self.toggle_control(1)
            self.pushDrawContours.setEnabled(False)
            self.convert_run_flag = True
            self.convert_slice(self.slice_list[self.index_list[self.slice_counter]])
        else:
            self.update_layer_ranges()
            if self.slice_list:
                self.preview_contours(self.config['SliceConverter']['ROIOffset'])
                self.toggle_control(2)
                self.pushDrawContours.setEnabled(True)
            else:
                self.preview_contours()

    def remove_files(self):
        """Remove selected slice files from the slice file list"""

        # Stop the selecting of files in the list from doing anything
        self.listSliceFiles.blockSignals(True)

        # Grab the list of selected items in the QListWidget
        for item in self.listSliceFiles.selectedItems():
            # Delete the corresponding file from the slice file list using the row index of the file
            del self.slice_list[self.listSliceFiles.row(item)]

            # Remove the part name's key from the dictionaries
            self.part_colours.pop(item.text(), None)
            self.part_transform.pop(item.text(), None)
            self.listSliceFiles.takeItem(self.listSliceFiles.row(item))

        # Check if the list is now empty, if so reset to button state 0
        if not self.slice_list:
            self.contour_dict = dict()
            self.pushDrawContours.setEnabled(False)
            self.toggle_control(0)

        self.update_layer_ranges()
        self.preview_contours(self.config['SliceConverter']['ROIOffset'])

    def convert_slice(self, slice_file):
        """Looping method to convert slice files"""

        self.active_process = 1

        worker = qt_thread.Worker(slice_converter.SliceConverter().convert_cli, slice_file,
                                  self.config['ImageCorrection']['ScaleFactor'])
        worker.signals.status.connect(self.update_status)
        worker.signals.progress.connect(self.update_progress)
        worker.signals.finished.connect(self.convert_slice_finished)
        self.threadpool.start(worker)

    def convert_slice_finished(self):
        self.listSliceFiles.item(self.index_list[self.slice_counter]).setBackground(QColor('yellow'))
        self.slice_counter += 1

        if self.convert_run_flag and not self.slice_counter == len(self.index_list):
            self.convert_slice(self.slice_list[self.index_list[self.slice_counter]])
        elif self.slice_counter == len(self.index_list):
            self.convert_run_flag = False
            self.pushDrawContours.setEnabled(True)
            self.toggle_control(2)
            self.update_layer_ranges()
            self.preview_contours(self.config['SliceConverter']['ROIOffset'])

    def draw_setup(self):
        """Setup to draw the contours"""

        # If a build has been created (has a name), show a warning before proceeding to draw contours
        if self.build['BuildInfo']['Name']:
            draw_confirmation = QMessageBox(self)
            draw_confirmation.setWindowTitle('Draw Contours')
            draw_confirmation.setIcon(QMessageBox.Warning)
            draw_confirmation.setText('Saving drawn contours to the build folder.\n\n'
                                      'Note that this will completely empty the build\'s contours folder and replace '
                                      'all of the defect reports with empty reports. All defect data will need to be '
                                      're-processed after re-drawing all the contours.\n\n'
                                      'Would you like to proceed to draw contours?')
            draw_confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            retval = draw_confirmation.exec_()

            # If the user clicked No, the method will end, otherwise it continues
            if retval == 16384:
                # Delete all the files in the build's contours folder and reports folder
                for filename in os.listdir(self.output_folder):
                    os.remove(self.output_folder + '/' + filename)

                for filename in os.listdir('%s/reports' % self.build['BuildInfo']['Folder']):
                    # Instead of deleting the combined and background reports, replace their contents with empty dicts
                    if 'combined' in filename or 'background' in filename:
                        with open('%s/reports/%s' % (self.build['BuildInfo']['Folder'], filename), 'w+') as report:
                            json.dump(dict(), report)
                        continue
                    os.remove('%s/reports/%s' % (self.build['BuildInfo']['Folder'], filename))
            else:
                return

        self.pushDrawContours.setEnabled(False)
        self.toggle_control(1)

        # Create the output folder if it doesn't already exist
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        # UI Progress
        self.progress_current = 0.0
        self.progress_previous = None
        self.update_progress(0)
        self.increment = 100 / (self.spinRangeHigh.value() + 1 - self.spinRangeLow.value())

        # Create a dictionary of colours (different shades of teal) for each part's contours and save it
        # These part colours don't affect past reports
        # At the same time, save a bunch of json files containing an empty dictionary to the build reports folder
        # These json files are used to store the defect coordinate and pixel size data for each of the parts
        part_colours = dict()

        for index, part_name in enumerate(self.part_colours.keys()):
            # Create the colours for each of the parts
            part_colours[part_name] = ((100 + index) % 255, (100 + index) % 255, 0)

            # Create the reports if a build has been created
            if self.build['BuildInfo']['Name']:
                with open('%s/reports/%s_report.json' % (self.build['BuildInfo']['Folder'], part_name), 'w+') as report:
                    json.dump(dict(), report)

        # Create a 'background' and 'combined' part colour and set them to black
        part_colours['background'] = (0, 0, 0)
        part_colours['combined'] = (0, 0, 0)

        # Set the starting layer to draw as the entered lower layer range (default is all the contours)
        self.contour_counter = self.spinRangeLow.value()
        self.draw_run_flag = True

        # Save the list of slice files, part colours, transformations, max layers and roi to the build.json file
        self.build['SliceConverter']['Files'] = self.slice_list
        self.build['SliceConverter']['Colours'] = part_colours
        self.build['SliceConverter']['Transform'] = self.part_transform
        self.build['SliceConverter']['MaxLayers'] = self.max_layers
        self.build['ROI'] = self.roi

        with open('build.json', 'w+') as build:
            json.dump(self.build, build, indent=4, sort_keys=True)

        # Start the draw loop
        # The names flag is only set on the first drawn layer so that the names image will only be created once
        self.draw_contours(self.contour_counter, True)

    def draw_contours(self, layer, names_flag=False):
        self.active_process = 2
        self.update_status('All | Drawing %s of %s.' % (str(layer).zfill(4), str(self.spinRangeHigh.value()).zfill(4)))

        # Create a blank black RGB image to draw the contours on
        image = np.zeros(tuple(self.config['ImageCorrection']['ImageResolution'] + [3]), np.uint8)

        worker = qt_thread.Worker(slice_converter.SliceConverter().draw_contours, self.contour_dict, image,
                                  layer, self.build['SliceConverter']['Colours'],
                                  self.build['SliceConverter']['Transform'], self.output_folder, -1, 0,
                                  names_flag, True)
        worker.signals.finished.connect(self.draw_contours_finished)
        self.threadpool.start(worker)

    def draw_contours_finished(self):
        self.contour_counter += 1

        self.progress_current += self.increment
        if round(self.progress_current) is not self.progress_previous:
            self.update_progress(round(self.progress_current))
            self.progress_previous = round(self.progress_current)

        if self.draw_run_flag and not self.contour_counter == (self.spinRangeHigh.value() + 1):
            self.draw_contours(self.contour_counter)
        elif self.contour_counter == (self.spinRangeHigh.value() + 1):
            self.draw_run_flag = False
            self.pushDrawContours.setEnabled(True)
            self.toggle_control(2)

    def set_background(self):
        if self.checkBackground.isChecked():
            if not self.lineBackground.text():
                if not self.browse_background():
                    self.checkBackground.setChecked(False)
            else:
                self.preview_contours()
        else:
            self.preview_contours()

    def browse_background(self):
        """Prompts the user to select an image to be used as the background"""

        filename = QFileDialog.getOpenFileName(self, 'Browse...', '', 'Image Files (*.png)')[0]

        if filename:
            self.image_background = cv2.imread(filename)
            self.lineBackground.setText(filename)
            self.preview_contours()
            return True
        else:
            return False

    def zoom_in(self):
        """Sets the display Graphics Viewer's zoom function on"""
        self.graphicsDisplay.zoom_flag = self.pushZoomIn.isChecked()

    def zoom_done(self):
        """Disables the zoom function and the checked status of the Zoom In action after performing a zoom action"""
        self.pushZoomIn.setChecked(False)
        self.graphicsDisplay.zoom_flag = False

    def zoom_out(self):
        """Resets the zoom state of the display Graphics Viewer"""
        self.graphicsDisplay.reset_image()

    def set_slice(self):
        """Changes the preview contour layer to the entered one"""
        self.current_layer = self.spinSliceNumber.value()
        self.labelSliceNumber.setText('%s / %s' % (str(self.current_layer).zfill(4), str(self.max_layers).zfill(4)))
        self.preview_contours()

    def set_minimum(self):
        """Sets the minimum value of the high range spinbox to the current low range spinbox's value"""
        self.spinRangeHigh.setMinimum(self.spinRangeLow.value())

    def set_maximum(self):
        """Sets the maximum value of the low range spinbox to the current high range spinbox's value"""
        self.spinRangeLow.setMaximum(self.spinRangeHigh.value())

    def select_roi(self):
        """Allows the user to select a region to crop the images for the defect processor"""
        self.graphicsDisplay.zoom_flag = self.pushSelect.isChecked()
        self.graphicsDisplay.roi_flag = self.pushSelect.isChecked()
        self.checkAutoSet.setChecked(False)

    def remove_roi(self):
        """Resets the selected region and removes the drawn rectangle from the preview screen"""
        self.roi[0] = 0
        self.checkAutoSet.setChecked(False)
        self.pushRemove.setEnabled(False)
        self.preview_contours()

    def set_roi(self, region, preview_flag):
        """Saves the received region to the build.json file and displays the ROI and region coordinates and size
        Also disables checked status of the Select button after successfully selecting a region"""

        if not bool(region):
            self.checkAutoSet.setChecked(False)
            region = [self.spinTLX.value(), self.spinTLY.value(),
                      self.spinResolutionX.value(), self.spinResolutionY.value()]

            # If units is set to millimetres, convert the entered millimetres to pixels
            if self.millimetre_flag:
                region = [round(item * self.config['ImageCorrection']['ScaleFactor']) for item in region]
        else:
            self.set_roi_display(region)

        self.pushRemove.setEnabled(True)
        self.pushSelect.setChecked(False)
        self.graphicsDisplay.roi_flag = False

        # The first element in the roi list is a flag used to signify that the roi is to be drawn and used
        self.roi = [1, region[0], region[1], region[0] + region[2], region[1] + region[3]]

        if preview_flag:
            self.preview_contours()

    def set_roi_display(self, region):
        """Display the selected region of interest values on the Dialog Window"""

        # If units is set to millimetres, convert the received pixels to millimetres only for the dialog display
        if self.millimetre_flag:
            region.extend([int(round(item / self.config['ImageCorrection']['ScaleFactor'])) for item in region])

        # If units is set to millimetres, use the above set indexes of converted values instead
        self.spinTLX.setValue(region[0 + 4 * int(self.millimetre_flag)])
        self.spinTLY.setValue(region[1 + 4 * int(self.millimetre_flag)])
        self.spinResolutionX.setValue(region[2 + 4 * int(self.millimetre_flag)])
        self.spinResolutionY.setValue(region[3 + 4 * int(self.millimetre_flag)])

    def rotate(self):
        """Applies rotation parameters to the part_transform dictionary for the selected parts"""

        for item in self.listSliceFiles.selectedItems():
            # Change the rotation parameter of the selected items to the entered ones
            self.part_transform[item.text()][2] += self.spinAngle.value() % 360

        self.preview_contours(self.config['SliceConverter']['ROIOffset'])

    def rotate_reset(self):
        """Resets the rotation parameters back to 0 for the selected parts"""

        for item in self.listSliceFiles.selectedItems():
            # Reset the rotation parameter of the selected items
            self.part_transform[item.text()][2] = 0

        self.preview_contours(self.config['SliceConverter']['ROIOffset'])

    def translate(self):
        """Applies translation parameters to the part_transform dictionary for the selected parts"""

        for item in self.listSliceFiles.selectedItems():
            # If the units are set to millimetres, convert the entered 'millimetre' values to pixels
            if self.millimetre_flag:
                scale_factor = self.config['ImageCorrection']['ScaleFactor']
                self.part_transform[item.text()][0] += (round(self.spinX.value() * scale_factor))
                self.part_transform[item.text()][1] += (round(self.spinY.value() * scale_factor))
            else:
                # Change the translation parameters of the selected items to the entered ones
                self.part_transform[item.text()][0] += self.spinX.value()
                self.part_transform[item.text()][1] += self.spinY.value()

        self.preview_contours(self.config['SliceConverter']['ROIOffset'])

    def translate_reset(self):
        """Resets the translation parameters back to 0 for the selected parts"""

        for item in self.listSliceFiles.selectedItems():
            # Reset the translation parameters of the selected items
            self.part_transform[item.text()][0] = 0
            self.part_transform[item.text()][1] = 0

        self.preview_contours(self.config['SliceConverter']['ROIOffset'])

    def pause(self):
        """Executes when the Paused/Resume button is pressed
        Pauses or resumes either the slice conversion or the contour drawing loops"""

        if 'Pause' in self.pushPause.text():
            self.pushPause.setText('Resume')
            self.pushDone.setEnabled(True)
            if self.active_process == 1:
                self.convert_run_flag = False
            elif self.active_process == 2:
                self.draw_run_flag = False

        elif 'Resume' in self.pushPause.text():
            self.pushPause.setText('Pause')
            self.pushDone.setEnabled(False)
            if self.active_process == 1:
                self.convert_run_flag = True
                self.convert_slice(self.slice_list[self.index_list[self.slice_counter]])
            elif self.active_process == 2:
                self.draw_run_flag = True
                self.draw_contours(self.contour_counter)

    def browse_output(self):
        """Prompts the user to select a folder to save the drawn contours to"""

        folder = QFileDialog.getExistingDirectory(self, 'Browse...', '')

        if folder:
            self.output_folder = folder
            self.lineFolder.setText(self.output_folder)

    def select_parts(self):

        # Reset the colours of all the parts back to blue
        for key in self.part_colours.keys():
            self.part_colours[key] = (255, 0, 0)

        self.selected_items = list()

        # Change the selected item colours to green and re-draw the contours
        for item in self.listSliceFiles.selectedItems():
            # Change the part colour of the selected item to green
            self.part_colours[item.text()] = (0, 128, 255)

            # Highlight the corresponding part columns in the Transformation table
            self.selected_items.append(item.text())

        # Update the Transform table to also highlight the aforementioned selected items
        self.update_table()
        self.preview_contours()

    def toggle_control(self, state):
        """Enables or disables the following elements in one fell swoop depending on the received state"""

        # State 0 - No files added
        # State 1 - Files in the middle of being converted or contours being drawn
        # State 2 - Files added, contour preview successfully displayed
        self.pushAddSF.setEnabled(state != 1)
        self.pushRemoveSF.setEnabled(state != 1)
        self.groupDisplayOptions.setEnabled(state == 2)
        self.groupDisplayControl.setEnabled(state == 2)
        self.groupDrawRange.setEnabled(state == 2)
        self.groupROI.setEnabled(state == 2)
        self.groupRotation.setEnabled(state == 2)
        self.groupTranslation.setEnabled(state == 2)
        self.pushBrowseOF.setEnabled(state != 1)
        self.pushPause.setEnabled(state == 1)
        self.pushDone.setEnabled(state != 1)

    def preview_contours(self, roi_offset=0):
        """Draw a 'preview' of the selected layer's contours"""

        if self.checkBackground.isChecked():
            # Use the chosen background image to draw contours on
            image = cv2.flip(self.image_background.copy(), 0)
        else:
            # Create a blank RGB image and convert it to white, and draw a black rectangle representing the platform
            image = np.zeros(tuple(self.config['ImageCorrection']['ImageResolution'] + [3]), np.uint8)
            image[:] = (255, 255, 255)
            cv2.rectangle(image, (0, 0), image.shape[:2][::-1], (0, 0, 0), 5)

        # Check if the Fill Contours checkbox is checked to figure out how to draw the contours
        if self.checkFillContours.isChecked():
            thickness = -1
        else:
            thickness = self.config['SliceConverter']['CentrelineT']

        # Disable determining the ROI if the Auto-Set checkbox is unchecked
        if not self.checkAutoSet.isChecked():
            roi_offset = 0

        worker = qt_thread.Worker(slice_converter.SliceConverter().draw_contours, self.contour_dict, image,
                                  self.current_layer, self.part_colours, self.part_transform,
                                  self.output_folder, thickness, roi_offset, False, False)
        worker.signals.roi.connect(self.set_roi)
        worker.signals.result.connect(self.update_display)

        self.threadpool.start(worker)

    def update_display(self, image):
        """Display the preview contours on the graphics viewer"""

        thickness = self.config['SliceConverter']['CentrelineT']

        if self.checkCentrelines.isChecked():
            cv2.line(image, (0, image.shape[0] // 2), (image.shape[1], image.shape[0] // 2), (0, 0, 0), thickness)
            cv2.line(image, (image.shape[1] // 2, 0), (image.shape[1] // 2, image.shape[0]), (0, 0, 0), thickness)

        # Draw a rectangle of the user selected region of interest
        if self.roi[0]:
            cv2.rectangle(image, (self.roi[1], self.roi[2]), (self.roi[3], self.roi[4]), (0, 0, 255), 4)

        self.graphicsDisplay.set_image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        self.update_table()

        # Allow the selection of files in the list from doing things
        self.listSliceFiles.blockSignals(False)

    def update_layer_ranges(self):
        """Updates all parts of the dialog window UI that involves the maximum number of layers
        Additionally populates the contour dictionary which will be used to draw the contours"""

        self.update_status('All | Loading contours...')

        self.contour_dict = dict()

        # Load all the contours into memory and save them to a dictionary
        for index, filename in enumerate(self.slice_list):
            with open(filename.replace('.cli', '_contours.txt')) as contour_file:
                self.contour_dict[list(sorted(self.part_colours.keys()))[index]] = contour_file.readlines()

        self.max_layers = 1

        # Find the max number of layers from the first line in the contours file
        for contours in self.contour_dict.values():
            self.max_layers = max(int(contours[0]), self.max_layers)

        self.labelSliceNumber.setText('%s / %s' % (str(self.current_layer).zfill(4), str(self.max_layers).zfill(4)))
        self.spinRangeHigh.setMaximum(self.max_layers)
        self.spinRangeHigh.setValue(self.max_layers)

        self.update_status('All | Contours loaded.')

    def update_table(self):
        """Updates the Transformation Table with the translation and rotation parameters of each part"""

        # Set the number of columns to the number of parts
        self.tableTransform.setColumnCount(len(self.part_transform))
        column = 0

        # Populate the table with the part transform data
        for name, value in sorted(self.part_transform.items()):
            # Set the first row of items being the part names
            self.tableTransform.setItem(0, column, QTableWidgetItem(name))

            # Highlight the items if the corresponding part is selected
            if name in self.selected_items:
                self.tableTransform.item(0, column).setBackground(QColor('yellow'))

            for index in range(3):

                # Set the translation or rotation values, converting back from pixels to millimetres if set
                if self.millimetre_flag:
                    item = str(round(value[index] / self.config['ImageCorrection']['ScaleFactor']))
                else:
                    item = str(value[index])

                self.tableTransform.setItem(index + 1, column, QTableWidgetItem(item))
                if name in self.selected_items:
                    self.tableTransform.item(index + 1, column).setBackground(QColor('yellow'))

            column += 1

        # Resize the columns to its contents
        self.tableTransform.resizeColumnsToContents()

    def update_position(self, x, y):
        """Displays the relative position of the mouse cursor over the Layer Preview graphics view"""

        # Limit the mouse position to within the image window/resolution
        x = np.clip(x, 0, self.config['ImageCorrection']['ImageResolution'][1])
        y = np.clip(y, 0, self.config['ImageCorrection']['ImageResolution'][0])

        # If the units are set to millimetres, the pixels need to be converted
        if self.millimetre_flag:
            self.labelXPosition.setText('X  {:06.2f}'.format(round(x / self.config['ImageCorrection']['ScaleFactor'], 2)))
            self.labelYPosition.setText('Y  {:06.2f}'.format(round(y / self.config['ImageCorrection']['ScaleFactor'], 2)))
        else:
            self.labelXPosition.setText('X     ' + str(x).zfill(4))
            self.labelYPosition.setText('Y     ' + str(y).zfill(4))

    def update_status(self, string):
        string = string.split(' | ')
        self.labelStatus.setText(string[1])
        self.labelStatusPart.setText(string[0])

    def update_progress(self, percentage):
        self.progressBar.setValue(percentage)

    def closeEvent(self, event):
        """If a process is in progress, display an error message and prevent the user from exiting the dialog window
        Otherwise it saves the current window position and size to the registry"""

        # Check if a conversion or drawing is in progress, and block the user from closing the window until paused
        if self.convert_run_flag or self.draw_run_flag:
            run_error = QMessageBox(self)
            run_error.setWindowTitle('Error')
            run_error.setIcon(QMessageBox.Critical)
            run_error.setText('Conversion or Drawing in progress.\n'
                              'Please pause or wait for the active process to finish before exiting.')
            run_error.exec_()
            event.ignore()
        else:
            self.window_settings.setValue('Slice Converter Geometry', self.saveGeometry())


class ImageConverter(QDialog, dialogImageConverter.Ui_dialogImageConverter):
    """Module used to initiate the modal Image Converter dialog window
    Allows the user to batch convert a bunch of images to any of their fixed states
    """

    def __init__(self, parent=None):

        # Setup Dialog UI with MainWindow as parent
        super(ImageConverter, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)
        self.window_settings = QSettings('MCAM', 'Defect Monitor')

        try:
            self.restoreGeometry(self.window_settings.value('Image Converter Geometry', ''))
        except TypeError:
            pass

        # Setup event listeners for all relevant UI components, and connect them to specific functions
        self.pushBrowse.clicked.connect(self.browse)
        self.checkToggleAll.toggled.connect(self.toggle_all)
        self.checkUndistort.toggled.connect(self.toggle_save)
        self.checkPerspective.toggled.connect(self.toggle_save)
        self.checkCrop.toggled.connect(self.toggle_save)
        self.checkCrop.toggled.connect(self.toggle_alternate)
        self.checkEqualization.toggled.connect(self.toggle_save)
        self.checkSave.toggled.connect(self.reset)
        self.checkAlternate.toggled.connect(self.reset)
        self.pushStart.clicked.connect(self.start)

        # Couple of flags
        self.run_flag = False
        self.naming_flag = True

        self.threadpool = QThreadPool()

    def browse(self):
        """Prompts the user to select images to be converted"""

        filenames = QFileDialog.getOpenFileNames(self, 'Browse...', '', 'Image Files (*.png)')[0]

        if filenames:
            self.image_list = filenames
            self.listImages.clear()

            # Add just the filename (without the directory path) to the list widget
            for index, item in enumerate(filenames):
                self.listImages.addItem(os.path.basename(item))

            self.groupImagesSave.setEnabled(True)
            self.image_counter = 0
            self.update_status('Please select images to save.')

    def toggle_all(self):
        """Toggles the checked state of all the options in the Images to Save groupBox"""

        for checkbox in self.groupImagesSave.findChildren(QCheckBox):
            checkbox.blockSignals(True)
            checkbox.setChecked(self.checkToggleAll.isChecked())
            checkbox.blockSignals(False)

        self.checkAlternate.setEnabled(self.checkToggleAll.isChecked())
        self.toggle_save()

    def toggle_save(self):
        """Toggles the enabled state of the Save to Individual Folders checkbox depending on the checked image boxes
        Also toggles the checked state of the Toggle All checkbox"""

        # Count the number of checked checkboxes
        counter = 0

        # Check if any of the checkboxes within the groupBox is checked (ignoring the Toggle All checkbox)
        for checkbox in self.groupImagesSave.findChildren(QCheckBox)[1:]:
            if checkbox.isChecked():
                counter += 1

        if counter > 0:
            # Enable the relevant checkbox and the Start button and exit the method
            self.checkSave.setEnabled(True)
            self.checkToggleAll.blockSignals(True)
            self.checkToggleAll.setChecked(counter == 4)
            self.checkToggleAll.blockSignals(False)
            self.reset()
            return
        else:
            # Disable the checkbox and Start button if none of the Save checkboxes are checked
            self.checkToggleAll.setChecked(False)
            self.checkSave.setEnabled(False)
            self.checkSave.setChecked(False)
            self.pushStart.setEnabled(False)
            self.update_status('Please select images to save.')

    def toggle_alternate(self):
        """Toggles the enabled state of the Alternate Naming Scheme checkbox depending on the Crop checkbox"""

        if not self.checkCrop.isChecked():
            self.checkAlternate.setChecked(False)

    def reset(self):
        """Resets the state of converted images if any of the checkboxes are toggled"""

        self.image_counter = 0
        self.pushStart.setText('Start')
        self.pushStart.setEnabled(True)
        self.update_status('Waiting to start conversion.')
        self.update_progress(0)

        for index in range(self.listImages.count()):
            self.listImages.item(index).setBackground(QColor('white'))

    def start(self):
        """Runs all the selected images in the image list through the Image Converter
        The button also functions as a Stop button which halts the conversion process
        Clicking the Start button again continues converting the remaining images unless the image list has changed"""

        if 'Start' in self.pushStart.text():
            self.run_flag = True

            # Save the isChecked and isEnabled states of the checkboxes as a list
            self.checked = list()
            self.enabled = list()

            # The findChildren function returns a list of all the checkboxes in the dialog window
            for checkbox in self.findChildren(QCheckBox):
                self.checked.append(checkbox.isChecked())
                self.enabled.append(checkbox.isEnabled())

                # Disable all the checkboxes to disallow the user from doing other tasks
                checkbox.setEnabled(False)

            # Disable all buttons to prevent user from doing other tasks
            self.pushBrowse.setEnabled(False)

            # Change the Start button into a Stop button
            self.pushStart.setText('Pause')

            folder_name = os.path.dirname(self.image_list[0])

            # Create the individual folders if the Save to Individual Folders checkbox is checked
            if self.checkSave.isChecked():
                if self.checkUndistort.isChecked():
                    if not os.path.isdir(folder_name + '/undistort'):
                        os.makedirs(folder_name + '/undistort')
                if self.checkPerspective.isChecked():
                    if not os.path.isdir(folder_name + '/perspective'):
                        os.makedirs(folder_name + '/perspective')
                if self.checkCrop.isChecked() and not self.checkAlternate.isChecked():
                    if not os.path.isdir(folder_name + '/crop'):
                        os.makedirs(folder_name + '/crop')
                if self.checkEqualization.isChecked():
                    if not os.path.isdir(folder_name + '/equalization'):
                        os.makedirs(folder_name + '/equalization')

            if self.checkAlternate.isChecked():
                if not os.path.isdir(folder_name + '/fixed'):
                    os.makedirs(folder_name + '/fixed/coat')
                    os.makedirs(folder_name + '/fixed/scan')
                    os.makedirs(folder_name + '/fixed/snapshot')

            # Start the image conversion loop
            self.convert_image(self.image_list[self.image_counter])

        elif 'Pause' in self.pushStart.text():
            self.run_flag = False
            self.pushStart.setText('Resume')
            self.pushStart.setEnabled(False)

        elif 'Resume' in self.pushStart.text():
            self.run_flag = True
            self.pushStart.setText('Pause')

            for checkbox in self.findChildren(QCheckBox):
                checkbox.setEnabled(False)

            self.convert_image(self.image_list[self.image_counter])

    def convert_image(self, image_name):
        """Converts the image by applying the required image processing functions to fix the images using QThreads"""

        # Load the calibration parameters to be used to convert the images
        with open('config.json') as config:
            parameters = json.load(config)['ImageCorrection']
        self.naming_flag = True

        worker = qt_thread.Worker(image_processing.ImageFix().convert_image, image_name, parameters,
                                  self.checked)
        worker.signals.status.connect(self.update_status)
        worker.signals.progress.connect(self.update_progress)
        worker.signals.naming_error.connect(self.naming_error)
        worker.signals.finished.connect(self.convert_image_finished)
        self.threadpool.start(worker)

    def convert_image_finished(self):
        """Continuation function that either continues the image processing loop or finishes the entire run"""

        if self.naming_flag:
            self.listImages.item(self.image_counter).setBackground(QColor('green'))

        self.image_counter += 1

        if self.run_flag and not self.image_counter == len(self.image_list):
            self.convert_image(self.image_list[self.image_counter])
        else:
            self.pushBrowse.setEnabled(True)
            for index, checkbox in enumerate(self.findChildren(QCheckBox)):
                checkbox.setEnabled(self.enabled[index])

            if self.image_counter == len(self.image_list):
                self.run_flag = False
                self.pushStart.setEnabled(False)
                self.pushStart.setText('Start')
                self.update_status('Conversion finished.')
            else:
                self.pushStart.setEnabled(True)
                self.update_status('Conversion paused.')

    def naming_error(self):
        """Sets the colour of the current item to yellow and stops the conversion from turning the item green
        Indicates that the image names are incorrect for the Alternate Naming Scheme"""

        self.naming_flag = False
        self.listImages.item(self.image_counter).setBackground(QColor('yellow'))

    def update_status(self, string):
        self.labelStatus.setText(string)

    def update_progress(self, percentage):
        self.progressBar.setValue(int(percentage))

    def closeEvent(self, event):
        """Saves the current window position and size to the registry"""

        # Check if a conversion is in progress, and block the user from closing the window until stopped
        if self.run_flag:
            run_error = QMessageBox(self)
            run_error.setWindowTitle('Error')
            run_error.setIcon(QMessageBox.Critical)
            run_error.setText('Conversion in progress.\n\n'
                              'Please pause or wait for the conversion to finish before exiting.')
            run_error.exec_()
            event.ignore()
        else:
            self.window_settings.setValue('Image Converter Geometry', self.saveGeometry())


class DefectReports(QDialog, dialogDefectReports.Ui_dialogDefectReports):
    """Module used to intiate the modeless Defect Reports dialog window
    Displays the coat and scan defect report data in a nice visual way
    Also allows the user to sort, remove, set thresholds and export the data to a .csv file for further analysis
    """

    tab_focus = pyqtSignal(int, int, bool, int)

    def __init__(self, parent=None):

        # Setup Dialog UI with MainWindow as parent
        super(DefectReports, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)
        self.window_settings = QSettings('MCAM', 'Defect Monitor')

        try:
            self.restoreGeometry(self.window_settings.value('Defect Reports Geometry', ''))
        except TypeError:
            pass

        # Load from the build.json file
        with open('build.json') as build:
            self.build = json.load(build)

        # Load from the config.json file
        with open('config.json') as config:
            self.config = json.load(config)

        # Setup event listeners for all relevant UI components, and connect them to specific functions
        self.comboParts.currentIndexChanged.connect(self.populate_tables)
        self.pushSet.clicked.connect(self.set_thresholds)
        self.pushExportAll.clicked.connect(self.export_all_data)
        self.pushExportVisible.clicked.connect(self.export_visible_data)
        self.pushHideSelected.clicked.connect(self.hide_selected)
        self.tableCoat.cellDoubleClicked.connect(self.cell_click)
        self.tableScan.cellDoubleClicked.connect(self.cell_click)

        # Grab the part name list (with combined and background at the start) by polling the reports folder
        self.part_names = ['combined', 'background']
        for name in os.listdir(self.build['BuildInfo']['Folder'] + '/reports'):
            if 'combined' in name or 'background' in name:
                continue
            else:
                self.part_names.append(name.replace('_report.json', ''))

        # Add the part names to the combo box
        self.comboParts.addItems(self.part_names)

        # Sets the data table's columns to automatically resize appropriately
        # Except the first column, the layer number, which will be as small as possible
        self.tableCoat.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableScan.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableCoat.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableScan.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # Set the threshold spinboxes with the values from the config.json file
        self.spinPixelSize.setValue(self.config['Threshold']['PixelSize'])
        self.spinOccurrences.setValue(self.config['Threshold']['Occurrences'])
        self.spinOverlay.setValue(self.config['Threshold']['Overlay'])
        self.spinHistogramCoat.setValue(self.config['Threshold']['HistogramCoat'])
        self.spinHistogramScan.setValue(self.config['Threshold']['HistogramScan'])

    def populate_tables(self, part):
        """Populates both tables with the data from the selected defect report"""

        # Read the appropriate report into memory
        with open('%s/reports/%s_report.json' % (self.build['BuildInfo']['Folder'], self.part_names[part])) as report:
            report = json.load(report)

        # Completely remove all the data from both tables
        self.tableCoat.setRowCount(0)
        self.tableScan.setRowCount(0)

        # Disable sorting while populating the table so the data order doesn't get messed up
        self.tableCoat.setSortingEnabled(False)
        self.tableScan.setSortingEnabled(False)

        # Check if the report dictionary has anything at all
        if report:
            # Calculate the maximum number of layers to set the number of table rows
            max_layer = max([int(number) for number in list(report)])
            self.tableCoat.setRowCount(max_layer)
            self.tableScan.setRowCount(max_layer)

            # Grab the threshold values for both the coat and the scan defects in separate lists
            threshold_coat = [0, self.config['Threshold']['Occurrences'], self.config['Threshold']['Occurrences'],
                              self.config['Threshold']['PixelSize'], self.config['Threshold']['PixelSize'],
                              self.config['Threshold']['HistogramCoat']]
            threshold_scan = [0, self.config['Threshold']['Occurrences'], self.config['Threshold']['Occurrences'],
                              self.config['Threshold']['HistogramScan'], self.config['Threshold']['Overlay']]

            # Display all the relevant data in the table, while also filling out the 'missing' rows with zeroes
            for row in range(max_layer):
                # COAT DATA
                # Grab the Coat data in a try loop in case the index doesn't exist in the dictionary
                try:
                    data = report[str(row + 1).zfill(4)]['coat']
                except (IndexError, KeyError):
                    data = {}

                # Reset a list of colours to colour code each cell
                data_colours = list()
                data_coat = list()

                if data:
                    # Grab the data from the report dictionary, with the first element being the layer number
                    data_coat = [row + 1, data['BS'][1], data['BC'][1], data['SP'][0], data['CO'][0]]

                    # Append the histogram result if it is available in the first place
                    try:
                        data_coat.append(round(data['HC'], 2))
                    except (KeyError, IndexError):
                        data_coat.append(0)

                    # Set colours for if the data is over/under the threshold, or there is no data at all
                    # Green is GOOD
                    # Red is BAD
                    # Yellow is NONE
                    # NOTE: Different results have different conditions (over/under) for a good/bad result
                    for index, value in enumerate(data_coat):
                        if value < threshold_coat[index]:
                            data_colours.append(QColor(0, 255, 0))
                        else:
                            data_colours.append(QColor(255, 0, 0))
                else:
                    for number in range(6):
                        data_coat.append(0)
                        data_colours.append(QColor(255, 255, 0))

                    # Set the first element to the layer number
                    data_coat[0] = row + 1

                # Fill the table cells with the corresponding data
                for column in range(len(data_coat)):
                    # The following lines allow the data to be sorted numerically (rather than as strings)
                    item = QTableWidgetItem()
                    item.setData(Qt.EditRole, data_coat[column])
                    self.tableCoat.setItem(row, column, item)

                    # Ignore the first column (layer number) when it comes to setting the background colour
                    if column != 0:
                        self.tableCoat.item(row, column).setBackground(data_colours[column])

                # SCAN DATA
                # Grab the Scan data in a try loop in case the index doesn't exist in the dictionary
                try:
                    data = report[str(row + 1).zfill(4)]['scan']
                except (IndexError, KeyError):
                    data = {}

                # Reset a list of colours to colour code each cell
                data_colours = list()
                data_scan = list()

                if data:
                    # Grab the data from the report dictionary, with the first element being the layer number
                    data_scan = [row + 1, data['BS'][1], data['BC'][1]]

                    # Append the histogram result if it is available in the first place
                    try:
                        data_scan.append(round(data['HC'], 2))
                    except (KeyError, IndexError):
                        data_scan.append(0)

                    # Same goes for the overlay comparison information
                    try:
                        data_scan.append(round(data['OC'] * 100, 4))
                    except (KeyError, IndexError):
                        data_scan.append(0)

                    # Set colours for if the data is over/under the threshold, or there is no data at all
                    for index, value in enumerate(data_scan):
                        if value < threshold_scan[index] and index < 3:
                            data_colours.append(QColor(0, 255, 0))
                        elif value > threshold_scan[index] and index == 3:
                            data_colours.append(QColor(0, 255, 0))
                        else:
                            data_colours.append(QColor(255, 0, 0))
                else:
                    for number in range(5):
                        data_scan.append(0)
                        data_colours.append(QColor(255, 255, 0))

                    # Set the first element to the layer number
                    data_scan[0] = row + 1

                # Fill the table cells with the corresponding data
                for column in range(len(data_scan)):
                    # The following lines allow the data to be sorted numerically (rather than as strings)
                    item = QTableWidgetItem()
                    item.setData(Qt.EditRole, data_scan[column])
                    self.tableScan.setItem(row, column, item)

                    # Ignore the first column (layer number) when it comes to setting the background colour
                    if column != 0:
                        self.tableScan.item(row, column).setBackground(data_colours[column])

        # Sets the row height to as small as possible to fit the text height
        self.tableCoat.resizeRowsToContents()
        self.tableScan.resizeRowsToContents()

        # Re-enable sorting
        self.tableCoat.setSortingEnabled(True)
        self.tableScan.setSortingEnabled(True)

    def set_thresholds(self):
        """Save the entered threshold values to the config.json file and reload the data based on the new values"""

        with open('config.json') as config:
            self.config = json.load(config)

        # Save the new values from the changed settings to the config dictionary
        self.config['Threshold']['PixelSize'] = self.spinPixelSize.value()
        self.config['Threshold']['Occurrences'] = self.spinOccurrences.value()
        self.config['Threshold']['Overlay'] = self.spinOverlay.value()
        self.config['Threshold']['HistogramCoat'] = self.spinHistogramCoat.value()
        self.config['Threshold']['HistogramScan'] = self.spinHistogramScan.value()

        with open('config.json', 'w+') as config:
            json.dump(self.config, config, indent=4, sort_keys=True)

        # Reload the data and colour code based on the new threshold values
        self.populate_tables(self.comboParts.currentIndex())

    def cell_click(self, row, column):
        """Send a signal back to the MainWindow to display the corresponding defect image
        When a cell in the report table is clicked"""

        # Grab the layer number from the table as it won't correlate with the row number if the table is sorted
        # Also depends if it's the coat or scan table being clicked
        if self.widgetReports.currentIndex() == 0:
            layer = int(self.tableCoat.item(row, 0).text())
        else:
            layer = int(self.tableScan.item(row, 0).text())
            if column == 4:
                column += 1

        # Emit a signal to change focus to the selected defect layer
        self.tab_focus.emit(self.widgetReports.currentIndex(), layer, True, column - 1)

    def export_all_data(self):
        """Exports all the data to two separate excel compatible .csv (comma separated values) files"""

        # Let the user set a name for the coat and scan data (with a pre-defined name already set)
        filename_coat = QFileDialog.getSaveFileName(self, 'Export Coat Data', '%s/%s_data_coat' %
                                                    (
                                                    self.build['BuildInfo']['Folder'], self.build['BuildInfo']['Name']),
                                                    'CSV File (*.csv)')[0]

        if filename_coat:
            filename_scan = QFileDialog.getSaveFileName(self, 'Export Scan Data', '%s/%s_data_scan' %
                                                        (self.build['BuildInfo']['Folder'],
                                                         self.build['BuildInfo']['Name']),
                                                        'CSV File (*.csv)')[0]
            if not filename_scan:
                # Did the filename grab this way to not have so many indents in the main code
                return
        else:
            return

        # Initialize the two data dictionaries to store the data to
        data_coat = {'LABELS': list()}
        data_scan = {'LABELS': list()}

        # All the lists for each layer needs to be initialized first before they can be extended
        for layer in range(1, self.build['SliceConverter']['MaxLayers'] + 1):
            data_coat[str(layer)] = list()
            data_scan[str(layer)] = list()

        # Iterate through all the parts
        for part_name in self.part_names:
            # Set up the first row of both dictionaries by extending the part name, labels and finally a spacer
            data_coat['LABELS'].extend(
                [part_name, 'LAYER', 'STREAKS', 'CHATTER', 'PATCHES', 'OUTLIERS', 'HISTOGRAM', ''])
            data_scan['LABELS'].extend([part_name, 'LAYER', 'STREAKS', 'CHATTER', 'HISTOGRAM', 'OVERLAY', ''])

            # Read each part's reports into memory
            with open('%s/reports/%s_report.json' % (self.build['BuildInfo']['Folder'], part_name)) as report:
                report = json.load(report)

            for layer in range(1, self.build['SliceConverter']['MaxLayers'] + 1):
                # Grab the coat data in a try loop in case the index doesn't exist in the dictionary
                try:
                    data = report[str(layer).zfill(4)]['coat']
                except (IndexError, KeyError):
                    data_coat[str(layer)].extend([part_name, str(layer), '0', '0', '0', '0', '0'])
                else:
                    data_coat[str(layer)].extend(
                        [part_name, str(layer), data['BS'][1], data['BC'][1], data['SP'][0], data['CO'][0]])

                    # Separated out as the parts don't contain histogram data
                    try:
                        data_coat[str(layer)].extend([round(data['HC'], 2), ''])
                    except (KeyError, IndexError):
                        data_coat[str(layer)].extend(['0', ''])

                # Do the same for the scan data
                try:
                    data = report[str(layer).zfill(4)]['scan']
                except (IndexError, KeyError):
                    data_scan[str(layer)].extend([part_name, str(layer), '0', '0'])
                else:
                    data_scan[str(layer)].extend([part_name, str(layer), data['BS'][1], data['BC'][1]])

                    try:
                        data_scan[str(layer)].append(round(data['HC'], 2))
                    except (KeyError, IndexError):
                        data_scan[str(layer)].append('0')

                    try:
                        data_scan[str(layer)].extend([round(data['OC'] * 100, 4), ''])
                    except (KeyError, IndexError):
                        data_scan[str(layer)].extend(['0', ''])

        # Write the coat and scan data to separate .csv files using the csv writer
        # Put into a try loop just in case the user tries to overwrite a csv file that is currently open
        try:
            with open(filename_coat, 'w+', newline='') as csv_file:
                writer = csv.writer(csv_file)
                for item in data_coat.values():
                    writer.writerow(item)
        except PermissionError:
            self.permission_error()
            return
        try:
            with open(filename_scan, 'w+', newline='') as csv_file:
                writer = csv.writer(csv_file)
                for item in data_scan.values():
                    writer.writerow(item)
        except PermissionError:
            self.permission_error()
            return

        # Open a message box with an export confirmation message
        export_confirmation = QMessageBox(self)
        export_confirmation.setWindowTitle('Export All Data')
        export_confirmation.setIcon(QMessageBox.Information)
        export_confirmation.setText('The coat data has been exported to %s.\n\nThe scan data has been exported '
                                    'to %s.' % (filename_coat, filename_scan))
        export_confirmation.exec_()

    def permission_error(self):
        """Opens a message box displaying a permission error when trying to write the csv file"""
        permission_error = QMessageBox(self)
        permission_error.setWindowTitle('Error')
        permission_error.setIcon(QMessageBox.Critical)
        permission_error.setText('Permission error when trying to save the .csv file.\nPlease close the .csv file '
                                 'you wish to overwrite before retrying.')
        permission_error.exec_()

    def export_visible_data(self):
        """Exports the visible table data to an excel compatible .csv (comma separated values) file"""

        filename = QFileDialog.getSaveFileName(self, 'Export Visible Data', '%s/%s_data' %
                                               (self.build['BuildInfo']['Folder'], self.build['BuildInfo']['Name']),
                                               'CSV File (*.csv)')[0]

        if filename:
            # The data will be stored in lists a dictionary with every key being a new row
            data = dict()

            tables = [self.tableCoat, self.tableScan]
            index = self.widgetReports.currentIndex()
            part = self.comboParts.currentIndex()

            # Set up the first row of the table with the labels depending on which table is being exported
            if index == 0:
                data['LABELS'] = ['LAYER', 'STREAKS', 'CHATTER', 'PATCHES', 'OUTLIERS']
                # Only the combined data has the following data
                if part == 0:
                    data['LABELS'].append('HISTOGRAM')
            else:
                data['LABELS'] = ['LAYER', 'STREAKS', 'CHATTER']
                if part == 0:
                    data['LABELS'].extend(['HISTOGRAM', 'OVERLAY'])

            # Grab the data from the currently visible table
            for row in range(tables[index].rowCount()):
                data[str(row)] = list()
                for column in range(6):
                    # Check if the cell has data and skip it if it doesnt (for individual parts)
                    try:
                        data[str(row)].append(tables[index].item(row, column).text())
                    except AttributeError:
                        continue

            # Write the data to a .csv file using the csv writer
            with open(filename, 'w+', newline='') as csv_file:
                writer = csv.writer(csv_file)
                for item in data.values():
                    writer.writerow(item)

            # Open a message box with an export confirmation message
            export_confirmation = QMessageBox(self)
            export_confirmation.setWindowTitle('Export Visible Data')
            export_confirmation.setIcon(QMessageBox.Information)
            export_confirmation.setText('The data has been exported to %s.' % filename)
            export_confirmation.exec_()

    def hide_selected(self):
        """Hides the currently selected row of layers from the currently displayed window"""

        indexes = list()

        # Coat Explorer
        if self.widgetReports.currentIndex() == 0:
            # Grab the row indexes of all the selected cells
            for item in self.tableCoat.selectedItems():
                indexes.append(item.row())

            # Remove any duplicate row indexes, sort and reverse the list and remove the rows from the table
            for index in sorted(list(set(indexes)))[::-1]:
                self.tableCoat.removeRow(index)
        # Scan Explorer
        elif self.widgetReports.currentIndex() == 1:
            for item in self.tableScan.selectedItems():
                indexes.append(item.row())
            for index in sorted(list(set(indexes)))[::-1]:
                self.tableScan.removeRow(index)

    def closeEvent(self, event):
        """Saves the current window position and size to the registry"""
        self.window_settings.setValue('Defect Reports Geometry', self.saveGeometry())
