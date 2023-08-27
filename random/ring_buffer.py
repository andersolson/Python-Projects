import arcpy
from datetime import datetime as dt

# Turn on overwrite output
arcpy.env.overwriteOutput = True

# Start a timer
startTime = dt.now()

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Define functions
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

'''
Inputs:
shp    -- Structures shapefile input

Outputs:
lst   -- Returns a nested list copy of the shapefile attribute table
'''
def getAttributes(shp):
    lst = []
    for row in arcpy.da.SearchCursor(shp, ['FID','PolyID','ImgDate','ImgSource','PolyDate','StateCode','CNTYCode' ]):
        # Temporary list for each row of the attribute table
        tmpLst = []
        tmpLst.append(row[0])
        tmpLst.append(row[1])
        tmpLst.append(row[2])
        tmpLst.append(row[3])
        tmpLst.append(row[4])
        tmpLst.append(row[5])
        tmpLst.append(row[6])
        # Append rows to list as nested items
        lst.append(tmpLst)
    return(lst)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Run Script
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

structures = r'D:\Documents\WORKING\pheonix\vectors\multibuffer\ca015_03302021.shp'
#structures = r'D:\Documents\WORKING\pheonix\vectors\multibuffer\c06015_sample.shp'
structRngs = r'D:\Documents\WORKING\pheonix\vectors\multibuffer\c06015_temp_buffer.shp'
#sampleFC   = r'D:\Documents\WORKING\pheonix\vectors\multibuffer\GDB.gdb\ca015_sample_buffers'
finalFC    = r'D:\Documents\WORKING\pheonix\vectors\multibuffer\GDB.gdb\ca015_buffers'

# Loop through nested list copy of structures shapefile
for row in getAttributes(structures):

    # Note: PolyID is stored as a Double in the shapefile
    polyID = row[1]

    # Build a layer query
    query = "PolyID = {0}".format(polyID)

    # Make a feature layer of the selection
    arcpy.management.MakeFeatureLayer(structures, "temp", query)

    # Run multi-ring buffer the structure of the temp selection layer to a temporary shapefile
    arcpy.analysis.MultipleRingBuffer("temp", structRngs, [5,30,100],
                                      "Feet", "distance", "ALL", "OUTSIDE_ONLY", "GEODESIC")

    # Fields that need to be added
    fields = [['orig_fid','LONG','orig_fid'],
              ['polyid','DOUBLE','polyid',19],
              ['imgdate','TEXT','imgdate',255],
              ['imgsource','TEXT','imgsource',32],
              ['polydate','TEXT','polydate',32],
              ['statecode','TEXT','statecode',32],
              ['cntycode','TEXT','cntycode',32]]

    # Add multiple fields from original structures
    arcpy.management.AddFields(structRngs, fields)

    # Calculate the fields using the nested list copy
    fCalc = [['orig_fid','{0}'.format(row[0])],
              ['polyid','{0}'.format(row[1])],
              ['imgdate',"'{0}'".format(row[2])],
              ['imgsource',"'{0}'".format(row[3])],
              ['polydate',"'{0}'".format(row[4])],
              ['statecode',"'{0}'".format(row[5])],
              ['cntycode',"'{0}'".format(row[6])]]

    # Calculate fields from original structures
    arcpy.CalculateFields_management(structRngs,"PYTHON3", fCalc)

    # Append structure buffers to a target FC
    arcpy.management.Append(structRngs,finalFC, 'NO_TEST')

print("Total run time: {0}".format(dt.now()-startTime))

