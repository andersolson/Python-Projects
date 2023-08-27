from osgeo import osr, gdal

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Define Local Variables
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Stop GDAL printing both warnings and errors to STDERR
#gdal.PushErrorHandler('CPLQuietErrorHandler')

# assign working directory
workingDir = r'D:\Projects\WORKING\pheonix\imagery\gdal\compare\NAIP'

# Input NAIP NAD83 / UTM zone 10N OR UTM zone 11N GeoTiff
rasterIn  = f'{workingDir}\src\M_3311717_SW\m_3311717_sw_11_060_20200505.tif'
#rasterIn  = f'{workingDir}\M_3712213_SE\m_3712213_se_10_060_20200524.tif'
#rasterIn  = f'{workingDir}\M_3712213_SW\m_3712213_sw_10_060_20200524.tif'
#rasterIn  = f'{workingDir}\M_3712221_NE\m_3712221_ne_10_060_20200524.tif'
#rasterIn  = f'{workingDir}\M_3411815_SE\m_3411815_se_11_060_20200501.tif'

# Output WGS84 Geotiff
rasterOut1 = f'{workingDir}\output1_WGS84.tif'

# Output WGS84 Geotiff
rasterOut2 = f'{workingDir}\output2_WGS84.tif'

# Output WGS84 Geotiff
rasterOut3 = f'{workingDir}\output3_WGS84.tif'

# Output WGS84 Geotiff
rasterOut4 = f'{workingDir}\output4_WGS84.tif'

# Output WGS84 Geotiff
rasterOut5 = f'{workingDir}\output5_WGS84.tif'

# Output for virtual raster
VRT        = f'{workingDir}\outVRT.vrt'

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
#================================#
# Run code
#================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Define options for warp following Dave's command line for DEM as a guide:
# "C:\Program Files\QGIS 3.22.2\bin\gdalwarp.exe" -t_srs EPSG:4326 -ts 10800 10800  -te  -86  46  -85  47 -of GTiff -co "COMPRESS=LZW" -co "BLOCKXSIZE=256" -co "BLOCKYSIZE=256" -r bilinear  -overwrite "M:\Scripts\30mMESH\vrt\MESH_N47W086.vrt" "M:\Scripts\30mMESH\tile\ElevUS30mBATH_2023_01_N47W086.tif"

# open UTM image
input  = gdal.Open(rasterIn)

# get image width and height
width  = input.RasterXSize #columns
height = input.RasterYSize #rows

# get image geo transform info
gt     = input.GetGeoTransform()
'''
gt[2],gt[4] - row rotation, column rotation
gt[1],gt[5] - pixel size
gt[0],gt[3] - x-coord upper left, y-coord upper left
'''
# get the input pixel resolution
resolution = 0.000006

# calculate bounding box coords for NAD83 / UTM zone 10N
min_x = gt[0]
min_y = gt[3] + width * gt[4] + height * gt[5]
max_x = gt[0] + width * gt[1] + height * gt[2]
max_y = gt[3]

# get the existing wkt UTM coordinate system
utm_cs = osr.SpatialReference()
utm_cs.ImportFromWkt(input.GetProjectionRef())
srcSRS = utm_cs

# create the wkt WGS84 coordinate system
wgs_cs = osr.SpatialReference()
wgs_cs.ImportFromEPSG(4326)
dstSRS = wgs_cs

# create a transform object to convert between coordinate systems
transform = osr.CoordinateTransformation(utm_cs, wgs_cs)

# get the bounding box coordinates in WGS84 Lat/Long
upperLeft  = transform.TransformPoint(min_x, max_y)
lowerRight = transform.TransformPoint(max_x, min_y)
upperRight = transform.TransformPoint(max_x, max_y)
lowerLeft  = transform.TransformPoint(min_x, min_y)

# name bounding box variable for WGS84 Lat/Long
#bounds = [upperLeft[0], upperLeft[1], lowerRight[0], lowerRight[1]] #[ulx, uly, lrx, lry] from translate doc
#bounds = [lowerLeft[0], lowerLeft[1], upperRight[0], upperRight[1]] #(minX, minY, maxX, maxY) from warp doc
#bounds = [upperRight[0], upperRight[1], lowerLeft[0], lowerLeft[1]] #switch to (maxX, maxY, minX, minY)
#bounds = [lowerRight[0], lowerRight[1], upperLeft[0], upperLeft[1]] #switch to [lrx, lry, ulx, uly]
#bounds = [upperLeft[1],upperLeft[0],lowerRight[1],lowerRight[0]] #maxY, minX, minY, maxX
#bounds = [upperLeft[1],lowerRight[0],lowerRight[1],upperLeft[0]] #maxY, maxX, minY, minX
#print(bounds)



# print("Running Katie Projection")
# katieBounds = [upperLeft[1],upperLeft[0],lowerRight[1],lowerRight[0]]
# print(katieBounds)
#
# # define options for warp: use katie's research
# cOptions = ['COMPRESS=LZW','BLOCKXSIZE=256','BLOCKYSIZE=256']
# wOptions = gdal.WarpOptions(format='GTiff', width=width, height=height, outputBounds=katieBounds, dstSRS='EPSG:4326',
#                             resampleAlg='near', creationOptions=cOptions)
#
# # Project raster from UTM to WGS84 using gdal warp with options
# warp = gdal.Warp(rasterOut1, rasterIn, options=wOptions)
# warp = None  # Closes the file



# print("Running Default Projection")
# # define options for warp: most basic projectiong process
# cOptions = ['COMPRESS=LZW','BLOCKXSIZE=256','BLOCKYSIZE=256']
# wOptions = gdal.WarpOptions(format='GTiff', dstSRS='EPSG:4326', resampleAlg='near',creationOptions=cOptions)
#
# # Project raster from UTM to WGS84 using gdal warp with options
# warp = gdal.Warp(rasterOut2, rasterIn, options=wOptions)
# warp = None  # Closes the file



# print("Running Virtual Raster Projection")
# # Using gdal translate in a step before the warp
# transOptions = gdal.TranslateOptions(format='VRT', bandList=[1,2,3,4], noData=[0,0,0,0])
#
# # Translate input raster to a vrt with the bounds set
# gt = gdal.Translate(VRT, rasterIn, options=transOptions)
#
# # define options for warp
# cOptions = ['COMPRESS=LZW','BLOCKXSIZE=256','BLOCKYSIZE=256']
# wOptions = gdal.WarpOptions(format='GTiff', width=width, height=height, dstSRS='EPSG:4326',
#                             resampleAlg='near', creationOptions=cOptions)
#
# # Project raster from UTM to WGS84 using gdal warp with options
# warp = gdal.Warp(rasterOut3, VRT, options=wOptions)
# warp = None  # Closes the file



# print("Running Default Projection with Resolution")
# # define options for warp: most basic projectiong process
# cOptions = ['COMPRESS=LZW','BLOCKXSIZE=256','BLOCKYSIZE=256']
# wOptions = gdal.WarpOptions(format='GTiff', xRes=resolution, yRes=resolution, srcSRS=srcSRS, dstSRS=dstSRS,
#                             resampleAlg='near', creationOptions=cOptions)
#
# # Project raster from UTM to WGS84 using gdal warp with options
# warp = gdal.Warp(rasterOut4, rasterIn, options=wOptions)
# warp = None  # Closes the file



print("Running Default Projection with Resolution & Cubic Resample")
# define options for warp: most basic projectiong process
cOptions = ['COMPRESS=LZW','BLOCKXSIZE=256','BLOCKYSIZE=256']
wOptions = gdal.WarpOptions(format='GTiff', xRes=resolution, yRes=resolution, srcSRS=srcSRS, dstSRS=dstSRS,
                            resampleAlg='cubic', creationOptions=cOptions)

# Project raster from UTM to WGS84 using gdal warp with options
warp = gdal.Warp(rasterOut5, rasterIn, options=wOptions)
warp = None  # Closes the file

print("Projection Complete!")
