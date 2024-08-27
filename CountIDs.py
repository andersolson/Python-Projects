'''****************************************************************
CountIDs.py
Author(s): Anders Olson
Usage: Run script using python IDE or similar
Description:
        Script traverses ID field and counts occurrence of each ID
****************************************************************'''

import arcpy
from collections import counter

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Configure logger
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

def outputMessage(msg):
    print(msg)
    arcpy.AddMessage(msg)

def outputError(msg):
    print(msg)
    arcpy.AddError(msg)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Define environment and messaging
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Set the overwriteOutput ON
arcpy.gp.overwriteOutput = True

# Set workspace to be in memory for faster run time
arcpy.env.workspace = "in_memory"

outputMessage("Workspace is: {}".format(arcpy.env.workspace))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Define variables
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

#Input shapefile or dbf with id field to count
inData = r"U:\Somedirectory\yourshapefile.shp"

# Empty list for storing all unique IDs
uniqueIDs = []

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Call Functions
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Populate a list of all IDs found in the desired ID field
for row in arcpy.da.SearchCursor(inData, ['<FIELD-NAME>']):
        uniqueIDs.append(row[0])

# Print a list of all ids and no repeating ids i.e. 'keys'
print(Counter(uniqueIDs).keys())

# Print a count for occurrence of each id found in original list i.e. 'values'
print(Counter(uniqueIDs).values())
