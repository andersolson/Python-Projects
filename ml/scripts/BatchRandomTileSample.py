import geopandas as gpd
import random
import os

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define variables and environments
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Location for shapefiles
shpInPath  = r'D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_Select'
shpOutPath = r'D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_Labels'

#List to store path locations of shp files
shpFileLst = []

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

def myFileLocations (fileEnding, directory, inLST):
    #Loop the directory and subdirectories for all .shp file endings and store them in a list
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(fileEnding):
                inLST.append(os.path.join(root, file))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Call Functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

#Run myFileLocations() function to find all csv files
myFileLocations(".shp", shpInPath , shpFileLst)
#print(shpFileLst)

for shp in shpFileLst:

    # Get the file name
    shpName = shp.split('\\')
    name = (shpName[-1].split('.', 1)[0])
    print("Running {0}...".format(name))

    # Read shapefile
    gpRead = gpd.read_file(shp)

    # Get the total count of features in shapefile
    r = len(gpRead)

    try:
        # Generate 70 unique random numbers within a range of the feature count
        num_list = random.sample(range(0, r), 75)
        print(num_list)

        # Create selection from query on row/index number
        gdfQuery = gpRead.iloc[num_list]

        print(len(gdfQuery))

        # Export to shapefile
        gdfQuery.to_file(r'{0}/{1}.shp'.format(shpOutPath,name))

    except:
        print("\tError Revisit: {0}\n".format(name))