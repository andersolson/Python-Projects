#-----------------------------------------------------------------------------
# Binary_Only.py
#
# Author: Anders Olson
#
# Usage: Runs as a standalone script, written with Python 3.7
#
# Description: Calculate and export Binary image from .SID file CIR-CCM (Color
#              Infra-Red Compressed County Mosaics) imagery using arcpy.
#
#-------------------------------------------------------------------------------

import os
import arcpy
from arcpy.sa import *
from datetime import datetime as dt

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Define local variables and environments
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Check out Spatial Analyst extension from arc
arcpy.CheckOutExtension("Spatial")

arcpy.env.overwriteOutput = True
arcpy.env.pyramid = None
arcpy.env.rasterStatistics = None

# Start a timer
startTime = dt.now()

# Create a txt log
logTxt = r'D:\Documents\WORKING\pheonix\log_Binary_{}.txt'.format(startTime.strftime("%d-%m-%Y"))

# Open log txt file for writing output messages
writeTo = open(logTxt,'w')

# Directory location for source NAIP imagery
srcDir = r'W:\NAIP_Source\tiles'

# List of file names
tilelist = []

#tilelist = ['W:\\NAIP_Source\\tiles\\42123\\m_4212362_se_10_060_20200710.tif',
# 'W:\\NAIP_Source\\tiles\\42123\\m_4212363_sw_10_060_20200708.tif',
# 'W:\\NAIP_Source\\tiles\\42123\\m_4212363_se_10_060_20200708.tif',
# 'W:\\NAIP_Source\\tiles\\42123\\m_4212364_sw_10_060_20200710.tif',
# 'W:\\NAIP_Source\\tiles\\42123\\m_4212364_se_10_060_20200710.tif',
# 'W:\\NAIP_Source\\tiles\\42122\\m_4212257_sw_10_060_20200709.tif',
# 'W:\\NAIP_Source\\tiles\\42122\\m_4212257_se_10_060_20200709.tif',
# 'W:\\NAIP_Source\\tiles\\42122\\m_4212258_sw_10_060_20200709.tif',
# 'W:\\NAIP_Source\\tiles\\42122\\m_4212258_se_10_060_20200709.tif',
# 'W:\\NAIP_Source\\tiles\\42122\\m_4212259_se_10_060_20200709.tif',
# 'W:\\NAIP_Source\\tiles\\42122\\m_4212260_sw_10_060_20200709.tif',
# 'W:\\NAIP_Source\\tiles\\42122\\m_4212260_se_10_060_20200708.tif',
# 'W:\\NAIP_Source\\tiles\\42122\\m_4212261_sw_10_060_20200708.tif',
# 'W:\\NAIP_Source\\tiles\\42122\\m_4212261_se_10_060_20200708.tif',
# 'W:\\NAIP_Source\\tiles\\42122\\m_4212262_sw_10_060_20200708.tif',
# 'W:\\NAIP_Source\\tiles\\42122\\m_4212262_se_10_060_20200708.tif',
# 'W:\\NAIP_Source\\tiles\\41121\\m_4112105_ne_10_060_20200711.tif',
# 'W:\\NAIP_Source\\tiles\\41121\\m_4112106_nw_10_060_20200711.tif',
# 'W:\\NAIP_Source\\tiles\\41121\\m_4112106_ne_10_060_20200711.tif',
# 'W:\\NAIP_Source\\tiles\\41121\\m_4112107_nw_10_060_20200711.tif',
# 'W:\\NAIP_Source\\tiles\\41121\\m_4112107_ne_10_060_20200711.tif',
# 'W:\\NAIP_Source\\tiles\\41121\\m_4112108_nw_10_060_20200711.tif',
# 'W:\\NAIP_Source\\tiles\\41121\\m_4112108_ne_10_060_20200711.tif',
# 'W:\\NAIP_Source\\tiles\\41120\\m_4112001_nw_10_060_20200711.tif',
# 'W:\\NAIP_Source\\tiles\\41120\\m_4112001_ne_10_060_20200711.tif',
# 'W:\\NAIP_Source\\tiles\\41120\\m_4112002_nw_10_060_20200711.tif',
# 'W:\\NAIP_Source\\tiles\\41120\\m_4112002_ne_10_060_20200711.tif',
# 'W:\\NAIP_Source\\tiles\\41120\\m_4112003_nw_10_060_20200711.tif']

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Define functions
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Define functions for error handling and messaging
def outputMessage(msg):
    print(msg)
    arcpy.AddMessage(msg)

def outputError(msg):
    print(msg)
    arcpy.AddError(msg)

# Define function to find pathnames and filenames
def myFileLocations (fileEnding, directory, inLST):
    #Loop the directory and subdirectories for all .shp file endings and store them in a list
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(fileEnding):
                inLST.append(os.path.join(root, file))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Run Script
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

outputMessage("Running: {0}".format(sys.argv[0]))
writeTo.write("Running: {0}\n".format(sys.argv[0]))

# Find all filenames for tif source imagery and save to list e.g. 'W:\\NAIP_Source\\tiles\\41120\\m_4112064_nw_10_060_20200711.tif'
myFileLocations('.tif', srcDir, tilelist)

outputMessage("Started Processing at: {0}".format(dt.now()))
writeTo.write("Started Processing at: {0}\n".format(dt.now()))

for fileName in tilelist:
    # Start a timer for processing tracking
    currentTime = dt.now()

    imageName = fileName.split('\\')[len(fileName.split('\\')) - 1][:-4]

    # Tag Month and Year
    tag = currentTime.strftime("%Y_%m")

    # Name output data
    wgsRas    = r'W:\NAIP_cl\CA\wgs_tile\wgs_{0}.tif'.format(imageName)
    binaryRas = r'W:\NAIP_cl\CA\temp\oneBit_{0}.tif'.format(imageName)
    twoBit    = r'W:\NAIP_cl\CA\binary\Vegetation_{0}_{1}.tif'.format(imageName,tag)

    # outputMessage(imageName)
    # outputMessage(binaryRas)
    # outputMessage(twoBit)
    # outputMessage(wgsRas)

    outputMessage("\tProjecting from UTM to WGS84:\n\t{0}".format(imageName))
    writeTo.write("\tProjecting from UTM to WGS84:\n\t{0}\n".format(imageName))

    # Spatial reference WGS84
    sr = arcpy.SpatialReference(4326)
    arcpy.management.ProjectRaster(fileName, wgsRas, sr)

    outputMessage("\tCalculating binary {0} image".format(imageName))
    writeTo.write("\tCalculating binary {0} image\n".format(imageName))

    # Caluclate NDVI thresholds and save the binary output
    nir = Float(Raster(wgsRas + r"\Band_4"))
    red = Float(Raster(wgsRas + r"\Band_1"))
    ndvi = (nir - red) / (nir + red)
    output = arcpy.sa.Con(ndvi>=.2,1,0)

    outputMessage("\tCalculation complete {0} image".format(dt.now()-currentTime))
    writeTo.write("\tCalculation complete {0} image\n".format(dt.now()-currentTime))

    outputMessage("\tConverting to 2-Bit:\n\t{0} image".format(imageName))
    writeTo.write("\tConverting to 2-Bit:\n\t{0} image\n".format(imageName))

    # Save raster as binary 2-bit
    arcpy.management.CopyRaster(output, twoBit,
                                '', None, "3", "NONE", "NONE", "2_BIT", "NONE", "NONE", "TIFF")

    outputMessage("\tProcess finished for: {0}".format(imageName))
    writeTo.write("\tProcess finished for: {0}\n".format(imageName))

    outputMessage("\tCurrent Runtime: {0}".format(dt.now()-startTime))
    writeTo.write("\tCurrent Runtime: {0}\n".format(dt.now()-startTime))

outputMessage("Complete! Total runtime: {0}".format(dt.now()-startTime))
writeTo.write("Complete! Total runtime: {0}".format(dt.now()-startTime))
writeTo.close()