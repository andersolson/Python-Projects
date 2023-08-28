# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 17:42:04 2022


"""

import os, glob
import archook
archook.get_arcpy(pro=True)
import arcpy
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
from arcpy.sa import *
arcpy.env.qualifiedFieldNames = False
from datetime import datetime as dt
inlocation = r"D:\Tyler\WFDefensibleSpace\Structure_Footprint"
outlocation = r'D:\Tyler\WFDefensibleSpace\Structure_Footprint\Buffer\\'
os.chdir(inlocation)
filelist = []
for file in glob.glob("*.shp"):
    filelist.append(file)
for x in range(len(filelist)):
    shapefilename = filelist[x].split('\\')[len(filelist[x].split('\\'))-1][:-4]
    arcpy.MakeFeatureLayer_management(filelist[x],'structures')
    outFeatureClass = r"{0}Def_Space_Zones_{1}.shp".format(outlocation,shapefilename)
    distances = [5,30,100]
    bufferUnit = "feet"
    arcpy.MultipleRingBuffer_analysis(inlocation+'\\'+filelist[x], outFeatureClass, distances, bufferUnit, "", "ALL",'OUTSIDE_ONLY')
    arcpy.Delete_management("structures")
    
