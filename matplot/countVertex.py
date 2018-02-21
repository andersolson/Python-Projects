import arcpy

def outputMessage(msg):
    print msg
    arcpy.AddMessage(msg)

def outputError(msg):
    print msg
    arcpy.AddError(msg)

# Set the overwriteOutput ON
arcpy.gp.overwriteOutput = True

# Set the workspace
ScratchFolder = arcpy.env.scratchFolder	
arcpy.env.workspace = "in_memory"

shpFile = r"C:\Users\aolson\Documents\Working\GoogleSHP\AOIs\multi_single.shp"

with arcpy.da.SearchCursor(shpFile, ("SHAPE@")) as cursor:
    for row in cursor:
        for part in row[0]:
            count = 0
            for pnt in part:
                count += 1
            print(count)