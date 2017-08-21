# Import external libraries
import os
import re
import json
import cv2
import numpy as np
from PyQt4.QtCore import QThread, SIGNAL

import image_processing

class SliceConverter(QThread):
    """Module used to convert any slice files from .cls or .cli format into ASCII format
    Output can then be used to draw contours using OpenCV
    Currently only supports converting .cls files
    Future implementation will look to either shifting or adding .cli slice conversion

    Currently takes in a .cls or .cli file and parses it, saving it as a .txt file after conversion
    """

    def __init__(self, part_names, draw_flag, fill_flag, contours_folder=None):

        QThread.__init__(self)

        with open('config.json') as config:
            self.config = json.load(config)

        # Save respective values to be used to draw contours and polygons
        # Get the resolution of the cropped images using the crop boundaries, 3 at the end indicates an RGB image
        self.image_resolution = ((self.config['CropBoundary'][1] - self.config['CropBoundary'][0]),
                                 (self.config['CropBoundary'][3] - self.config['CropBoundary'][2]), 3)
        self.offset = (self.config['Offset'][0], self.config['Offset'][1])
        self.scale_factor = self.config['ScaleFactor']
        self.transform = self.config['TransformationParameters']

        # Store the received arguments as local instance variables
        self.part_names = part_names
        self.draw_flag = draw_flag
        self.fill_flag = fill_flag
        self.contours_folder = contours_folder

    def run(self):

        for part_name in self.part_names:

            self.emit(SIGNAL("update_status_slice(QString)"), os.path.basename(part_name))

            # Executes if the sent file is a .cls file
            if '.cls' in part_name:
                # Look for an already converted contours file
                if not os.path.isfile(part_name.replace('.cls', '_contours.txt')):
                    self.convert2contours(part_name.replace('.cli', '_contours.txt'), self.read_cls(part_name))
            # Executes if the sent file is a .cli file
            elif '.cli' in part_name:
                # Look for an already converted contours file
                if not os.path.isfile(part_name.replace('.cli', '_contours.txt')):
                    self.convert2contours(part_name.replace('.cli', '_contours.txt'), self.read_cli(part_name))
            else:
                self.emit(SIGNAL("update_status(QString)"), 'Slice file not found.')

            self.emit(SIGNAL("update_status(QString)"), 'Contours file %s found.' % os.path.basename(part_name))

        if self.draw_flag:
            # Create a dictionary of colours (different shades of teal) for each part's contours
            colours = dict()
            for index, part_name in enumerate(self.part_names):
                colours['%s' % os.path.basename(part_name)] = ((100 + 5 * index) % 255, (100 + 5 * index) % 255, 0)

            self.emit(SIGNAL("update_status_slice(QString)"), 'All.')
            self.emit(SIGNAL("update_progress(QString)"), '0')

            # Draw and save the contours to an image file
            self.draw_contours(self.part_names, colours, self.contours_folder)

    def read_cls(self, file_name):
        """Reads the .cls file and converts the contents into ASCII, then organises the data into a list"""

        self.emit(SIGNAL("update_status(QString)"), 'Reading CLS file...')

        # Set up a few flags, counters and lists
        layer_flag = False
        border_flag = False
        next_border_flag = False
        index = 2
        vector_no = 0

        # Initialize the converted data list with some important information
        data_ascii = [float(0.001), '']

        # UI Progress and Status Messages
        progress = 10.0
        progress_previous = None

        with open(file_name, 'rb') as cls_file:
            # Split the entire file into a massive list if the following strings are found
            data_binary = re.split('(NEW_LAYER)|(SUPPORT)*(NEW_BORDER)|(NEW_QUADRANT)'
                                   '|(INC_OFFSETS)|(NEW_ISLAND)|(NEW_SKIN)|(NEW_CORE)', cls_file.read())
            self.emit(SIGNAL("update_progress(QString)"), '8')
            # Remove any NoneType data in the list
            data_binary = filter(None, data_binary)
            increment = 90.0 / len(data_binary)
            self.emit(SIGNAL("update_progress(QString)"), str(int(round(progress))))

            for line in data_binary:
                if layer_flag or border_flag:
                    data_line = list()
                    data = list()
                    for character in line:
                        data_line.append(bin(ord(character))[2:].zfill(8))
                    data_line = data_line[::-1]
                    for one, two, three, four in zip(data_line[0::4], data_line[1::4], data_line[2::4],
                                                     data_line[3::4]):
                        decimal = int(one + two + three + four, 2)
                        data.append(decimal)
                    if layer_flag:
                        data_ascii[index] += str(data[-1] / 100)
                        layer_flag = False
                    elif border_flag:
                        data = data[::-1]
                        data_ascii[index] += '%s,%s,' % (data[0], data[1])
                        for one, two in zip(data[2::4], data[3::4]):
                            data_ascii[index] += (str(one / 100) + ',' + str(two / 100) + ',')
                            vector_no += 1
                        data_ascii[index] = data_ascii[index].replace('1,%s,%s,' % (data[0], data[1]),
                                                                      '1,%s,%s,' % (data[0], vector_no)).rstrip(',')
                        border_flag = False
                        next_border_flag = False
                    # Reset vector numbers
                    vector_no = 0
                    index += 1
                if 'NEW_LAYER' in line:
                    data_ascii.append('$$LAYER/')
                    layer_flag = True
                    next_border_flag = True
                if 'NEW_BORDER' in line and next_border_flag:
                    data_ascii.append('$$POLYLINE/1,')
                    border_flag = True
                    layer_flag = False
                # Put into a conditional to only trigger if the whole number changes so as to not overload the emit
                if int(round(progress)) is not progress_previous:
                    self.emit(SIGNAL("update_progress(QString)"), str(int(round(progress))))
                    progress_previous = int(round(progress))
                progress += increment

        return data_ascii

    def read_cli(self, file_name):
        """Reads the .cli file and converts the contents into an organised list
        If the file was encoded in binary, this method also converts the contents into ascii format"""

        self.emit(SIGNAL("update_status(QString)"), 'Reading CLI file...')

        # Set up a few flags, counters and lists
        binary_flag = False
        data_ascii = list()
        line_ascii = ''

        # UI Progress and Status Messages
        progress = 0.0
        progress_previous = None

        # Open the .cli file
        with open(file_name, 'r') as cli_file:
            increment = 100.0 / sum(1 for _ in cli_file)
            # Go back to the start of the file as getting the length of the file put the seek head to the EOF
            cli_file.seek(0)
            for line in cli_file:
                # Check if the file is actually encoded in binary, if so, break from this loop
                if 'BINARY' in line.strip():
                    binary_flag = True
                    break
                # Extract pertinent information from the header and store them in the dictionary
                elif 'UNITS' in line.strip():
                    data_ascii.append(float(line[8:-2]))
                elif 'GEOMETRYSTART' in line.strip():
                    break
                progress += increment

            for line in cli_file:
                if binary_flag:
                    break
                # Check if the line is empty or not (because of the removal of random newline characters
                if line.rstrip('\r\n/n'):
                    data_ascii.append(line.rstrip('\r\n/n'))
                # Put into a conditional to only trigger if the whole number changes so as to not overload the emit
                if int(round(progress)) is not progress_previous:
                    self.emit(SIGNAL("update_progress(QString)"), str(int(round(progress))))
                    progress_previous = int(round(progress))
                progress += increment

        if binary_flag:
            self.emit(SIGNAL("update_status(QString)"), 'Reading CLI file... Binary encoding detected.')
            progress = 0.0
            progress_previous = None

            # The file needs to be read as binary if it was encoded in binary
            with open(file_name, 'rb') as cli_file:
                increment = 100.0 / sum(1 for _ in cli_file)
                # Go back to the start of the file as getting the length of the file put the seek head to the EOF
                cli_file.seek(0)
                for line in cli_file:
                    if 'UNITS' in line.strip():
                        data_ascii.append(float(line[8:-2]))
                    elif 'HEADEREND' in line.strip():
                        data_binary = line.replace('$$HEADEREND', '')
                        break
                for line in cli_file:
                    data_binary += line
                    # Put into a conditional to only trigger if the whole number changes so as to not overload the emit
                    if int(round(progress)) is not progress_previous:
                        self.emit(SIGNAL("update_progress(QString)"), str(int(round(progress))))
                        progress_previous = int(round(progress))
                    progress += increment

            layer_flag = False
            layer_count = 0
            polyline_count = 0
            vector_count = 0

            # UI Progress and Status Messages
            progress = 0.0
            progress_previous = None
            increment = 100.0 / (len(data_binary) / 2.0)
            self.emit(SIGNAL("update_status(QString)"), 'Converting Binary into ASCII...')

            for one, two in zip(data_binary[0::2], data_binary[1::2]):
                # Convert the character unicode into an integer, then into a binary number
                # Join the second binary number with the first binary number and convert the 16-bit bin number into int
                decimal = int(bin(ord(two))[2:].zfill(8) + bin(ord(one))[2:].zfill(8), 2)
                # Check for command indexes and replace with appropriate ascii words
                if layer_flag:
                    line_ascii += (str(decimal) + ',')
                    layer_flag = False
                elif polyline_count > 0:
                    line_ascii += (str(decimal) + ',')
                    polyline_count -= 1
                    if polyline_count == 0:
                        vector_count = decimal * 2
                elif vector_count > 0:
                    line_ascii += (str(decimal) + ',')
                    vector_count -= 1
                elif decimal == 128:
                    data_ascii.append(line_ascii.rstrip(','))
                    line_ascii = '$$LAYER/'
                    layer_count += 1
                    layer_flag = True
                elif decimal == 129:
                    data_ascii.append(line_ascii.rstrip(','))
                    line_ascii = '$$POLYLINE/'
                    polyline_count = 3

                # Put into a conditional to only trigger if the whole number changes so as to not overload the emit
                if int(round(progress)) is not progress_previous:
                    self.emit(SIGNAL("update_progress(QString)"), str(int(round(progress))))
                    progress_previous = int(round(progress))
                progress += increment

            data_ascii[1] = layer_count

        return data_ascii

    def convert2contours(self, file_name, data_ascii):
        """Converts the data from the slice file into an organized scaled list of contours
        First element is the number of layers
        Every layer starts with a START LAYER XX, YY list, followed by the list of contours, followed by a END LAYER
        XX is the layer number, YY is the scaled layer height
        Method also saves the contours to a text file in real-time
        """

        # UI Progress and Status Messages
        progress = 0.0
        progress_previous = None
        increment = 100.0 / (len(data_ascii))
        self.emit(SIGNAL("update_status(QString)"), 'Converting data into organized list of contours...')

        # Initialize some variables to be used later
        units = data_ascii[0]
        layer_count = 0

        with open(file_name, 'w+') as contours_file:
            # Write the first line, the number of layers, to the text file
            contours_file.write('%s\n' % ['LAYERS', data_ascii[1]])

            for line in data_ascii[2::]:
                if 'LAYER' in line:
                    # Strip the newline character from the end, and split the string where the slash appears
                    line = re.split('(/)', line.rstrip('\n'))
                    if layer_count is not 0:
                        contours_file.write('%s\n' % ['END LAYER'])
                    layer_count += 1
                    contours_file.write('%s\n' % ['START LAYER %s' % str(layer_count).zfill(4), float(line[2]) * units])
                elif 'POLYLINE' in line:
                    # Split each number into its own entry in a list
                    # Remove all the comma elements and the first 3 numbers
                    line = re.split('(,)', line.rstrip('\r\n/n'))
                    line = [comma for comma in line if comma != ',']
                    # Store the contour coordinates as pixel units after taking scale factor into account
                    line = [int(round(float(element) * units * self.scale_factor)) for element in line[3:]]
                    contours_file.write('%s\n' % line)

            # Put into a conditional to only trigger if the whole number changes so as to not overload the emit
            if int(round(progress)) is not progress_previous:
                self.emit(SIGNAL("update_progress(QString)"), str(int(round(progress))))
                progress_previous = int(round(progress))
            progress += increment

        self.emit(SIGNAL("update_status(QString)"), 'Conversion complete.')

    def draw_contours(self, file_names, colours, folder_name):
        """Draw all the contours of the selected parts on the same image"""

        # Check if a separate folder has been selected to save the drawn contours to
        # If so, make sure that the folder exists, otherwise save to the contours folder in the current build
        if folder_name:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
        else:
            folder_name = '%s/contours' % self.config['ImageFolder']

        # UI Progress and Status Messages
        progress = 0.0
        progress_previous = None

        # Initial while loop conditions
        layer = 1
        layer_max = 10

        while layer < layer_max:
            # Create a black RGB image to draw contours on
            image_contours = np.zeros(self.image_resolution, np.uint8)

            for file_name in file_names:
                # Create an empty contours list to store all the contours of the current layer
                contours = list()
                contours_flag = False

                with open(file_name.replace('.cli', '_contours.txt').replace('.cls', '_contours.txt')) as contours_file:
                    for line in contours_file:
                        # Grab the contours and format them as a numpy array that drawContours accepts
                        if 'END LAYER' in line and contours_flag:
                            # Break to save a tiny bit of processing time once the current layer's contours are grabbed
                            break
                        elif contours_flag:
                            line = line.strip('[]\n').split(', ')
                            contours.append(np.array(line).reshape(1, len(line)/2, 2).astype(np.int32))
                        elif 'START LAYER %s' % str(layer).zfill(4) in line:
                            contours_flag = True
                        elif 'LAYERS' in line:
                            line = line.strip('[]\n').split(', ')
                            if int(line[1]) > layer_max:
                                layer_max = int(line[1])

                # Draw the contours onto the image_contours canvas
                # If the Fill Contours checkbox is checked, fill the contours, otherwise just draw the contours itself
                if self.fill_flag:
                    cv2.drawContours(image_contours, contours, -1, colours[os.path.basename(file_name)],
                                     offset=self.offset, thickness=cv2.FILLED)
                else:
                    cv2.drawContours(image_contours, contours, -1, colours[os.path.basename(file_name)],
                                     offset=self.offset, thickness=int(self.scale_factor))

            self.emit(SIGNAL("update_status(QString)"), 'Drawing contours %s of %s.' %
                      (str(layer).zfill(4), str(layer_max).zfill(4)))

            # Flip the image vertically to account for the fact that OpenCV's origin is the top left corner
            image_contours = cv2.flip(image_contours, 0)

            # Correct the image using calculated transformation parameters to account for the perspective warp
            image_contours = image_processing.ImageCorrection(None).transform(image_contours, self.transform)

            # Save the image to the selected image folder
            cv2.imwrite('%s/image_contours_%s.png' % (folder_name, str(layer).zfill(4)), image_contours)

            # Increment to the next layer
            layer += 1

            # Put into a conditional to only trigger if the whole number changes so as to not overload the emit
            progress += 100.0 / layer_max
            if int(round(progress)) is not progress_previous:
                self.emit(SIGNAL("update_progress(QString)"), str(int(round(progress))))
                progress_previous = int(round(progress))
