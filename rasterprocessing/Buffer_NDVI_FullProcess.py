# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import geopandas
import archook
archook.get_arcpy(pro=True)
import arcpy
arcpy.CheckOutExtension("Spatial")
from arcpy.sa import *
arcpy.env.qualifiedFieldNames = False
from datetime import datetime as dt
arcpy.env.overwriteOutput = True
starttime = dt.now()
#things to do:
#1. 
#2. 
#3. 
#4. 
#5. 

structures = r"D:\Tyler\WFDefensibleSpace\Structure_Footprint\06015_structure.shp"
tile = r"D:\Tyler\WFDefensibleSpace\Images\ortho_1-1_hc_s_ca015_2020_1.sid"
imagename = tile.split('\\')[len(tile.split('\\'))-1][:-4]


# test = df.buffer(20)
# test.to_file(r"D:\Tyler\WFDefensibleSpace\Structure_Footprint\Buffer\Test20.shp")


arcpy.MakeFeatureLayer_management(structures,'structures')
inFeatures = "structures"
outFeatureClass = "D:\Tyler\WFDefensibleSpace\Structure_Footprint\Buffer\Def_Space_Zones_06015.shp"
distances = [5,30,100]
bufferUnit = "feet"

# Execute MultipleRingBuffer
arcpy.MultipleRingBuffer_analysis(inFeatures, outFeatureClass, distances, bufferUnit, "", "NONE",'OUTSIDE_ONLY')
arcpy.Delete_management("structures")
print("total time was {0}".format(dt.now()-starttime))
nir = Float(Raster(tile + r"\Band_1"))
red = Float(Raster(tile + r"\Band_2"))
ndvi = (nir - red) / (nir + red)
# arcpy.Delete_management("Buffers")
# ndvi.save(r"D:\Tyler\WFDefensibleSpace\NDVI_Images\\"+imagename+'.tif')
# final_ndvi = r"D:\Tyler\WFDefensibleSpace\NDVI_Images\NDVI_ortho_1-1_hc_s_ca015_2020_1.tif"
# imagename2 = final_ndvi.split('\\')[len(final_ndvi.split('\\'))-1]
# ndvi_final = Raster(final_ndvi)
save = r'D:\Tyler\WFDefensibleSpace\NDVI_Images\Binary\\'+"Binary_"+imagename+".tif"
basename = "Binary_"+imagename+".tif"
output = arcpy.sa.Con(ndvi>=.2,1,0)
output.save(save)
dbfsave = r"D:\Tyler\WFDefensibleSpace\ZonalStats\\"+"zonalStats_"+imagename+'.dbf'
ZonalStatisticsAsTable(outFeatureClass, "FID", save,dbfsave,'DATA','ALL')
arcpy.MakeFeatureLayer_management(outFeatureClass,'Buffers')
arcpy.AddJoin_management("Buffers", "FID", dbfsave, "FID_")
final_location = r"D:\Tyler\WFDefensibleSpace\_Final\\" 
final_file= imagename+"_NDVI_Buffers.shp"
arcpy.FeatureClassToShapefile_conversion(["Buffers"], final_location)

print("total time was {0}".format(dt.now()-starttime))
