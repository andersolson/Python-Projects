# For every shapefile in the directory, add spatial indices (.sbn, and .sbx)
import os
import arcpy

dir = 'K:\3 Risk\1 Natural Hazards\2 Coastal\Storm Surge\Data\Release Data\2019_04\Data\FL'

for dirpath, dirs, files in os.walk(dir):
	for file in files:
		if file.endswith('.shp'):
			arcpy.AddSpatialIndex_management(dirpath + '/' + file)
			