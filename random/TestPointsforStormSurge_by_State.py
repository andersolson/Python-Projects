# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:14:07 2019
Modified on Tues Dec 8 2020

"""
import arcpy
from arcpy import env
import os

###########     3  variable to change in the section below ############################################################
# Change this variable to the top level directory that houses the polygon shapefiles to be sampled
#InputShapefilesFolder = " "
InputShapefilesFolder = r"D:\D\Storm_surge\FromDave\MergedStates"

# Assumes that there are coresponding points shapefiles for each of the above shapefiles that are being sampled.
#Change this variable to th folder that houses all the individual test points - it will only run on those that have
#comparable shapefiles in the folder above
#InputTestPointsFolder = ""
InputTestPointsFolder = r"D:\D\Storm_surge\FromDave\SamplePoints"

#Change this to where you want to export the spatial joins and the final table.Make sure it's empty to start with
#workspace = r"C:/temp"
workspace = r"D:\D\Storm_surge\FromDave\tempWorkspace"
######################################################################################################################

arcpy.env.workspace = workspace

def stripextension(pfile):
    return pfile[0:len(pfile)-4]
    
def fipsfromfile(pfile):
    return pfile[:2]
    #Surge10m_[YYYY]_[MM]_[FIPSTCO].shp

for dirpath, dirs, files in os.walk(InputShapefilesFolder):
    for file in files:
        if file.endswith('.shp'):

            #print(InputTestPointsFolder + "\\" + fipsfromfile(file) + "_TestPoints.shp")
            #print(dirpath + "\\" + file)
      
            #Spatial Join to the original layer to pull the values
            arcpy.SpatialJoin_analysis(InputTestPointsFolder + "\\" + fipsfromfile(file) + "_TestPoints.shp", dirpath + "\\" + file, workspace + "\\" + stripextension(file) + "sjpoints.shp", "JOIN_ONE_TO_ONE", "KEEP_ALL")
            
            #Delete extraneous fields from the resulting layer
            arcpy.DeleteField_management(workspace + "\\" + stripextension(file) + "sjpoints.shp", ["Join_Count", "TARGET_FID", "CID"])
            print("Finished ", workspace + "\\" + stripextension(file) + "sjpoints.shp")
            
            
# after all that, merge all the files together and export the table

arcpy.env.workspace = workspace
shplist =  arcpy.ListFeatureClasses('*.shp')  
arcpy.Merge_management(shplist, os.path.join(workspace, 'Merged_fc.shp')) 
arcpy.TableToExcel_conversion('Merged_fc.shp', 'TestPointsTable.xlsx')



