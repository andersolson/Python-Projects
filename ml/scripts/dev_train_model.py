from fastai.vision.all import *
import pathlib
import os
from matplotlib import rcParams
from torchvision import models

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define local variables and environments
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Directory location of training data jpg tiles
tileDir = r'D:\Projects\WORKING\ML\imagery\training_water_wildland'

# Name directory to training data as a Path variable
data_dir = pathlib.Path(tileDir)

# Get the image files found in the training data path location
files = get_image_files(data_dir)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Pull Firebreak label names from directory name of images. Called in ImageDataLoaders.from_path_func()
def label_func(x): return x.parent.name

# Summarize label names found in each label directory and the count of images in each label directory
def data_summary(imgDir):
    print(f'Path to training data directory:\n\t{imgDir}')

    # Iterate over the subdirectories
    for foldername in os.listdir(imgDir):
        folderpath = os.path.join(imgDir, foldername)

        # Check if the item is a directory
        if os.path.isdir(folderpath):
            # Count the number of JPG files in the folder
            jpg_count = sum(1 for filename in os.listdir(folderpath) if filename.lower().endswith(".jpg"))

            # Print the folder name and JPG count
            print(f"{foldername}: {jpg_count} JPG file(s)")

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Run Script
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

if __name__ == "__main__":

    # Print out metrics for input data
    data_summary(data_dir)

    # Data Loader:
    dls = ImageDataLoaders.from_path_func(data_dir, files, label_func, item_tfms=Resize(224), valid_pct=0.2, seed=42, bs=64)

    # Label List
    print(f'There are {dls.c} categories: {dls.vocab}')

    # From jupyter notebook: `cnn_learner` has been renamed to `vision_learner` -- please update your code
    #learn = cnn_learner(dls,resnet18, metrics=[error_rate,accuracy],loss_func=LabelSmoothingCrossEntropy(),path='.models').to_fp16()
    learn = vision_learner(dls,resnet18, metrics=[error_rate,accuracy],loss_func=LabelSmoothingCrossEntropy(),path='.models').to_fp16()

    # Find the best learning rate for the model
    # e.g. : SuggestedLRs(minimum=0.03630780577659607, steep=7.585775892948732e-05, valley=0.0008317637839354575, slide=0.009120108559727669)
    lrs = learn.lr_find(suggest_funcs=(minimum, steep, valley, slide))

    # Prints: Steepest Point: 1.32e-04
    print(f"Steepest Point: {lrs[1]:.2e}")

    #learn.recorder.plot()
    learn.recorder.plot_lr_find()

    # Display the chart and manually save if desired
    #plt.show()

    # Begin the learning process
    callbacks = [SaveModelCallback(fname='fire_break_model'), CSVLogger(append=True)]
    learn.fine_tune(10, freeze_epochs=3, base_lr=lrs[1], cbs=callbacks)

    rcParams['figure.figsize'] = (12, 12)
    interp = ClassificationInterpretation.from_learner(learn)
    interp.plot_confusion_matrix(figsize=(12, 12), dpi=60)

    #plt.show()

    interp.print_classification_report()

    learn.export('wildlandwater_resnet18.pkl')
    learn.export(r'D:\Projects\Github\SAGIS-Risk\1 Natural Hazards\1 Wildfire\Firebreak_Enhancement\dev\fastai_models\wildlandwater_resnet18.pkl')