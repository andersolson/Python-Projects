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

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Pull Firebreak label names from directory name of images. Called in ImageDataLoaders.from_path_func()
def label_func(x): return x.parent.name

# Function for making predictions
def seeress(jpgIn, model):

    # List for storing classification results
    sResult = []

    # Test the jpg initiates before sending them to the high oracle. Shun all who are found to be emtpy and worthless.
    try:
        im = Image.open(jpgIn)
        print(f'Processing: {jpgIn}')

        # Pull out image id
        imageID = jpgIn.stem
        # print(imageID)

        # Make the prediction
        pred_class, pred_idx, outputs = model.predict(jpgIn)

        # Extract the probabilities for 'water' and 'wildland' classes
        water_prob = outputs[0].item()
        wildland_prob = outputs[1].item()

        # Append the results to the list
        sResult.append([imageID, pred_class, water_prob, wildland_prob])

        #The sResult list is nested, so the first position Item at [0] is the classification info we want
        return sResult[0]

    except IOError:
        imageID = str(os.path.basename(jpgIn))
        #failedJpg.append(imageID[:-4])
        print(f'Cannot open image file: {jpgIn}')

# Function for making predictions with concurrent futures
def oracle(jpgIn):

    # List for storing the output results of predictions
    oResult   = []

    # Load the pretrained Wildland and Water cnn model. The Seeress is summoned.
    wwModel = load_learner(
        r'D:\Projects\Github\SAGIS-Risk\1 Natural Hazards\1 Wildfire\Firebreak_Enhancement\dev\fastai_models\wildlandwater_resnet18.pkl',
        cpu=True)

    # Test the jpg initiates before sending them to the high oracle. Shun all who are found to be emtpy and worthless.
    try:
        im = Image.open(jpgIn)
        print(f'Processing: {jpgIn}')

        # Pull out image id
        imageID = jpgIn.stem

        # Make the prediction
        pred_class, pred_idx, outputs = wwModel.predict(jpgIn)

        # Extract the probabilities for 'water' and 'wildland' classes
        water_prob = outputs[0].item()
        wildland_prob = outputs[1].item()

        # Test for none type
        if not [x for x in (imageID, pred_class, water_prob, wildland_prob) if x is None]:

            # Append the results to the list
            oResult.append([imageID, pred_class, water_prob, wildland_prob])

            # The oResult list is nested, so the first position Item at [0] is the classification info we want
            return oResult[0]

        else:
            print(f'None Type found in: {jpgIn}')

            null = 'NULL'

            # Append the results to the list
            oResult.append([null, null, null, null])

            # The oResult list is nested, so the first position Item at [0] is the classification info we want
            return oResult[0]

    except IOError:
        imageID = str(os.path.basename(jpgIn))
        #failedJpg.append(imageID[:-4])
        print(f'Cannot open image file: {jpgIn}')


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Run Script
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

if __name__ == "__main__":

    print(f"Process started at {dt.now()}")

    # Define location of images to be labeled
    imagesDir = r'D:\Projects\WORKING\ML\imagery\tmp\TestImages'
    data_dir = pathlib.Path(imagesDir)
    files = get_image_files(data_dir) #is recursive for water & wildland subdirs

    # Start time tracker
    start_time = time.perf_counter()

    ''' Seeress Summoning Ritual '''

    # # Define the path to output the CSV file
    # csv_path = r'D:\Projects\WORKING\ML\Test_Results_Table_1.csv'
    #
    # # Load the pretrained Wildland and Water cnn model. The Seeress is summoned.
    # wwModel = load_learner(
    #     r'D:\Projects\Github\SAGIS-Risk\1 Natural Hazards\1 Wildfire\Firebreak_Enhancement\dev\fastai_models\wildlandwater_resnet18.pkl',
    #     cpu=True)
    #
    # # Run predictions on jpg files in directory using joblib
    # results = Parallel(n_jobs=10)(delayed(seeress)(jpg,wwModel) for jpg in files)
    #
    # # Write the results to the CSV file
    # with open(csv_path, "w", newline="") as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(["Image Name", "Label", "Water Probability", "Wildland Probability"])  # Write the header
    #     writer.writerows(results)  # Write the data rows

    ''' Oracle Summoning Ritual '''

    # Assemble the line of suplicants
    images = [jpg for jpg in files]

    with cf.ProcessPoolExecutor(7) as executor:

        # Run predictions on jpg files in directory using concurrent futures
        results = executor.map(oracle,images)

    # Define the path to output the CSV file
    csv_path = r'D:\Projects\WORKING\ML\Test_Results_Table_3.csv'

    # Write the results to the CSV file
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Image Name", "Label", "Water Probability", "Wildland Probability"])  # Write the header
        writer.writerows(results)  # Write the data rows

    # Time tracker for finish
    finish_time = time.perf_counter()

    print(f"Program finished in {finish_time - start_time} seconds")