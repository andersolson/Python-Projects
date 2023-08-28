#-----------------------------------------------------------------------------
# NDVI_arcpy.py
#
# Author: Anders Olson
#
# Usage: Runs as a standalone script, written with Python 3.7
#
# Description: Calculate and export NDVI image from CIR-CCM (Color Infra-Red Compressed County Mosaics)
#              imagery using arcpy.
#
#-------------------------------------------------------------------------------

import os, glob
import sys
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
arcpy.env.qualifiedFieldNames = False
arcpy.env.pyramid = None
arcpy.env.rasterStatistics = None

# Start a timer
startTime = dt.now()

# Directory location for WGS projected CIR imagery
os.chdir(r'B:\projects\WildfirePhoenix\PlacerCounty\tiles_wgs')

# List of file names
tilelist = []

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

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Run Script
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

outputMessage("Running: {0}".format(sys.argv[0]))

for file in glob.glob("*.tif"):
    tilelist.append(file)

outputMessage("Started Processing at: {0}".format(dt.now()))

for imagename in tilelist:

    print("\tNDVI started for {0}".format(imagename))

    # Start a timer
    runTime = dt.now()

    #outputMessage(imagename)

    # Output NDVI image name
    save = r'B:\projects\WildfirePhoenix\PlacerCounty\ndvi_wgs\ndvi_{0}'.format(imagename)

    nir = Float(Raster(imagename + r"\Band_4"))
    red = Float(Raster(imagename + r"\Band_1"))
    ndvi = (nir - red) / (nir + red)
    ndvi.save(save)

    print("\tNDVI took {0} to complete {1}".format(dt.now()-runTime, save))

currentTime = dt.today()
totalTime = currentTime - startTime
outputMessage("Total Runtime: {0}".format(str(totalTime)))