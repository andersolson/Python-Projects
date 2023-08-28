# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 19:49:15 2022


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
os.chdir(r"D:\Tyler\WFDefensibleSpace\Images")
tilelist = []
for file in glob.glob("*.SID"):
    tilelist.append(file)
for x in range(len(tilelist)):
    starttime = dt.now()
    imagename = tilelist[x].split('\\')[len(tilelist[x].split('\\'))-1][:-4]
    nir = Float(Raster(tilelist[x] + r"\Band_1"))
    red = Float(Raster(tilelist[x] + r"\Band_2"))
    ndvi = (nir - red) / (nir + red)
    save = r'D:\Tyler\WFDefensibleSpace\NDVI_Images\Binary\\'+"Binary_"+imagename+".tif"
    basename = "Binary_"+imagename+".tif"
    output = arcpy.sa.Con(ndvi>=.2,1,0)
    output.save(save)
    print("took {0} to complete {1} tile".format(dt.now()-starttime, imagename))
