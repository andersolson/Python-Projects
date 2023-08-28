# ---------------------------------------------------------------------------
# FindFCs.py
#
# Author: Anders Olson
#
# Usage:  Requires arcpy and python 3, can be run stand-alone
#
# Description: Script runs through a GDB and finds all the feature classes
#              stored inside a feature dataset. The list of feature classes
#              is then used to clip a dataset.
# ---------------------------------------------------------------------------

import os
import arcpy

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define variables and environments
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Set the arcpy overwriteOutput ON
arcpy.gp.overwriteOutput = True

# Set the GDB workspace environment
arcpy.env.workspace = r"C:\Users\andolson\Documents\WORKING\FlashFloodFrequency\GridTest.gdb"

# Clip these features to the features found in gdb
in_features = r"C:\Users\andolson\Documents\WORKING\FlashFloodFrequency\FlashFloodFreq_2020_07.shp"

# DS for grid cell output
gridCells  = r"C:\Users\andolson\Documents\WORKING\FlashFloodFrequency\GridTest.gdb\GridCells"

# Run overlap on all of these features
clippedFCs = r"C:\Users\andolson\Documents\WORKING\FlashFloodFrequency\GridTest.gdb\GridClip"


#List of FC path locations in GDB
myFCLst = []


#Store the pathnames to all FCs in a designated workspace to a list
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

for ds in datasets:
    #print(ds)
    if ds == 'GridCells':
        #print(ds)
        for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
            path = os.path.join(arcpy.env.workspace, ds, fc)
            myFCLst.append(path)
            #print(path)
    else:
        pass

#print(myFCLst)

#Count for output name
count = 0

#Loop through the FCs and clip input shape to grid
for FC in myFCLst:
    #print(FC)
    print(r"Clipping: {}".format(FC))
    out_feature_class = r"GridClip\clip{0}".format(count)
    arcpy.Clip_analysis(in_features, FC, out_feature_class)
    count += 1

'''
for fc in arcpy.ListFeatureClasses(clippedFCs):
    # path = os.path.join(clippedFCs, ds, fc)
    # myFCLst2.append(path)
    print(fc)


#Loop through the clipped FCs and run count overlap
for FC in myFCLst:
    arcpy.CountOverlappingFeatures(FC, outFeat)
'''

