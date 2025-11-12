'''****************************************************************
FieldValueCompare.py
Author(s): Anders Olson
Usage: Run script using python IDE or similar
Description:
        Script traverses ID field for 2 shapefiles and compares the
        list of IDs to see what is missing.
****************************************************************'''

import arcpy
from collections import Counter

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
# Define Functions
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

def createValueList(shpIn,fld):
    # List to return all values for given field
    fieldValues = []

    # Populate a list of all IDs found in the desired ID field
    for row in arcpy.da.SearchCursor(shpIn, [fld]):
        fieldValues.append(row[0])

    # # Print a list of all ids and no repeating ids i.e. 'keys'
    # print(Counter(uniqueValues).keys())
    #
    # # Print a count for occurrence of each id found in original list i.e. 'values'
    # print(Counter(uniqueValues).values())

    # Output a list of all values found in the field
    return(fieldValues)

def diffLST(inLST1,inLST2):
    return (list(set(inLST1) - set(inLST2)))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Define variables
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Input shapefiles or dbf with id field to compare
shp1 = r'C:\Users\is_olson\Documents\Projects\Central-Square\reports\CSProjectsReport_111025.shp'
shp2 = r'C:\Users\is_olson\Documents\Projects\Central-Square\reports\CSProjectsReport_111025_TEST.shp'

# Field name that the value search will use to find all values
fieldName = 'PIN'

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Call Functions
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Get list of all values in given field from each shapefile to compare
shp1Values = createValueList(shp1,fieldName)
shp2Values = createValueList(shp2,fieldName)

# Get list of values that do not match
diff = diffLST(shp1Values,shp2Values)
# diff = diffLST(shp2Values,shp1Values)

# print(shp1Values)
# print(shp2Values)
print(diff)
