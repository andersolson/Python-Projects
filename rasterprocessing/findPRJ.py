import arcpy
import os

def myFileLocations(fileEnding, directory, inLST):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(fileEnding):
                inLST.append(os.path.join(root, file))

srcDir = r'W:\naip\2022\ca\source\tiles\Group4'
tilelist = []

myFileLocations('.tif', srcDir, tilelist)

print(len(tilelist))

# Loop through the list
for raster in tilelist:
    # Create the spatial reference object
    spatial_ref = arcpy.Describe(raster).spatialReference

    print(raster)
    print(spatial_ref.name)

    # # If the spatial reference is unknown
    # if spatial_ref.name == None:
    #     print("{} has an unknown spatial reference".format(raster))

    # # Otherwise, print out the feature class name and spatial reference
    # else:
    #     print("{} : {}".format(raster, spatial_ref.name))