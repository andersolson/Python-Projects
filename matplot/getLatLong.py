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

shpFile = r"C:\Users\aolson\Documents\Working\GoogleSHP\AOIs\sampleAOIShape.shp"

pnts = []
#create a point list            
with arcpy.da.SearchCursor(shpFile, ("SHAPE@")) as cursor:
    for row in cursor:
        for part in row[0]:
            for pnt in part:
                tmpLst = []
                x = pnt.X 
                y = pnt.Y
                tmpLst.append(x)
                tmpLst.append(y)
                #print(tmpLst)
                pnts.append(tmpLst)

print(pnts)