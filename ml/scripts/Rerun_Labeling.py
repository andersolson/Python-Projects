import os
import csv
import pathlib
from pathlib import Path
from fastai.vision.all import *
from PIL import Image
import time
from joblib import Parallel, delayed
from datetime import datetime as dt
import concurrent.futures as cf
from pandas import *

# Sample class with init method
class rerunImages:

    # init method or constructor
    def __init__(self, jpgPath, csvPath):
        self.jpgPath = jpgPath
        self.csvPath = csvPath

    def cntImages(self):
        # Get image file paths
        jpgFiles = get_image_files(self.jpgPath)

        # Total number of jpg images found
        jpgTot = len(jpgFiles)
        print(f'{jpgTot} images found.')

    def cntRows(self):
        print(f'CSV location: {self.csvPath}')



if __name__ == "__main__":

    print(f"Process started at {dt.now()}")

    # Start time tracker
    start_time = time.perf_counter()

    # Define path location variable for images
    #jpgDir = r'L:\layergen-processing\FirebreakML\Firebreak_Water_wildland\imagery\FL_Water_Wildland'
    jpgDir   = r'D:\Projects\WORKING\ML\imagery\tmp\TestImages'
    jpgPath  = pathlib.Path(jpgDir)

    # Define path location variable for csv prediction table
    csvDir   = r'D:\Projects\WORKING\ML\prediction_tables\FL_Results_Table0.csv'
    csvPath  = pathlib.Path(csvDir)

    p = rerunImages(jpgPath,csvPath)
    p.cntImages()
    p.cntRows()

    # Time tracker for finish
    finish_time = time.perf_counter()

    print(f"Program finished in {finish_time - start_time} seconds")


    # # Return a list of JPG file paths for images that were missed the 1st time
    # def findMissingID(jpgFileLst,csvFile):
    #     jpgID = []
    #
    #     # Loop through the jpgFileLst and extract the ID
    #     for x in jpgFileLst:
    #         jpgID.append(str(x.stem))
    #
    #     #print(jpgID)
    #
    #     # read CSV file
    #     data = read_csv(csvFile)
    #
    #     # pull ID column
    #     csvID = data['Image Name'].tolist()
    #     #print('Image Name:', ID)
    #
    #     missingIds = list(jpgID - csvID)
    #
    #     print(missingIds)
    #     print(len(missingIds))
    #
    #
    # # Line-by-line function to write prediction results to a csv
    # def myCSVwrite(prediction, csvIn):
    #     #print(prediction)
    #     #print(csvIn)
    #
    #     # Test for none type
    #     if not [x for x in (prediction) if x is None]:
    #
    #         # Write the results to the CSV file
    #         with open(csvIn, "a", newline="") as csvfile:
    #             writer = csv.writer(csvfile)
    #             writer.writerow(prediction)
    #
    #     else:
    #         print(f'None Type found in: {prediction[0]}')
    #
    #         null = ['NULL','NULL','NULL','NULL']
    #
    #         # Write NULL to the CSV file
    #         with open(csvIn, "a", newline="") as csvfile:
    #             writer = csv.writer(csvfile)
    #             writer.writerow(null)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Run Script
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# if __name__ == "__main__":
#
#     print(f"Process started at {dt.now()}")
#
#     # Start time tracker
#     start_time = time.perf_counter()
#
#     # Define path location variable for images
#     #imagesDir = r'L:\layergen-processing\FirebreakML\Firebreak_Water_wildland\imagery\FL_Water_Wildland'
#     jpgDir   = r'D:\Projects\WORKING\ML\imagery\tmp\TestImages'
#     jpgPath  = pathlib.Path(jpgDir)
#     jpgFiles = get_image_files(jpgPath)
#
#     # Define path location variable for csv prediction table
#     csvDir   = r'D:\Projects\WORKING\ML\prediction_tables\FL_Results_Table0.csv'
#     csvPath  = pathlib.Path(csvDir)
#
#     obj = rerunImages(jpgFiles,csvPath)
#     obj.cntImages()
#
#     #findMissingID(files, csv_path)
#
#     # Time tracker for finish
#     finish_time = time.perf_counter()
#
#     print(f"Program finished in {finish_time - start_time} seconds")


