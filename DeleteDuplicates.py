'''****************************************************************
DeleteDuplicate.py
Author(s): Anders Olson
Usage: Run script using python IDE or similar
Description:
        Script traverses a selected attribute field of input dataset
        to find duplicates. Only one record per a duplicate can exist;
        script deletes one of the duplicates.
****************************************************************'''

import arcpy

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

# Input dataset to find and remove duplicates
inData = r'C:\Users\andolson\Documents\WORKING\TEMP\SampleData.shp'

# List for tracking duplicate IDs
idList = []

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Call Functions
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

#Populate a list of attributes from desired input field and delete any duplicates, but only one duplicate.
with arcpy.da.UpdateCursor(inData, ['FIPSSTCO']) as cursor:
    for row in cursor:
        if row[0] in idList:
            cursor.deleteRow()
        elif row[0] not in idList:
            idList.append(row[0])
        else:
            outputMessage("Error building list...")

outputMessage(len(idList))
