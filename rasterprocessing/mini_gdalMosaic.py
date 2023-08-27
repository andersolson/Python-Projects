import os, sys
import subprocess
from osgeo import gdal
from datetime import datetime as dt

# Start a timer
startTime = dt.now()

mainDir = r'D:\Projects\WORKING\pheonix\imagery\gdal\compare'

# tiles = [r'D:\Projects\WORKING\pheonix\imagery\gdal\compare\NAIP\M_3712221_NE\output1_WGS84.tif',
#          r'D:\Projects\WORKING\pheonix\imagery\gdal\compare\NAIP\M_3712213_SW\output1_WGS84.tif',
#          r'D:\Projects\WORKING\pheonix\imagery\gdal\compare\NAIP\M_3712213_SE\output1_WGS84.tif']

tiles = [r'D:\Projects\WORKING\pheonix\imagery\binary\wgs_m_4112101_ne_10_060_20200711_Binary.tif',
         r'D:\Projects\WORKING\pheonix\imagery\binary\wgs_m_4112101_nw_10_060_20200712_Binary.tif']

outName = 'mosaicTest2'

# mergeName = f'{mainDir}\{outName}'
#
# tilesStr = ' '.join(tiles)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Run Raster processing
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

print(f'Running mosaic for: {outName}...')

# Create a virtual raster of all selected tiles for county
gdal.BuildVRT('{0}\{1}.vrt'.format(mainDir,outName), tiles)

# Create output options for translate function: geotiff, compression,
translateOptions = gdal.TranslateOptions(format='gtiff',
                                         creationOptions=['COMPRESS=LZW'])
# Convert virtual raster to a tif
gdal.Translate('{0}\{1}.tif'.format(mainDir,outName), '{0}\{1}.vrt'.format(mainDir,outName), options=translateOptions)

# print(f'Running gdal_merge.py for: {outName}...')
#
# # Project tile from UTM to WGS84 using gdalwarp.exe
# subprocess.call([r'C:\Users\andolson\AppData\Local\ESRI\conda\envs\ArcGDAL\Scripts\gdal_merge.py', '-o', mergeName,
#                  '-of', 'GTiff', tilesStr])

print("Complete! Total runtime: {0}".format(dt.now()-startTime))
