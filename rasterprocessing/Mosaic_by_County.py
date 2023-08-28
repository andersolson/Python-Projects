#---------------------------------------------------------------------------
# Mosaic_by_County.py
#
# Author: Anders Olson
# Usage:  Requires gdal and python 3, run as stand-alone script.
#
# Description: Mosaics vegetation binary images for each county using county
#             shapefile for California and index shapefile of NAIP tiles.
# ---------------------------------------------------------------------------

import os
from osgeo import gdal
from osgeo import ogr
from datetime import datetime as dt

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Define Local Variables
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Start a timer
startTime = dt.now()

# California counties shapefile
#caCountyShp = r'D:\Documents\WORKING\pheonix\vectors\County_2022_07\Data\Remainder.shp'
caCountyShp = r'D:\Documents\WORKING\pheonix\vectors\County_2022_07\Data\CA_errors_06093_06049.shp'

# NAIP tile index shapefile
naipIndexShp = r'D:\Documents\WORKING\pheonix\vectors\index\cl_NAIP_index.shp'

# Directory location for tiles
rasters = r'W:\NAIP_cl\CA\binary'

# Output location for final mosaic
outDir = r'W:\NAIP_cl\CA\mosaic_county'

# Create list of tiles by county stored in txt
logTxt = r'D:\Documents\WORKING\pheonix\MosaicLogDEV_{}.txt'.format(startTime.strftime("%d-%m-%Y"))

# Open log txt file for writing output messages
writeTo = open(logTxt, 'w')

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Define functions
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

def myFileLocations (fileEnding, rasterPath):
    raster_tiles = []

    # Get a list of all binary tile path filename locations
    for root, dirs, files in os.walk(rasterPath):
        for file in files:
            if file.endswith(fileEnding):
                raster_tiles.append(os.path.join(root, file))

    return(raster_tiles)

def findCntyGeom(inLayer):
    wktLst = []

    # Get field values
    fipsstco = inLayer.GetField('FIPSSTCO')

    # Get wkt geometry for the county
    geom = inLayer.GetGeometryRef()
    geomExport = geom.ExportToWkt()

    # wktLst.append('ca')
    wktLst.append(fipsstco)
    wktLst.append(geomExport)
    return(wktLst)

def spatialSelect(wktLst,inLayer,raster_tiles):
    index_tiles     = []
    files_to_mosaic = []

    # Make a spatial selection from tile shapefile for each county wkt polygon
    inLayer.SetSpatialFilter(ogr.CreateGeometryFromWkt(wktLst[1]))

    # Get a list of all county naip tile filenames from index shapefile e.g. m_3712021_se_10_060_20200619
    for feature in inLayer:
        tifName = feature.GetField('FileName')
        index_tiles.append(tifName[:-4]) #Remove tif file ending

    #print(len(index_tiles))

    # Create a list of raster image pathnames searching for tilename in string e.g. Vegetation_m_3712021_se_10_060_20200619_2022_10.tif
    for tile in index_tiles:
        matches = [match for match in raster_tiles if tile in match]
        #print(matches[0])
        files_to_mosaic.append(matches[0])

    #print(len(files_to_mosaic))

    return(files_to_mosaic)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Run code
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Notify user and write to log
print("Start time: {0}".format(startTime))
writeTo.write("Start time: {0}\n".format(startTime))

driver      = ogr.GetDriverByName('ESRI Shapefile')
# Set data source for county shapefile
dataSource  = driver.Open(caCountyShp, 0) # 0 means read-only. 1 means writeable.
# Set data source for naip tile index shapefile
dataSource2 = driver.Open(naipIndexShp, 0)

# Call function to get list of all binary tif filepath names in directory
binaryLST = myFileLocations('.tif', rasters)
print('Found {0} tif files for processing'.format(len(binaryLST)))

# Check to see if counties shapefile is found. Then count the number of features in the layer
if dataSource is None:
    print('Could not open {0}'.format(caCountyShp))
    writeTo.write('Could not open {0}\n'.format(caCountyShp))
    writeTo.close()
else:
    print('Opened {0}'.format(caCountyShp))
    writeTo.write('Opened {0}\n'.format(caCountyShp))

    layer = dataSource.GetLayer()
    featureCount = layer.GetFeatureCount()
    print("Number of features in {0}: {1}".format(os.path.basename(caCountyShp),featureCount))
    writeTo.write("Number of features in {0}: {1}\n".format(os.path.basename(caCountyShp),featureCount))

# Check to see if naip tiles shapefile is found. Then get the FIPSSTCO and GEOM for each feature
if dataSource is None:
    print('Could not open {0}'.format(naipIndexShp))
    writeTo.write('Could not open {0}\n'.format(naipIndexShp))
    writeTo.close()
else:
    print('Opened {0}'.format(naipIndexShp))
    writeTo.write('Opened {0}\n'.format(naipIndexShp))

    # Define layer for counties shapefile
    cntyLayer = dataSource.GetLayer()

    # Define layer for naip tile index shapefile
    tileLayer = dataSource2.GetLayer()

    # Loop through counties, select intersecting tiles, mosaic tiles
    for feature in cntyLayer:

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        # ================================#
        # Run Vector processing
        # ================================#
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

        pStart = dt.now()

        # Call function to get fipsstco and geom for each county in a list
        cntyGeom = findCntyGeom(feature)
        print('Selected county: {0}'.format(cntyGeom[0]))
        writeTo.write('Selected county: {0}\n'.format(cntyGeom[0]))

        # Call function to get correct tile image pathnames that match county geom and index attribute
        tiles = spatialSelect(cntyGeom,tileLayer,binaryLST)
        print('Found {0} intersecting tiles to mosaic'.format(len(tiles)))
        writeTo.write('Found {0} intersecting tiles to mosaic\n'.format(len(tiles)))

        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        # ================================#
        # Run Raster processing
        # ================================#
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

        print('Running mosaic for: {0}...'.format(cntyGeom[0]))
        writeTo.write('\nRunning mosaic for: {0}...\n'.format(cntyGeom[0]))

        outName = 'mosaic_{0}'.format(cntyGeom[0])

        # Create a virtual raster of all selected tiles for county
        gdal.BuildVRT('{0}\{1}.vrt'.format(outDir,outName), tiles)

        # Create output options for translate function: geotiff, Byte, compression, and 2-bit
        translateOptions = gdal.TranslateOptions(format='gtiff',
                                                 outputType=gdal.gdalconst.GDT_Byte,
                                                 creationOptions=['COMPRESS=LZW','NBITS=2'])
        # Convert virtual raster to a tif
        gdal.Translate('{0}\{1}.tif'.format(outDir,outName), '{0}\{1}.vrt'.format(outDir,outName), options=translateOptions)

        print("{0} complete! Runtime: {1}".format(cntyGeom[0],dt.now()-pStart))
        writeTo.write("{0} complete! Runtime: {1}\n".format(cntyGeom[0],dt.now()-pStart))

print("Complete! Total runtime: {0}".format(dt.now()-startTime))
writeTo.write("Complete! Total runtime: {0}".format(dt.now()-startTime))
writeTo.close()