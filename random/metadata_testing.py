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
#rasterIn  = f'{workingDir}\M_3712213_SE\m_3712213_se_10_060_20200524.tif'
#rasterIn  = f'{workingDir}\M_3712213_SW\m_3712213_sw_10_060_20200524.tif'
#rasterIn  = f'{workingDir}\M_3712221_NE\m_3712221_ne_10_060_20200524.tif'
rasterIn  = f'{workingDir}\M_3411815_SE\m_3411815_se_11_060_20200501.tif'

# Output WGS84 Geotiff
rasterOut = f'{workingDir}\output_WGS84_kt2.tif'

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
print(width)
height = input.RasterYSize #rows
print(height)

# get image geo transform info
gt     = input.GetGeoTransform()
'''
gt[2],gt[4] - row rotation, column rotation
gt[1],gt[5] - pixel size
gt[0],gt[3] - x-coord upper left, y-coord upper left
'''

# calculate bounding box coords for NAD83 / UTM zone 10N
min_x = gt[0]
min_y = gt[3] + width * gt[4] + height * gt[5]
max_x = gt[0] + width * gt[1] + height * gt[2]
max_y = gt[3]

# get the existing wkt UTM coordinate system
utm_cs = osr.SpatialReference()
print(utm_cs)
utm_cs.ImportFromWkt(input.GetProjectionRef())

# create the wkt WGS84 coordinate system
wgs84_wkt = 'GEOGCS["WGS 84",DATUM["WGS_1984",' \
            'SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],' \
            'PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],' \
            'UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],' \
            'AUTHORITY["EPSG","4326"]]'
wgs_cs = osr.SpatialReference()
wgs_cs.ImportFromWkt(wgs84_wkt)

# create a transform object to convert between coordinate systems
transform = osr.CoordinateTransformation(utm_cs, wgs_cs)

# get the bounding box coordinates in WGS84 Lat/Long
upperLeft  = transform.TransformPoint(min_x, max_y)
print(upperLeft)
lowerRight = transform.TransformPoint(max_x, min_y)
print(lowerRight)
upperRight = transform.TransformPoint(max_x, max_y)
print(upperRight)
lowerLeft  = transform.TransformPoint(min_x, min_y)
print(lowerLeft)

# name bounding box variable for WGS84 Lat/Long
bounds = [upperLeft[1], upperLeft[0], lowerRight[1], lowerRight[0]] #[ulx, uly, lrx, lry]
print(bounds)

# define options for warp
cOptions = ['COMPRESS=LZW']
wOptions = gdal.WarpOptions(format='GTiff', width=width, height=height, outputBounds=bounds, dstSRS='EPSG:4326', resampleAlg='near', creationOptions=cOptions)

# Project raster from UTM to WGS84 using gdal warp with options
warp = gdal.Warp(rasterOut, rasterIn, options=wOptions)
warp = None  # Closes the file

print("Projection Complete!")
