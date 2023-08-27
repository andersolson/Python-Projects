import geopandas as gpd
import os

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define variables and environments
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Location for shapefiles
shpInPath = r'D:\Projects\WORKING\ML\vectors\SamplePNTS\shp'

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
    gpRead = gpd.read_file(shp)
    if len(gpRead) < 70:
        # Get the name of the file
        shpName = shp.split('\\')
        name = (shpName[-1].split('.', 1)[0])
        print("{0} less than 70 sample points!".format(name))
    elif len(gpRead) >= 70:
        pass
    else:
        print("Errors {0}".format(shp))
