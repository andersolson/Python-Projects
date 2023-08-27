import csv
import os
import pathlib
from pathlib import Path
from fastai.vision.all import *
from PIL import Image
from datetime import datetime as dt

# Define location of images to be labeled
imagesDir = r'D:\Projects\WORKING\ML\imagery\tmp\TestImages'
data_dir  = pathlib.Path(imagesDir)
#files     = get_image_files(data_dir/"wildland")
files = get_image_files(data_dir) #is recursive

# Define the path to the CSV file
csv_path = r'D:\Projects\WORKING\ML\Test_Results_Table_0.csv'

# Define tha path to TXT file for storing empty jpg IDs
emptyIDs = r'D:\Projects\WORKING\ML\imagery\CO_empty_Ids.txt'

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Pull Firebreak label names from directory name of images. Called in ImageDataLoaders.from_path_func()
def label_func(x): return x.parent.name


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Run Script
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

#if __name__ == "__main__":

wwModel = load_learner(r'D:\Projects\Github\SAGIS-Risk\1 Natural Hazards\1 Wildfire\Firebreak_Enhancement\dev\fastai_models\wildlandwater_resnet18.pkl', cpu=True)
#wwModel = load_learner(r'D:\Projects\Github\SAGIS-Risk\1 Natural Hazards\1 Wildfire\Firebreak_Enhancement\dev\.models\models\fire_break_model.pth', cpu=True)
#wwModel = load_learner(r'D:\Projects\Github\SAGIS-Risk\1 Natural Hazards\1 Wildfire\Firebreak_Enhancement\dev\.models\wildlandwater_resnet18.pkl')

totalCnt  = len(files)
cnt       = 0
results   = []
failedJpg = []

# Start a timer
startTime = dt.now()

# Loop through all images in a directory and make sure they are not empty before running the prediction
for jpg in files:
    try:
        im = Image.open(jpg)
        # print(jpg)

        # Pull out image id
        imageID = jpg.stem
        # print(imageID)

        # Make the prediction
        pred_class, pred_idx, outputs = wwModel.predict(jpg)

        # Extract the probabilities for 'water' and 'wildland' classes
        water_prob    = outputs[0].item()
        wildland_prob = outputs[1].item()

        # Append the results to the list
        results.append([imageID, pred_class, water_prob, wildland_prob])

        cnt += 1
        print(f'{cnt} of {totalCnt} Complete!')

    except IOError:
        imageID = str(os.path.basename(jpg))
        failedJpg.append(imageID[:-4])
        print(f'Cannot open image file: {jpg}')

# Write the results to the CSV file
with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Image Name", "Label", "Water Probability", "Wildland Probability"])  # Write the header
    writer.writerows(results)  # Write the data rows

# Write the missing file names to a text file
with open(emptyIDs, "w") as file:
    file.write(str(failedJpg))
file.close()

print(f'Process finished! Runtime: {dt.now()-startTime}')