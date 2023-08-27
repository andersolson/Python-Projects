import os
import geopandas as gpd
from datetime import datetime as dt

# jpgDirectory = r'L:\FirebreakML\Firebreak_Water_wildland\imagery\WY_Water_Wildland'
# zipSHP       = r'L:\FirebreakML\Firebreak_Water_wildland\WY_WW_Merge.zip'

jpgDirectory = r'D:\Projects\WORKING\ML\imagery\CO_Water_Wildland\wildland'
zipSHP       = r'L:\FirebreakML\Firebreak_Water_wildland\CO_WW_Merge.zip'

gdf          = gpd.read_file(zipSHP)
shpID_list   = gdf['ID'].tolist()
jpgID_list   = []
output_file  = r'D:\Projects\WORKING\ML\imagery\CO_missing_files.txt'

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Function pulls image ID from the filename and writes it to a list
def myFileLocations(jpgDirectory, inLST):
    fileEnding = '.jpg'
    # Loop the directory and subdirectories for all .jpg file endings and store them in a list
    for root, dirs, files in os.walk(jpgDirectory):
        for file in files:
            if file.endswith(fileEnding):
                imageID = file[:-4]
                inLST.append(imageID)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Run Script
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Start a timer
startTime = dt.now()

# SHP ids written to list with geopandas command: gdf['ID'].tolist()
print('Total number of grid cells: {0}'.format(len(shpID_list)))

# Create a new list of image IDs pulled from directory of JPG filenames
myFileLocations(jpgDirectory, jpgID_list)
print('Total number of jpg images: {0}'.format(len(jpgID_list)))

# To get IDs which are in shpID_list (shapefile) but not in jpgID_list (folder directory)
missing_files = list(shpID_list - jpgID_list)
#print(missing_files)

# Print the missing file names
print('Total number of missing jpg images: {0}'.format(len(missing_files)))

# Write the missing file names to a text file
with open(output_file, "w") as file:
    file.write(str(missing_files))
file.close()

print(f'Process finished! Runtime: {dt.now()-startTime}')