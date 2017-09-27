# Import external libraries
import os
import json
import cv2
import numpy as np

# Some global colours are defined here (represented as BGR)
COLOUR_RED = (0, 0, 255)
COLOUR_BLUE = (255, 0, 0)
COLOUR_GREEN = (0, 255, 0)
COLOUR_YELLOW = (0, 255, 255)
COLOUR_PURPLE = (255, 0, 255)
COLOUR_BLACK = (0, 0, 0)
COLOUR_WHITE = (255, 255, 255)


class ImageTransform:
    """Module containing methods used to transform or modify any images using a variety of OpenCV functions"""

    def __init__(self, test_flag=False):

        # Load configuration settings from config.json file
        with open('config.json') as config:
            self.config = json.load(config)

        # Checks whether to use the temporary results of the camera calibration, or the ones saved in the config file
        if test_flag:
            with open('%s/calibration_results.json' % self.build['WorkingDirectory']) as camera_parameters:
                self.parameters = json.load(camera_parameters)
                self.parameters = self.parameters['ImageCorrection']
        else:
            self.parameters = self.config['ImageCorrection']

    def apply_fixes(self, image):
        """Applies the distortion, perspective and crop processes to the received image"""

        image = self.distortion_fix(image)
        image = self.perspective_fix(image)
        image = self.crop(image)

        return image

    def distortion_fix(self, image):
        """Fixes the barrel/pincushion distortion commonly found in pinhole cameras"""

        # Store the camera's intrinsic values as a 2x2 matrix
        camera_matrix = np.array(self.parameters['CameraMatrix'])
        camera_matrix[0, 2] = image.shape[1] / 2.0  # Half image width
        camera_matrix[1, 2] = image.shape[0] / 2.0  # Half image height

        # OpenCV distortion fix function
        try:
            image = cv2.undistort(image, camera_matrix, np.array(self.parameters['DistortionCoefficients']))
            return image
        except:
            print('Image Distortion fix failed.')
            return False

    def perspective_fix(self, image):
        """Fixes the perspective warp due to the off-centre position of the camera"""

        try:
            image = cv2.warpPerspective(image, np.array(self.parameters['HomographyMatrix']),
                                        tuple(self.parameters['Resolution']))
            return image
        except:
            print('Image Perspective Fix failed.')
            return False

    def crop(self, image):
        """Crops the image to a more desirable region of interest"""

        # Save value to be used to determine region of interest
        crop_boundary = self.config['ImageCorrection']['CropBoundary']

        # Crop the image to a rectangle region of interest as dictated by the following values [H,W]
        image = image[crop_boundary[0]: crop_boundary[1], crop_boundary[2]: crop_boundary[3]]

        return image

    @staticmethod
    def transform(image, transform):

        width = image.shape[1]
        height = image.shape[0]

        # Flip
        if transform[3]:
            image = cv2.flip(image, 1)
        if transform[4]:
            image = cv2.flip(image, 0)

        # Translation
        translation_matrix = np.float32([[1, 0, transform[1]], [0, 1, transform[0]]])
        image = cv2.warpAffine(image, translation_matrix, (width, height))

        # Rotation
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), transform[2], 1)
        image = cv2.warpAffine(image, rotation_matrix, (width, height))

        # Stretching
        # Top Left Corner
        points1 = np.float32([[width, 0], [0, 0], [0, height]])
        points2 = np.float32([[width, transform[5] + transform[12]],
                              [transform[8], transform[5]],
                              [transform[8] + transform[13], height + transform[7]]])
        matrix = cv2.getAffineTransform(points1, points2)
        image = cv2.warpAffine(image, matrix, (width, height))
        # Top Right Corner
        points1 = np.float32([[0, 0], [width, 0], [width, height]])
        points2 = np.float32([[0, transform[10]],
                              [width + transform[6], 0],
                              [width + transform[6] + transform[15], height + transform[7]]])
        matrix = cv2.getAffineTransform(points1, points2)
        image = cv2.warpAffine(image, matrix, (width, height))
        # Bottom Left Corner
        points1 = np.float32([[0, 0], [0, height], [width, height]])
        points2 = np.float32([[transform[9], 0], [0, height], [width, height + transform[16]]])
        matrix = cv2.getAffineTransform(points1, points2)
        image = cv2.warpAffine(image, matrix, (width, height))
        # Bottom Right Corner
        points1 = np.float32([[0, height], [width, height], [width, 0]])
        points2 = np.float32([[0, height + transform[14]], [width, height], [width + transform[11], 0]])
        matrix = cv2.getAffineTransform(points1, points2)
        image = cv2.warpAffine(image, matrix, (width, height))

        return image

    @staticmethod
    def clahe(image, gray_flag=False, cliplimit=8.0, tilegridsize=(64, 64)):
        """Applies a Contrast Limited Adaptive Histogram Equalization to the image
        Used to improve the contrast of the image to make it clearer/visible
        The gray flag is used to indicate if the image is to be converted back to BGR or not
        """

        # Equalization algorithm requires the image to be in grayscale colour space to function
        # This line checks if the image is already grayscale or in RGB (BGR)
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # CLAHE filter functions
        clahe_filter = cv2.createCLAHE(cliplimit, tilegridsize)
        image = clahe_filter.apply(image)

        # Convert the image back to BGR as when converting to a QPixmap, grayscale images don't work
        if not gray_flag:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        return image


class DefectDetector:
    """Module used to process the corrected images using OpenCV functions to detect a variety of different defects
    Defects to be analyzed are outlined in the README.txt file
    Throughout the code, image objects are named image_(purpose)_(modification *default=BGR)
    Therefore an image that will contain defect pixels that has been converted to gray would be image_defects_gray
    """

    def __init__(self):

        # Load configuration settings from config.json file
        with open('config.json') as config:
            self.config = json.load(config)

        # Checking if the received image exists (a blank string may be sent which means the image doesn't exist)
        # Only a problem for the contours and previous images as this method cannot be accessed if the raw doesn't exist
        # image_raw refers to the original image and will remain unmodified throughout the class
        self.image_raw = cv2.imread(self.build['DefectDetector']['Image'])
        # image_contours refers to the image with all the part contours drawn on them
        if os.path.isfile(self.build['DefectDetector']['Contours']):
            self.image_contours = cv2.imread(self.build['DefectDetector']['Contours'])
            self.contours_flag = True
        else:
            self.contours_flag = False

        # image_previous refers to the previous layer's image
        if os.path.isfile(self.build['DefectDetector']['ImagePrevious']):
            self.image_previous = cv2.imread(self.build['DefectDetector']['ImagePrevious'])
            self.compare_flag = True
        else:
            self.compare_flag = False

        self.layer = str(self.build['DefectDetector']['Layer']).zfill(4)
        self.phase = self.build['DefectDetector']['Phase']

        # This is the master defect dictionary which stores all the defect results for all the parts
        self.defect_dict = dict()

        # self.defects_on = {'Bright Spots': [], 'Blade Streaks': [], 'Blade Chatter': [], 'Contrast Differences': []}
        # self.defects_off = {'Bright Spots': [], 'Blade Streaks': [], 'Blade Chatter': [], 'Contrast Differences': []}

        # Store a dictionary of all the reports to be written to (including the background and combined reports)
        self.part_colours = self.build['BuildInfo']['Colours']

        # Open all the reports and save their dictionaries to the master defect dictionary
        # These dictionaries will be overwritten with new data should the program process the same layer/part
        for report_name in self.part_colours.keys():
            with open('%s/reports/%s_report.json' % (self.build['ImageCapture']['Folder'], report_name)) as report:
                self.defect_dict[report_name] = json.load(report)

            # The dictionary needs to be built up if it doesn't already exist
            if self.layer not in self.defect_dict[report_name]:
                self.defect_dict[report_name][self.layer] = dict()
                self.defect_dict[report_name][self.layer]['scan'] = dict()
                self.defect_dict[report_name][self.layer]['coat'] = dict()

        # Because blade chatter relies on number of occurrences rather than pixel size
        self.chatter_count = 0

    def run_detector(self, status, progress):
        self.status = status
        self.progress = progress

        # This way, both processes will be performed on the images marked as 'single'
        if 'coat' in self.phase or 'single' in self.phase:
            image_coat = self.image_raw.copy()
            self.analyze_coat(image_coat)
        if 'scan' in self.phase or 'single' in self.phase:
            image_scan = self.image_raw.copy()
            self.analyze_scan(image_scan)

        # Save all the reports to their respective json files
        for report_name in self.part_colours.keys():
            with open('%s/reports/%s_report.json' % (self.build['ImageCapture']['Folder'], report_name),
                      'w+') as report:
                json.dump(self.defect_dict[report_name], report, indent=4, sort_keys=True)

    def analyze_coat(self, image_coat):
        """Analyzes the coat image for any potential defects as listed below"""

        self.progress.emit(0)

        # Bright spot defects will be drawn in red
        image_coat = self.detect_bright_spots(image_coat)
        self.progress.emit(20)

        # Blade streak defects will be drawn in blue
        image_coat = self.detect_blade_streaks(image_coat)
        self.progress.emit(40)
        # Blade chatter defects will be drawn in green
        image_coat = self.detect_blade_chatter(image_coat)
        self.progress.emit(60)
        # Contrast difference defects will be drawn in yellow
        image_coat = self.detect_contrast_difference(image_coat)

        self.progress.emit(80)
        if self.compare_flag:
            self.compare_histogram(self.image_raw, self.image_previous)

        # Save the analyzed coat image with all the defects on it to the correct folder
        cv2.imwrite('%s/defects/%s/%sD_%s.png' % (self.build['ImageCapture']['Folder'], self.phase, self.phase,
                                                  self.layer), image_coat)
        self.progress.emit(100)

    def analyze_scan(self, image_scan):
        """Analyzes the scan image for any potential defects as listed below"""

        self.progress.emit(0)
        image_scan = self.detect_blade_streaks(image_scan)
        self.progress.emit(25)
        image_scan = self.detect_blade_chatter(image_scan)
        self.progress.emit(50)
        image_scan = self.detect_scan_pattern(image_scan)
        self.progress.emit(75)
        if self.compare_flag:
            self.compare_histogram(self.image_raw, self.image_previous)

        # Save the analyzed scan image with all the defects on it to the correct folder
        cv2.imwrite('%s/defects/%s/%sD_%s.png' % (self.build['ImageCapture']['Folder'], self.phase, self.phase,
                                                  self.layer), image_scan)
        self.progress.emit(100)

    def detect_bright_spots(self, image):
        """Detects any spots in the image that are above a certain contrast threshold, aka are too bright"""

        # Save a copy of the original defect image
        image_defects = self.image_raw.copy()
        image_defects_clahe = ImageTransform.clahe(image_defects, gray_flag=True)

        # Otsu's Binarization is used to calculate a threshold value to be used to get a proper threshold image
        retval = cv2.threshold(image_defects_clahe, 0, 255, cv2.THRESH_OTSU)[0]
        image_threshold = cv2.threshold(image_defects_clahe, retval * 1.85, 255, cv2.THRESH_BINARY)[1]

        # Change the colour of the pixels in the original image to red if they're above the threshold
        image_defects[image_threshold == 255] = COLOUR_RED

        self.report_defects(image_defects, COLOUR_RED, 'Bright Spots')

        return self.overlay_defects(image, image_defects, COLOUR_RED)

    def detect_blade_streaks(self, image):
        """Detects any horizontal lines on the image, doesn't work as well in the darker areas"""

        image_defects = self.image_raw.copy()
        image_defects_clahe = ImageTransform.clahe(image_defects, gray_flag=True)

        # Add a gaussian blur to the clahe image
        image_defects_clahe = cv2.GaussianBlur(image_defects_clahe, (15, 15), 0)

        # Use a Sobel edge finder to find just the edges in the X plane (horizontal lines)
        image_edges = cv2.Sobel(image_defects_clahe, cv2.CV_8UC1, 0, 1)

        # Remove any unclear or ambiguous results, leaving only the distinct edges
        image_edges = cv2.threshold(image_edges, 20, 255, cv2.THRESH_BINARY)[1]
        image_edges = cv2.dilate(image_edges, np.ones((1, 20), np.uint8), iterations=1)
        image_edges = cv2.erode(image_edges, np.ones((1, 20), np.uint8), iterations=3)

        # a list consisting 2 points that forms a line matching the variables
        lines = cv2.HoughLinesP(image_edges, 1, np.pi / 180, threshold=100, minLineLength=1000, maxLineGap=500)

        # Draw blue lines (representing the blade streaks) on the defect image
        for index in range(len(lines)):
            for x1, y1, x2, y2 in lines[index]:
                # Only draw horizontal lines that are not located near the top or bottom of image
                if abs(y1 - y2) == 0 and 20 < y1 < image_defects.shape[0] - 20:
                    cv2.line(image_defects, (x1, y1), (x2, y2), COLOUR_BLUE, 2)

        self.report_defects(image_defects, COLOUR_BLUE, 'Blade Streaks')

        return self.overlay_defects(image, image_defects, COLOUR_BLUE)

    def detect_blade_chatter(self, image):
        """Detects any vertical lines on the image that are caused as a result of blade chatter
        Done by matching any chatter against a pre-collected set of blade chatter templates"""

        image_defects = self.image_raw.copy()
        image_defects_clahe = ImageTransform.clahe(image_defects, gray_flag=True, cliplimit=3.0, tilegridsize=(12, 12))

        # Load the chatter template images into memory in grayscale
        chatter_templates = list()
        for filename in os.listdir('%s/templates' % self.build['WorkingDirectory']):
            chatter_templates.append(cv2.imread('%s/templates/%s' % (self.build['WorkingDirectory'], filename), 0))

            for template in chatter_templates:
                # Look for the template in the original image
                result = cv2.matchTemplate(image_defects_clahe, template, cv2.TM_CCOEFF_NORMED)

                # Find the coordinates of the results which are above a set threshold
                coordinates = np.where(result >= 0.4)
                coordinate_previous = [0, 0]

            # Draws a box around the matching points
            for coordinate in zip(*coordinates[::-1]):
                # This conditional prevents stacking of multiple boxes on the one spot due to a low threshold value
                if abs(coordinate[1] - coordinate_previous[1]) > 50:
                    cv2.rectangle(image_defects, (coordinate[0], coordinate[1]),
                                  (coordinate[0] + template.shape[1], coordinate[1] + template.shape[0]),
                                  COLOUR_GREEN, thickness=3)
                    coordinate_previous = coordinate
                    self.chatter_count += 1

        self.report_defects(image_defects, COLOUR_GREEN, 'Blade Chatter')

        return self.overlay_defects(image, image_defects, COLOUR_GREEN)

    def detect_contrast_difference(self, image):
        """Detects any areas of the image that are too bright or dark compared to the average contrast
        Use this until detect_dark_spots is fixed and working sufficiently"""

        image_defects = self.image_raw.copy()

        # Otsu's Binarization is used to calculate a threshold value and image
        image_defects_gray = cv2.cvtColor(image_defects, cv2.COLOR_BGR2GRAY)
        retval, image_threshold = cv2.threshold(image_defects_gray, 0, 255, cv2.THRESH_OTSU)

        # Clean up the image threshold by removing any noise (opening/closing holes)
        kernel = cv2.getStructuringElement(cv2.MORPH_ERODE, (5, 5))
        image_threshold = cv2.erode(image_threshold, kernel, iterations=3)
        for index in range(7):
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * index + 1, 2 * index + 1))
            image_threshold = cv2.morphologyEx(image_threshold, cv2.MORPH_CLOSE, kernel, iterations=3)
            image_threshold = cv2.morphologyEx(image_threshold, cv2.MORPH_OPEN, kernel, iterations=3)

        # image_white is the section of image_defects that are white in the created threshold
        # image_black is the opposite
        image_white = cv2.bitwise_and(image_defects, image_defects, mask=image_threshold)
        image_black = cv2.bitwise_and(image_defects, image_defects, mask=cv2.bitwise_not(image_threshold))

        # Ignore the right edge of the build platform (defects there don't matter)
        image_black[:, image_defects.shape[1] - 20:] = COLOUR_BLACK

        # Outer ring bright spots, set these in the defect image to yellow
        image_outer = cv2.threshold(image_black, retval * 1.32, 255, cv2.THRESH_BINARY)[1]
        image_defects[np.where((image_outer == COLOUR_WHITE).all(axis=2))] = COLOUR_YELLOW

        # Outer ring shadows
        image_outer_shadow = cv2.threshold(image_black, retval * 0.7, 255, cv2.THRESH_BINARY_INV)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_ERODE, (5, 5))
        image_outer_shadow = cv2.erode(image_outer_shadow, kernel, iterations=5)
        image_outer_shadow = cv2.bitwise_or(image_defects, image_outer_shadow)
        image_outer_shadow = cv2.threshold(image_outer_shadow, retval * 0.5, 255, cv2.THRESH_TOZERO_INV)[1]
        image_defects[np.where((image_outer_shadow != COLOUR_BLACK).all(axis=2))] = COLOUR_YELLOW
        image_defects[np.where((image_black == COLOUR_WHITE).all(axis=2))] = COLOUR_YELLOW

        # Inner ring bright spots
        image_inner = cv2.threshold(image_white, retval * 1.7, 255, cv2.THRESH_BINARY)[1]
        image_defects[np.where((image_inner == COLOUR_WHITE).all(axis=2))] = COLOUR_YELLOW

        # Inner ring shadows
        image_inner_shadow = cv2.threshold(image_white, retval * 0.95, 255, cv2.THRESH_TOZERO_INV)[1]
        image_defects[np.where((image_inner_shadow != COLOUR_BLACK).all(axis=2))] = COLOUR_YELLOW

        self.report_defects(image_defects, COLOUR_YELLOW, 'Contrast Difference')

        return self.overlay_defects(image, image_defects, COLOUR_YELLOW)

    def detect_scan_pattern(self, image):
        """Detects any scan patterns on the image and draws them as filled contours"""

        image_defects = self.image_raw.copy()
        image_defects_gray = cv2.cvtColor(image_defects, cv2.COLOR_BGR2GRAY)
        image_defects_gray = cv2.GaussianBlur(image_defects_gray, (27, 27), 0)
        image_edges = cv2.Laplacian(image_defects_gray, cv2.CV_64F)

        for index in range(3):
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * index + 1, 2 * index + 1))
            image_edges = cv2.morphologyEx(image_edges, cv2.MORPH_CLOSE, kernel)
            image_edges = cv2.morphologyEx(image_edges, cv2.MORPH_OPEN, kernel)

        #image_edges = cv2.morphologyEx(image_edges, cv2.MORPH_CLOSE, kernel, iterations=3)
        #image_edges = cv2.erode(image_edges, cv2.getStructuringElement(cv2.MORPH_ERODE, (5, 5)), iterations=1)
        image_edges = cv2.convertScaleAbs(image_edges)

        # Find the contours using the cleaned up image
        contours = cv2.findContours(image_edges, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)[1]
        contours_list = list()

        # Check if the contours are larger than a preset threshold
        for contour in contours:
            if cv2.contourArea(contour) > 1000:
                contours_list.append(contour)

        # Draw the contours on the original image
        cv2.drawContours(image_defects, contours_list, -1, COLOUR_PURPLE, thickness=cv2.FILLED)

        if self.contours_flag:
            self.compare_overlay(image_defects, self.image_contours)

        return self.overlay_defects(image, image_defects, COLOUR_PURPLE)

    def report_defects(self, image_defects, defect_colour, defect_type):

        # Only do this method if an overlay is available in the first place
        if self.contours_flag:

            size, coordinates = self.find_coordinates(image_defects, self.image_contours, COLOUR_BLACK, defect_colour)
            if size > 0:
                self.defect_dict['background'][self.layer][self.phase][defect_type] = [size] + coordinates
                self.defect_dict['combined'][self.layer][self.phase][defect_type] = [size]
                self.defect_dict['combined'][self.layer][self.phase][defect_type].append(coordinates)
            else:
                self.defect_dict['background'][self.layer][self.phase][defect_type] = [0]
                self.defect_dict['combined'][self.layer][self.phase][defect_type] = [0]

            for part_name, part_colour in self.part_colours.items():
                # Skip the background or combined keys as they are already processed as a byproduct of the other parts
                if 'background' in part_name or 'combined' in part_name:
                    continue

                # For each part, find the coordinates and total size of the defect pixels that overlap the part
                size, coordinates = self.find_coordinates(image_defects, self.image_contours,
                                                          tuple(part_colour), defect_colour)

                if size > 0:
                    # Add these to the defect dictionary for the current part, and the combined dictionary
                    self.defect_dict[part_name][self.layer][self.phase][defect_type] = [size] + coordinates
                    self.defect_dict['combined'][self.layer][self.phase][defect_type][0] += size
                    self.defect_dict['combined'][self.layer][self.phase][defect_type].append(coordinates)
                else:
                    self.defect_dict[part_name][self.layer][self.phase][defect_type] = [0]

    def compare_overlay(self, image_scan, image_contours):
        """Compares the detected scan pattern image against the part contours image using template matching"""

        # Convert all the part colours from teal into purple so that it can be compared to the detected scan pattern
        mask = cv2.inRange(image_contours, (100, 100, 0), (255, 255, 0))
        image_contours[np.nonzero(mask)] = COLOUR_PURPLE

        # Use template matching to compare the two images and save the result to the combined report
        result = cv2.matchTemplate(image_scan, image_contours, cv2.TM_CCOEFF_NORMED)[0][0]
        self.defect_dict['combined'][self.layer][self.phase]['Overlay Comparison'] = float(result)

    def compare_histogram(self, image_current, image_previous):
        """Compares the histogram of each method and calculates the difference result"""

        hist_current = cv2.calcHist([image_current], [0], None, [256], [0, 256])
        hist_previous = cv2.calcHist([image_previous], [0], None, [256], [0, 256])

        # To be tested to see if this improves or does anything to the result
        # cv2.normalize(hist_current, hist_current)
        # cv2.normalize(hist_previous, hist_previous)

        # Lots of methods to compare histograms and to calculate histograms itself
        # To be further tested for the best options
        result = cv2.compareHist(hist_current, hist_previous, cv2.HISTCMP_KL_DIV)

        # Result of KL_DIV comparing a completely black image to a completely white image - 325853401.3861952
        # Converting the result to a percentage based on this complete non-match number
        # result = (325853401.3861952 - result) / 325853401.3861952 * 100

        self.defect_dict['combined'][self.layer][self.phase]['Histogram Comparison'] = result

    @staticmethod
    def overlay_defects(image, image_defects, defect_colour):
        """Applies any solid defect pixel colours (depending on the defect being overlaid) to the first image"""
        image_mask = cv2.inRange(image_defects, defect_colour, defect_colour)
        if cv2.countNonZero(image_mask) > 0:
            image[np.nonzero(image_mask)] = defect_colour
        return image

    @staticmethod
    def find_coordinates(image_defects, image_overlay, part_colour, defect_colour):
        """Determines the coordinates of any defects (coloured pixels) and whether they overlap with the part contours
        Because reporting the coordinates of every pixel will yield an incredibly long list...
        The centre coordinates of each 'defect blob' is reported instead"""

        # Create a mask of each part using their respective colour
        mask = cv2.inRange(image_overlay, part_colour, part_colour)

        # Because the colour causes some noise in the mask due to gradients, close and remove any white noise
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))

        # Overlay the defect image with the created mask of the part in question
        image_overlap = cv2.bitwise_and(image_defects, image_defects, mask=mask)

        # Find all the coloured defect pixels in the overlap image (outputs an image of the red pixels)
        image_overlap = cv2.inRange(image_overlap, defect_colour, defect_colour)

        # Find the number of overlapping pixels as outputted by the above function
        size = cv2.countNonZero(image_overlap)

        # Group any large blobs of red pixels and find the contours of them
        contours = cv2.findContours(image_overlap, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

        # For each contour found, if the size of the contour exceeds a certain amount, find its centre coordinates
        coordinates = list()
        for contour in contours:
            if cv2.contourArea(contour) > 50:
                (x, y) = cv2.minEnclosingCircle(contour)[0]
                coordinates.append((int(x), int(y)))

        return size, coordinates

    @staticmethod
    def defect_size(image):
        """Returns the number of pixels that fall between the set range of colours"""
        return cv2.countNonZero(cv2.inRange(image, np.array([0, 0, 200]), np.array([100, 100, 255])))

    @staticmethod
    def split_colour(image, colour):
        """Returns two images, one of just the received colour and one of the background without the colour"""

        mask = cv2.inRange(image, colour, colour)
        foreground = cv2.bitwise_and(image, image, mask=mask)
        background = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
        return foreground, background

    # The following methods are still works in progress and will need further testing

    # TODO To be fixed, improved, tested and implemented
    def detect_dark_spots(self):
        """Also picks up dark areas caused by uneven or bad lighting"""
        image_defects = self.image_raw.copy()
        eq = self.clahe(image_defects)
        retval = cv2.threshold(eq, 0, 255, cv2.THRESH_OTSU)[0]
        _, threshold = cv2.threshold(eq, retval * 0.25, 255, cv2.THRESH_BINARY_INV)
        image_defects[threshold == 255] = COLOUR_RED
        self.overlay_defects(self.image_coat, image_defects)

        # # checks if the defect overlaps with scan
        # # change color= if uses different color for layer contour
        # def slice_overlap(self, defect, color=(128, 128, 0)):
        #     # creates a mask containing only the scan lines
        #     mask = cv2.inRange(self.layer, color, color)
        #     # getting the part of defect image that overlaps with the layout
        #     overlay = cv2.bitwise_and(defect, defect, mask=mask)
        #     # find all pixels that are red
        #     found = cv2.inRange(overlay, COLOR_RED, COLOR_RED)
        #     return cv2.countNonZero(found) > 10

    # TODO Should work better if able to mask out corners
    def detect_dosing_error(self):
        image_defects = self.image_raw.copy()
        image_defects_gray = cv2.cvtColor(image_defects, cv2.COLOR_BGR2GRAY)
        retval = cv2.threshold(image_defects_gray, 0, 255, cv2.THRESH_OTSU)[0]
        image_threshold = cv2.threshold(image_defects, retval * 0.6, 255, cv2.THRESH_BINARY_INV)[1]
        image_threshold[:, : image_defects.shape[1] / 2] = COLOUR_BLACK
        image_defects[np.where((image_threshold == COLOUR_WHITE).all(axis=2))] = COLOUR_RED

        self.overlay_defects(self.image_coat, image_defects)
