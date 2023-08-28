#---------------------------------------------------------------------------
# FindSHPs.py
#
# Author: Anders Olson
#
# Usage:  Requires arcpy and python 3, can be run stand-alone
#
# Description: Script runs through a directory to find all files of a specified
#              file ending. Each file that is found has its path stored in a list.
#              The list of path locations is used in a for-loop in to run Dissolve
#              geoprocessing task using arcpy.
# ---------------------------------------------------------------------------

import os
import arcpy

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define variables and environments
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Set the arcpy overwriteOutput ON
arcpy.gp.overwriteOutput = True

# Set the workspace
arcpy.env.workspace = "in_memory"
ScratchGDB = arcpy.env.scratchGDB

print("Scratch folder is: {}".format(ScratchGDB))

#File Directory to search through
#shpRootFolder = r"K:\3 Risk\1 Natural Hazards\2 Coastal\Storm Surge\zz_Archive\Storm_Surge_2019_04"
shpRootFolder = r"C:\Users\andolson\Documents\WORKING\Firebreak\Data\Firebreak_Diablo"

#List to store path locations of .shp files
myShapesLst = []

#List to store FIPSSTCO codes for dissolved shapefiles
lstFIPSSTCO = []

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

'''
Summary: Find all shape files in a directory and write their location to a list

Inputs:
fileEnding -- The file ending to search recursively for
directory  -- The root folder to search through recursively
inLST      -- The list for storing file locations

Outputs:
None       -- No output returned, but inLST is populated with .shp path locations

'''

def myFileLocations (fileEnding, directory, inLST):
    #Loop the directory and subdirectories for all .shp file endings and store them in a list
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(fileEnding):
                inLST.append(os.path.join(root, file))

'''
Summary: Add a temporary field to all shapefiles, populate the temp field, delete old field, rename the temp field 

Inputs:
mySHPfiles -- The path location of all shapefiles to change

Outputs:
fipsLST    -- Returns a list of fipsstco codes that were dissolved. Shapefiles are 
              dissolved and then saved to scratch location.

'''

def fieldCalc(mySHPfiles):

    for shapeFile in mySHPfiles:
        print('\t' + shapeFile)

        # Add temp field for Long Integer data type
        arcpy.management.AddField(shapeFile, "temp", "LONG")

        # Populate temp field with text string as an int
        arcpy.management.CalculateField(shapeFile, "temp", '!TCMULTIPLY!', "PYTHON3")

        # Delete old field
        arcpy.management.DeleteField(shapeFile, 'TCMULTIPLY')

        # Add new field for Long Integer data type
        arcpy.management.AddField(shapeFile, 'TCMULTIPLY', "LONG")

        # Populate new field with text string as an int
        arcpy.management.CalculateField(shapeFile, 'TCMULTIPLY', '!temp!', "PYTHON3")

        # Rename temp field with old field name
        #arcpy.management.AlterField(shapeFile, 'temp', 'TCMULTIPLY')

        # Delete temp field
        #arcpy.management.DeleteField(shapeFile, 'temp')


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Call Functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

#Run myFileLocations() function
myFileLocations(".shp", shpRootFolder, myShapesLst)
print(myShapesLst)

#Run fieldCalc() function
fieldCalc(myShapesLst)
print("All Done.")