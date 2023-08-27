from osgeo import gdal, gdal_array
import numpy as np

imagename = r'D:\Documents\WORKING\pheonix\imagery\wgs_tiles\wgs_m_4212364_sw_10_060_20200710.tif'
save = r'D:\Documents\WORKING\pheonix\imagery\ndvi\ndvi_4212364_sw_10_060.tif'

ds = gdal.Open(imagename)
b1 = ds.GetRasterBand(1)
b4 = ds.GetRasterBand(4)
red_arr = b1.ReadAsArray()
nir_arr = b4.ReadAsArray()

ndvi = (nir_arr - red_arr)/(nir_arr + red_arr)

gdal_array.SaveArray(ndvi, save, "GTIFF", ds)

ds = None




# # Directory to gdal merge python script
# dirGDAL = r'C:\Users\andolson\AppData\Local\ESRI\conda\envs\PyGDAL\Scripts\gdal_merge.py'
#
# # Retrieve all tif in directory
# files_to_mosaic = glob.glob('{0}/{1}'.format(rasters,'*.tif'))
# #print(files_to_mosaic)
#
# # All files need to be in a string for gdal_merge.py
# files_string = " ".join(files_to_mosaic)
# #print(files_string)
#
# # Define gdal command line as string
# command = "{0} -o {1}\{2}_mosaic.tif -of gtiff -n 0 ".format(dirGDAL, outDir,name) + files_string
# #command = "gdal_merge.py -o {0}\{1}_mosaic.tif -of gtiff ".format(outDir,name) + files_string
# #print(command)
# print(os.popen(command).read())
#
# print("Complete! Total runtime: {0}".format(dt.now()-startTime))
