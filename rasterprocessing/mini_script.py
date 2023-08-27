import os
from osgeo import osr, gdal
from datetime import datetime as dt

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Define Local Variables
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Start a timer
startTime = dt.now()

# Stop GDAL printing both warnings and errors to STDERR
#gdal.PushErrorHandler('CPLQuietErrorHandler')

# Directory location of source NAIP imagery from AWS
srcDir = r'W:\NAIP_Source\tiles'

# List of file names
tilelist = []

# Test NAIP image for gdal edit
testRaster = r'D:\Projects\WORKING\pheonix\imagery\gdal\m_3312007_se_10_060_20200607.tif'

# Output WGS84 Geotif
outWGS1  = r'D:\Projects\WORKING\pheonix\imagery\gdal\WGS1.tif'
outWGS2  = r'D:\Projects\WORKING\pheonix\imagery\gdal\WGS2.tif'
outWGS3  = r'D:\Projects\WORKING\pheonix\imagery\gdal\WGS3.tif'
outWGS4  = r'D:\Projects\WORKING\pheonix\imagery\gdal\WGS4.tif'
outWGS5  = r'D:\Projects\WORKING\pheonix\imagery\gdal\WGS5.tif'
outWGS6  = r'D:\Projects\WORKING\pheonix\imagery\gdal\WGS6.tif'
outWGS7  = r'D:\Projects\WORKING\pheonix\imagery\gdal\WGS7.tif'
outWGS8  = r'D:\Projects\WORKING\pheonix\imagery\gdal\WGS8.tif'
outWGS9  = r'D:\Projects\WORKING\pheonix\imagery\gdal\WGS9.tif'
outWGS10 = r'D:\Projects\WORKING\pheonix\imagery\gdal\WGS10.tif'
outWGS11 = r'D:\Projects\WORKING\pheonix\imagery\gdal\WGS11.tif'
outWGS12 = r'D:\Projects\WORKING\pheonix\imagery\gdal\WGS12.tif'

tVRT     = r'D:\Projects\WORKING\pheonix\imagery\gdal\tWGS.vrt'

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Define functions
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Define function to find pathnames and filenames
def myFileLocations (fileEnding, directory, inLST):
    #Loop the directory and subdirectories for all .shp file endings and store them in a list
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(fileEnding):
                inLST.append(os.path.join(root, file))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Run code
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

### TRYING TO FIX THE WARNING: ###
### Warning 1: TIFFReadDirectory:Sum of Photometric type-related color channels and ExtraSamples doesn't match SamplesPerPixel. Defining non-color channels as ExtraSamples.
### ERROR IS INHERENT IN THE SOURCE METADATA: https://trac.osgeo.org/gdal/ticket/5177 ###

# # Define NIR band with gdal_edit.py
# subprocess.call([sys.executable, r'C:\Users\andolson\AppData\Local\ESRI\conda\envs\GDALenv\Scripts\gdal_edit.py',
#                  '-colorinterp_1', 'red',
#                  '-colorinterp_2', 'green',
#                  '-colorinterp_3', 'blue',
#                  '-colorinterp_4', 'alpha', testRaster])
#
# ds        = gdal.Open(testRaster)
# info      = gdal.Info(ds)
# print(info)

### TRYING TO FIND DIFFERENCES IN METADATA COLS, ROWS, PROJECTION ###
### Run time is 0:21:29.264525 ###
# [10630, 10620, 10610, 10640, 10020, 9880, 9940, 9980, 10000, 10030, 9950, 9910, 9830, 9920, 9970, 9860, 9960, 9850, 10010, 9890, 9900, 9990, 10050, 10040, 9930, 9840, 9870, 10060, 9820, 10410, 10430, 10390, 10360, 10350, 10370, 10490, 10440, 10460, 10470, 10450, 10330, 10300, 10380, 10420, 10400, 10340, 10480, 10320, 10290, 10500, 10310, 10530, 10540, 10580, 10600, 10590, 10560, 10520, 10510, 10550, 10570, 10280, 10150, 10130, 10260, 10250, 10160, 10120, 10190, 10170, 10110, 10240, 10100, 10140, 10180, 10220, 10070, 10090, 10200, 10210, 10080, 10230, 10270, 10680, 10650, 10660, 10670, 9750, 9730, 9780, 9740, 9770, 9790, 9810, 9800, 9760, 9710, 9720, 9700, 9330, 9310, 9360, 9340, 9320, 9350, 9300, 9370, 9590, 9550, 9540, 9530, 9440, 9470, 9620, 9520, 9560, 9570, 9500, 9610, 9580, 9510, 9480, 9630, 9650, 9660, 9490, 9600, 9640, 9670, 9680, 9460, 9450, 9430, 9420, 9380, 9390, 9400, 9410, 9690, 10690, 10700, 10710]
# [12490, 12500, 12510, 12400, 12360, 12380, 12420, 12390, 12410, 12370, 12340, 12330, 12350, 12320, 12240, 12250, 12230, 12270, 12280, 12300, 12260, 12290, 12220, 12310, 12480, 12460, 12470, 12450, 12440, 12430, 12520, 12530, 12540]
# 142 - Unique Column Counts
# 33  - Unique Row Counts

# # Find all filenames for tif source imagery and save to list
# # e.g. 'W:\\NAIP_Source\\tiles\\41120\m_4112064_nw_10_060_20200711.tif'
# myFileLocations('.tif', srcDir, tilelist)
# print('Found {0} image tiles'.format(len(tilelist)))
#
# cols = []
# rows = []
#
# for tilePath in tilelist:
#     # Get filename of the tile
#     fName = tilePath.split('\\')
#     name  = (fName[-1].split('.', 1)[0])
#     #print(name)
#
#     # Pull metadata
#     ds = gdal.Open(tilePath)
#     metadata = ds.GetMetadata()
#     bandCnt = ds.RasterCount
#     rasterX = ds.RasterXSize
#     rasterY = ds.RasterYSize
#     #print(metadata)
#     #print(bandCnt)
#     #print(rasterX)
#     #print(rasterY)
#
#     cols.append(rasterX) if rasterX not in cols else cols
#     rows.append(rasterY) if rasterY not in rows else rows
#
# print(cols)
# print(rows)
# print(len(cols))
# print(len(rows))

### LOOKING FOR RASTER METADATA TO PASS INTO GDAL WARP ###

input        = gdal.Open(testRaster)
projection   = input.GetProjection() # same as GetProjectionRef()
proj_ref     = input.GetProjectionRef() # same as GetProjection()
geotransform = input.GetGeoTransform()
info         = gdal.Info(input)
bandCnt      = input.RasterCount
rasterX      = input.RasterXSize
rasterY      = input.RasterYSize
ul_x, res_x, xrot, ul_y, roty, res_y = input.GetGeoTransform()
lr_x = ul_x + res_x * rasterX
lr_y = ul_y + res_y * rasterY

# print(projection)
# print(proj_ref)
# print(geotransform)
# print(info)
# print(bandCnt)
print(rasterX)
print(rasterY)
# print(f'X-upper left: {ul_x}\nY-upper left: {ul_y}\nX-resolution: {res_x}\nY-resolution: {res_y}')
# utm_bounds = f'{ul_x} {lr_y} {lr_x} {ul_y}'
# print(utm_bounds)

# get the existing wkt UTM coordinate system
utm_cs = osr.SpatialReference()
utm_cs.ImportFromWkt(input.GetProjectionRef())

# create the wkt WGS84 coordinate system
wgs84_wkt = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]]'
wgs_cs = osr.SpatialReference()
wgs_cs.ImportFromWkt(wgs84_wkt)

# create a transform object to convert between coordinate systems
transform = osr.CoordinateTransformation(utm_cs, wgs_cs)

# get the point to transform, pixel (0,0) in this case
width = input.RasterXSize
height = input.RasterYSize
gt = input.GetGeoTransform()
#print(gt)

## gt[2],gt[4] - row rotation, column rotation
## gt[1],gt[5] - pixel size
## gt[0],gt[3] - x-coord upper left, y-coord upper left

# get the pixel size of the input image
pixelSizeX = gt[1]
pixelSizeY = -gt[5]
print(f'{pixelSizeX} {pixelSizeY}')

# calculate the projected image bounding box coords
min_x = gt[0]
min_y = gt[3] + width * gt[4] + height * gt[5]
max_x = gt[0] + width * gt[1] + height * gt[2]
max_y = gt[3]

# print(f'UTM Upper Left: {min_x} {max_y}') #UL
# print(f'UTM Lower Right: {max_x} {min_y}') #LR
# print(f'UTM Upper Right: {max_x} {max_y}') #UR
# print(f'UTM Lower Left: {min_x} {min_y}')  #LL

# get the bounding box coordinates in lat/long
upperLeft  = transform.TransformPoint(min_x, max_y)  #UL
lowerRight = transform.TransformPoint(max_x, min_y)  #LR
upperRight = transform.TransformPoint(max_x, max_y)  #UR
lowerLeft  = transform.TransformPoint(min_x, min_y)  #LL

print(f'WGS84 Upper Left: {upperLeft}')
print(f'WGS84 Lower Right: {lowerRight}')
print(f'WGS84 Upper Right: {upperRight}')
print(f'WGS84 Lower Left: {lowerLeft}')

# name bounding box variable with long/lat:x/y
bounds = [upperLeft[0], upperLeft[1], lowerRight[0], lowerRight[1]] #[ulx, uly, lrx, lry] from translate doc
#bounds = [lowerLeft[0], lowerLeft[1], upperRight[0], upperRight[1]] #(minX, minY, maxX, maxY) from warp doc
#bounds = [upperRight[0], upperRight[1], lowerLeft[0], lowerLeft[1]] #switch to (maxX, maxY, minX, minY)
#bounds = [lowerRight[0], lowerRight[1], upperLeft[0], upperLeft[1]] #switch to [lrx, lry, ulx, uly]
print(bounds)

# Create output options for Warp, DO NOT set a no data value here in the options
# Test WGS1, columns and rows only:
#wgsOptions = gdal.WarpOptions(format='GTiff', width=width, height=height, dstSRS='EPSG:4326', resampleAlg='near')
##Creates output, but pixels off ~4.3ft compared to arc result

# Test WGS2, bounding box for (minX, minY, maxX, maxY) from warp documentation:
#wgsOptions = gdal.WarpOptions(format='GTiff', outputBounds=bounds, dstSRS='EPSG:4326', resampleAlg='near')
##ERROR 1: Too many points (529 out of 529) failed to transform, unable to compute output bounds.
##Warning 1: Unable to compute source region for output window 0,0,11260,12154, skipping.
#Blank image with no data created

# Test WGS3, bounding box for [ulx, uly, lrx, lry] from translate documentation:
#wgsOptions = gdal.WarpOptions(format='GTiff', outputBounds=bounds, dstSRS='EPSG:4326', resampleAlg='near')
##ERROR 1: Attempt to create -11803x11387 dataset is illegal,sizes must be larger than zero.

# Test WGS4, bounding box for [ulx, uly, lrx, lry] from translate documentation and col/row:
#wgsOptions = gdal.WarpOptions(format='GTiff', width=width, height=height, outputBounds=bounds, dstSRS='EPSG:4326', resampleAlg='near')
##ERROR 1: Too many points (529 out of 529) failed to transform, unable to compute output bounds.
##Warning 1: Unable to compute source region for output window 0,0,10630,12490, skipping.
#Blank image with no data created

# Test WGS5, bounding box for (minX, minY, maxX, maxY) from warp documentation and col/row:
#wgsOptions = gdal.WarpOptions(format='GTiff', width=width, height=height, outputBounds=bounds, dstSRS='EPSG:4326', resampleAlg='near')
##ERROR 1: Too many points (529 out of 529) failed to transform, unable to compute output bounds.
##Warning 1: Unable to compute source region for output window 0,0,10630,12490, skipping.
#Blank image with no data created

# Test WGS6, switched order of bounding box for [lrx, lry, ulx, uly] from translate documentation:
#wgsOptions = gdal.WarpOptions(format='GTiff', width=width, height=height, outputBounds=bounds, dstSRS='EPSG:4326', resampleAlg='near')
##ERROR 1: Too many points (529 out of 529) failed to transform, unable to compute output bounds.
##Warning 1: Unable to compute source region for output window 0,0,10630,12490, skipping.
#Blank image with no data created

# Project raster from UTM to WGS84 using gdal warp
#warp = gdal.Warp(outWGS6, testRaster, options=wgsOptions)
#warp = None  # Closes the file

# Using gdal translate in a step before the warp
transOptions = gdal.TranslateOptions(format='VRT', outputBounds=bounds, outputSRS='EPSG:4326')

# Translate input raster to a vrt with the bounds set
gt = gdal.Translate(tVRT, testRaster, options=transOptions)

# Test WGS7, use warp with default options to see result
# warp = gdal.Warp(outWGS7, tVRT, dstSRS='EPSG:4326')
# warp = None  # Closes the file
##ERROR 1: Cannot find transformation for provided coordinates

# Test WGS8, using width and height in warp options
# wgsOptions = gdal.WarpOptions(format='GTiff', width=width, height=height, dstSRS='EPSG:4326', resampleAlg='near')

# Project raster from UTM to WGS84 using gdal warp
# warp = gdal.Warp(outWGS8, tVRT, options=wgsOptions)
# warp = None  # Closes the file
##ERROR 1: Cannot find transformation for provided coordinates

# Test WGS9, using rex and resy in warp options
# wgsOptions = gdal.WarpOptions(format='GTiff', xRes='0.6', yRes='0.6', dstSRS='EPSG:4326', resampleAlg='near')

# Project raster from UTM to WGS84 using gdal warp
# warp = gdal.Warp(outWGS9, testRaster, options=wgsOptions)
# warp = None  # Closes the file
##ERROR 1: Attempt to create 0x0 dataset is illegal,sizes must be larger than zero.

# Test WGS10, using creation options for compression
# creationO = ['COMPRESS=LZW', 'BLOCKXSIZE=256', 'BLOCKYSIZE=256']
# wgsOptions = gdal.WarpOptions(format='GTiff', dstSRS='EPSG:4326', resampleAlg='near', creationOptions=creationO)

# Project raster from UTM to WGS84 using gdal warp
# warp = gdal.Warp(outWGS10, testRaster, options=wgsOptions)
# warp = None  # Closes the file
##Output image is slightly different at the edges than the arc and previous runs, image size is smaller with LZW compression

# Test WGS12, using creation options for compression
#wkt = 'WGS_1984_(ITRF00)_To_NAD_1983'
#creationO = ['COMPRESS=LZW', 'BLOCKXSIZE=256', 'BLOCKYSIZE=256']
#wgsOptions = gdal.WarpOptions(format='GTiff', dstSRS='EPSG:4326', width=width, height=height, resampleAlg='near', coordinateOperation=wkt, creationOptions=creationO)
##Output is a weird warped image

# Project raster from UTM to WGS84 using gdal warp
#warp = gdal.Warp(outWGS11, tVRT, options=wgsOptions)
#warp = None  # Closes the file

# Test WGS12, using creation options for compression
wkt = 'WGS_1984_(ITRF00)_To_NAD_1983'
creationO = ['COMPRESS=LZW', 'BLOCKXSIZE=256', 'BLOCKYSIZE=256']
wgsOptions = gdal.WarpOptions(format='GTiff', dstSRS='EPSG:4326', resampleAlg='near', coordinateOperation=wkt, creationOptions=creationO)

# Project raster from UTM to WGS84 using gdal warp
warp = gdal.Warp(outWGS12, tVRT, options=wgsOptions)
warp = None  # Closes the file

print("Complete! Total runtime: {0}".format(dt.now()-startTime))