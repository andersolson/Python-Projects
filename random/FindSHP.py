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
shpRootFolder = r"K:\3 Risk\1 Natural Hazards\2 Coastal\Storm Surge\zz_Archive\Storm_Surge_2019_04\Data\VA"

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
Summary: Dissolve all my shapefiles by the "Region" attribute and save the dissolved shapes to
         the Scratch Folder location.  

Inputs:
mySHPfiles -- The file ending to search recursively for

Outputs:
fipsLST    -- Returns a list of fipsstco codes that were dissolved. Shapefiles are 
              dissolved and then saved to scratch location.

'''

def dissolveMyShapes (mySHPfiles, outFIPSlst):

    for shapeFile in mySHPfiles:
        # Get the FIPSCO string from filename
        shpString = shapeFile[-9:]
        #print(shpString)

        # Split the string at '.' to get a list
        shpSplit = shpString.split('.')
        outFIPSlst.append(shpSplit[0])
        #print(shpSplit[0])

        #Output location for dissolve is the scratch folder
        out_feature = ScratchGDB + "\\C{0}".format(shpSplit[0])
        #print(out_feature)

        # Dissolve
        #
        arcpy.Dissolve_management(shapeFile, out_feature, dissolve_field="REGION", statistics_fields="",
                                  multi_part="MULTI_PART", unsplit_lines="DISSOLVE_LINES")

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Call Functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

#Run myFileLocations() function
myFileLocations(".shp", shpRootFolder, myShapesLst)
print(myShapesLst)

#Run dissolceMyShapes() function
dissolveMyShapes(myShapesLst, lstFIPSSTCO)
print(lstFIPSSTCO)
