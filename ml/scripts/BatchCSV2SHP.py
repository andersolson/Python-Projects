import geopandas as gpd
import pandas as pd
import os


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define variables and environments
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

csvInPath   = r'D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\ReDo\TestPoints'
shpOutPath  = r'D:\Projects\WORKING\ML\vectors\SamplePNTS\shp'

#List to store path locations of csv files
csvFileLst = []

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

def CSV2SHP(Infile, Outdir):
    # Get the name of the file
    csvName = Infile.split('\\')
    name = (csvName[-1].split('.',1)[0])

    # Read and store content
    # of a csv file
    read_file = gpd.read_file(Infile)

    # Add geometry to csv file
    gdfPoints = gpd.GeoDataFrame(read_file, geometry=gpd.points_from_xy(read_file.POINT_X, read_file.POINT_Y, crs="EPSG:4326"))

    # Write the dataframe object
    # into shp file
    gdfPoints.to_file('{0}\{1}.shp'.format(Outdir,name))
    print('Finished:\n{0}\{1}.shp\n'.format(Outdir, name))


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Call Functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##


#Run myFileLocations() function to find all csv files
myFileLocations(".csv", csvInPath , csvFileLst)
#print(csvFileLst)

# Export csv as shapefiles
for fName in csvFileLst:
    CSV2SHP(fName,shpOutPath)