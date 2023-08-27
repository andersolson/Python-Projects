import os
from datetime import datetime as dt
import arcpy
from arcpy.sa import *



dbfsave = r"D:\Tyler\WFDefensibleSpace\ZonalStats\\"+"zonalStats_"+imagename+'.dbf'
ZonalStatisticsAsTable(outFeatureClass, "FID", save,dbfsave,'DATA','ALL')
arcpy.MakeFeatureLayer_management(outFeatureClass,'Buffers')
arcpy.AddJoin_management("Buffers", "FID", dbfsave, "FID_")
final_location = r"D:\Tyler\WFDefensibleSpace\_Final\\"
final_file= imagename+"_NDVI_Buffers.shp"
arcpy.FeatureClassToShapefile_conversion(["Buffers"], final_location)

