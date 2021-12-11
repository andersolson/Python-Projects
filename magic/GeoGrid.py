import arcpy

Latitude = input("Latitude (dd): ")
# param0 = arcpy.Parameter(
#             displayName="Latitude",
#             name="Latitude (Decimal Degrees)",
#             datatype="String",
#             parameterType="Required",
#             direction="Input")

Longitude = input("Longitude (dd): ")
# param1 = arcpy.Parameter(
#             displayName="Longitude",
#             name="Longitude (Decimal Degrees)",
#             datatype="String",
#             parameterType="Required",
#             direction="Input")

WidthxHieght = input("Dimension W x H (miles): ")
# param2 = arcpy.Parameter(
#             displayName="Width",
#             name="Width (Kilometers)",
#             datatype="String",
#             parameterType="Required",
#             direction="Input")

outputShapefile = input("Output Path (Name is GRID.shp): ")
# param4 = arcpy.Parameter(
#             displayName="Shapefile Output",
#             name="Shapefile Output",
#             datatype="Shapefile",
#             parameterType="Required",
#             direction="Output")


def outputMessage(msg):
    print
    msg
    arcpy.AddMessage(msg)

def outputError(msg):
    print
    msg
    arcpy.AddError(msg)

# Set the overwriteOutput ON
arcpy.gp.overwriteOutput = True

# Set the workspace
ScratchFolder = arcpy.env.scratchFolder
arcpy.env.workspace = "in_memory"
outputMessage(arcpy.env.workspace)

# outputMessage("ScratchFolder is:  " + ScratchFolder)
# if not os.path.exists(ScratchFolder):
#	os.makedirs(ScratchFolder)

# get parameters: Create Point Feature Class
# strWorkspace   = ScratchFolder
# param1         = "0" #User enters Latitude
# param2         = "0" #User enters Longitude
# WIDTH_         = "10" #User enters AOI Width
# HEIGHT_        = "20" #User enters AOI Height
# CenPoint       = "POINTS"
# buff_W         = "Buff_W" #Name of the WIDTH_ Buffer
# buff_H         = "Buff_H" #Name of the HEIGHT_ Buffer
# tempSHP        = "tempSHP"
# outAOI         = r"E:\Working\AOI.shp"
# spRef          = arcpy.SpatialReference('WGS 1984')

# strWorkspace   = ScratchFolder
param1 = parameters[0].valueAsText   # arcpy.GetParameterAsText(0) #User enters Latitude
param2 = parameters[1].valueAsText   # arcpy.GetParameterAsText(1) #User enters Longitude
WIDTH_ = parameters[2].valueAsText   # param2 #arcpy.GetParameterAsText(2) #User enters AOI Width
HEIGHT_ = parameters[3].valueAsText  # param3 #arcpy.GetParameterAsText(3) #User enters AOI Height
CenPoint = "POINTS"
buff_W = "Buff_W"  # Name of the WIDTH_ Buffer
buff_H = "Buff_H"  # Name of the HEIGHT_ Buffer
tempSHP = "tempSHP"
outAOI = parameters[4].valueAsText  # param4 #arcpy.GetParameterAsText(4) #"AOI"
spRef = arcpy.SpatialReference('WGS 1984')

# Create Point Feature Class for input to buffer gp tool (!!!!!THIS CUASES PROBLEMS IN 10.2!!!!!) LOOK UP how to use PointGeometry (arcpy)
# OR arcpy.Point(x,y) OR arcpy.PointGeometry(point)

try:
    # Create an empty Point object
    #
    point = arcpy.Point()

    # A list to hold the PointGeometry objects
    #
    pointGeometryList = []

    # For each coordinate pair, populate the Point object and create
    # a new PointGeometry
    # for pt in pointList:
    # point.X = pt[0]
    # point.Y = pt[1]

    point.X = float(param2)  # User input for Longitude
    point.Y = float(param1)  # User input for Latitude

    pointGeometry = arcpy.PointGeometry(point)
    pointGeometryList.append(pointGeometry)

    # Create a copy of the PointGeometry objects, by using pointGeometryList
    # as input to the CopyFeatures tool.
    #
    arcpy.CopyFeatures_management(pointGeometryList, CenPoint)
    arcpy.DefineProjection_management(CenPoint, spRef)

    outputMessage(arcpy.GetMessages(0))

except arcpy.ExecuteError:
    outputMessage(arcpy.GetMessages(2))

except Exception as ex:
    outputMessage(ex.args[0])

# Buffer the Lat/Long point
try:
    W_Buff = float(WIDTH_) / 2
    H_Buff = float(HEIGHT_) / 2
    distance_W = str(W_Buff) + " Kilometers"
    distance_H = str(H_Buff) + " Kilometers"
    arcpy.Buffer_analysis(CenPoint, buff_W, distance_W, "FULL", "ROUND", "ALL")
    arcpy.Buffer_analysis(CenPoint, buff_H, distance_H, "FULL", "ROUND", "ALL")
    # arcpy.FeatureEnvelopeToPolygon_management(buff_W, outAOI, "SINGLEPART")
    # arcpy.MinimumBoundingGeometry_management(buff_W, outAOI, "RECTANGLE_BY_AREA", "NONE")

    outputMessage(arcpy.GetMessages(0))

except arcpy.ExecuteError:
    arcpy.AddError(arcpy.GetMessages(2))

except Exception as ex:
    arcpy.AddError(ex.args[0])

# Create the Rectangle AOI
if arcpy.Exists(buff_W):
    W_pntlist = []
    W_desc = arcpy.gp.Describe(buff_W)
    W_extent = str(W_desc.Extent).split(" ")
    W_pntlist.append(W_extent)

    H_pntlist = []
    H_desc = arcpy.gp.Describe(buff_H)
    H_extent = str(H_desc.Extent).split(" ")
    H_pntlist.append(H_extent)

    try:
        arcpy.CreateFeatureclass_management("in_memory", tempSHP, 'POLYLINE', "#", "DISABLED", "DISABLED",
                                            spRef)
        myCursor = arcpy.InsertCursor(tempSHP)
        point = arcpy.Point()
        array = arcpy.Array()

        point.X = float(W_extent[0])
        point.Y = float(H_extent[1])
        array.add(point)
        point.X = float(W_extent[0])
        point.Y = float(H_extent[3])
        array.add(point)
        point.X = float(W_extent[2])
        point.Y = float(H_extent[3])
        array.add(point)
        point.X = float(W_extent[2])
        point.Y = float(H_extent[1])
        array.add(point)
        point.X = float(W_extent[0])
        point.Y = float(H_extent[1])
        array.add(point)

        # Create new row to put pnt into
        row = myCursor.newRow()
        # Assign pnt obj to Shape field
        row.Shape = array
        # "save" the insert
        myCursor.insertRow(row)
        del row

        if myCursor:
            del myCursor

        # arcpy.FeatureToPolygon_management(tempSHP, outAOI)
        arcpy.MinimumBoundingGeometry_management(tempSHP, outAOI, "RECTANGLE_BY_AREA", "ALL")

        outputMessage(arcpy.GetMessages(0))

    except arcpy.ExecuteError:
        arcpy.AddError(arcpy.GetMessages(2))

    except Exception as ex:
        arcpy.AddError(ex.args[0])

return