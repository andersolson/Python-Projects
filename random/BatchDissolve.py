import arcpy
import sys
from datetime import datetime

def outputMessage(msg):
    print(msg)
    arcpy.AddMessage(msg)

def outputError(msg):
    print(msg)
    arcpy.AddError(msg)

outputMessage("Running: {0}".format(sys.argv[0]))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define variables and environments
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Set the overwriteOutput ON
arcpy.gp.overwriteOutput = True

# Working ENV location
#workingGDB = r'D:\Storm_surge\Storm_surge_2021\FloridaTopoChecks\FloridaTopoCheck.gdb'
workingGDB = r'D:\Storm_surge_2021_04\Data\Working_data\Working_Surge_2021_04\Working_Surge_2021_04.gdb'

# Set working environment
arcpy.env.workspace = workingGDB

# State shapefile containing FIPSSTCO numbers
#stateShapefile = r'D:\Storm_surge\Storm_surge_2021\FloridaTopoChecks\FloridaFix\StormsurgeFL_2020.gdb\FL_TopoDataset\StormsurgeFL_2020'
stateShapefile = r'D:\Storm_surge_2021_04\Data\Source_data\2020_USAA\USAA\StormsurgeLA_2020.gdb\StormsurgeLA_2020'

# List of FIPSSTCO counties
countyList = []

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define Functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

def dissolveCounty(inFC,outFC):
    print("Running dissolve for: {0}".format(inFC))

    # Check that the feature class with the special projection exists
    if arcpy.Exists(inFC):
        # Dissolve shit
        arcpy.Dissolve_management(inFC, outFC, ["OBJECTID"], "", "MULTI_PART")

    else:
        print("{0} does not exist.".format(inFC))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Execute Process
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

#Start a timer
start_time = datetime.now()
outputMessage(start_time)

# List for storing duplicate FIPSSTCO numbers
cTracker = []

# Step One: Make an index list of all the county codes to select
outputMessage("Building county name index...")
for row in arcpy.da.SearchCursor(stateShapefile, ['FIPSSTCO']):
    if row[0] in cTracker:
        pass
    elif row[0] not in cTracker:
        countyList.append(row[0])
        cTracker.append(row[0])
    else:
        outputMessage("Error building county name index...")
outputMessage("County name index built...")

# Run time tracking
current_time = datetime.now()
run_time = current_time - start_time
outputMessage(run_time)
#outputMessage(len(countyList))

# create a counter for counties to be processed
cCounter = len(countyList)

# Step 2: Export each county as separate shapefile
outputMessage("Exporting FIPSSTCO county shapefile...")
for FIPSSTCO in countyList:
    #outputMessage(FIPSSTCO)
    whereClause = "FIPSSTCO = '{0}'".format(FIPSSTCO)
    outSHP      = "fipsstco_{0}".format(FIPSSTCO)

    #outputMessage(stateShapefile)
    #outputMessage(workingGDB)
    #outputMessage(outSHP)
    #outputMessage(whereClause)

    # Export selection to working GDB
    arcpy.conversion.FeatureClassToFeatureClass(stateShapefile, workingGDB, outSHP, whereClause)

    # Update counter
    cCounter -= 1
    outputMessage('{0} counties remain to export...'.format(cCounter))
outputMessage("FIPSSTCO county Export complete...")

# Run time tracking
current_time = datetime.now()
run_time = current_time - start_time
outputMessage(run_time)

# create a counter for counties to be processed
cCounter = len(countyList)

# Step 3: Dissolve all county shapefiles
outputMessage("Dissolving FIPSSTCO county shapefile...")
for FIPSSTCO in countyList:
    #outputMessage(FIPSSTCO)
    #inCounty  = r'D:\Storm_surge\Storm_surge_2021\FloridaTopoChecks\FloridaTopoCheck.gdb\fipsstco_{0}'.format(FIPSSTCO)
    #outCounty = r'D:\Storm_surge\Storm_surge_2021\FloridaTopoChecks\FloridaFix\StormsurgeFL_2020.gdb\dissolve_{0}'.format(FIPSSTCO)
    inCounty  = r'D:\Storm_surge_2021_04\Data\Working_data\Working_Surge_2021_04\Working_Surge_2021_04.gdb\fipsstco_{0}'.format(FIPSSTCO)
    outCounty = r'D:\Storm_surge_2021_04\Data\Working_data\Working_Surge_2021_04\Working_Surge_2021_04.gdb\dissolve_{0}'.format(FIPSSTCO)
    
    #outputMessage(inCounty)
    #outputMessage(outCounty)

    # Dissolve County
    dissolveCounty(inCounty, outCounty)

    # Update counter
    cCounter -= 1
    outputMessage('{0} counties remain to Dissolve...'.format(cCounter))
outputMessage("FIPSSTCO county Dissolve complete...")

end_time   = datetime.now()
total_time = end_time-start_time
outputMessage("Script Complete!")
outputMessage(total_time)
