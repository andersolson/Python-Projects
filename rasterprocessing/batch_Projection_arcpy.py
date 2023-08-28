# #-----------------------------------------------------------------------------
# # batch_Projection_arcpy.py
# #
# # Author: Anders Olson
# #
# # Usage: Runs as a standalone script, written with Python 3.7
# #
# # Description: Batch project NAIP imagery from UTM to WGS84
# #
# #-------------------------------------------------------------------------------

import os
import multiprocessing
import arcpy
from datetime import datetime as dt

def outputMessage(msg):
    print(msg)
    arcpy.AddMessage(msg)

def outputError(msg):
    print(msg)
    arcpy.AddError(msg)

def myFileLocations(fileEnding, directory, inLST):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(fileEnding):
                inLST.append(os.path.join(root, file))

def reproject(tileInput):
    currentTime = dt.now()
    imageName = tileInput.split('\\')[-1][:-4]
    #wgsRas = r'D:\Anders\phoenix\imagery\NAIP_Source\wgs_tiles\wgs_{0}.tif'.format(imageName)
    wgsRas = r'W:\naip\2022\ca\cl_standard\wgs_tile\wgs_{0}.tif'.format(imageName)

    # Check if image file already exists
    if not os.path.isfile(wgsRas):
        outputMessage("\tProjecting from UTM to WGS84:\n\t{0}".format(imageName))
        sr = arcpy.SpatialReference(4326)
        arcpy.management.ProjectRaster(tileInput, wgsRas, sr, 'NEAREST', '', 'WGS_1984_(ITRF00)_To_NAD_1983')
        arcpy.management.SetRasterProperties(wgsRas, nodata='1 0;2 0;3 0;4 0')
        outputMessage("\tProjection complete {0}".format(dt.now() - currentTime))
    else:
        outputMessage("\tWGS Raster already exists:\n\t{0}".format(imageName))


if __name__ == "__main__":
    arcpy.env.overwriteOutput = True
    arcpy.env.pyramid = None
    arcpy.env.rasterStatistics = None

    startTime = dt.now()
    #srcDir = r'D:\Anders\phoenix\imagery\NAIP_Source\tiles'
    #srcDir = r'W:\naip\2022\ca\source\tiles\Group1'
    #srcDir = r'W:\naip\2022\ca\source\tiles\Group2'
    #srcDir = r'W:\naip\2022\ca\source\tiles\Group3'
    srcDir = r'W:\naip\2022\ca\source\tiles\Group4'
    tilelist = []

    outputMessage("Running: {0}".format(os.path.basename(__file__)))

    myFileLocations('.tif', srcDir, tilelist)

    outputMessage("Started Processing at: {0}".format(dt.now()))

    with multiprocessing.Pool(26) as pool:
        pool.map(reproject, tilelist)

    outputMessage("Complete! Total runtime: {0}".format(dt.now()-startTime))