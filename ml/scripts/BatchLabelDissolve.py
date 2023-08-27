import geopandas as gpd
from datetime import datetime as dt
import sys

print("Running: {0}".format(sys.argv[0]))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define variables and environments
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Start a timer
startTime = dt.now()

# Txt list of all desired states with names as they appear in the source directory
# e.g. Firebreak_2022_11_CO_Internal.shp - 'CO'
stateList = r'D:\Projects\WORKING\ML\StateList.txt'
#stateList = r'D:\Projects\WORKING\ML\StateListCO.txt'

# Shapefile input location
inDir = r'D:\Projects\WORKING\ML\vectors\Firebreak_2022_11\Internal'

# Shapefile output location
outDir = r'D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_Select'

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define Functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

def dissolve_BreakName(state, inSHP,outPath):
    print("\tRunning dissolve for: \n{0}".format(inSHP))

    fbState = gpd.read_file(inSHP)

    try:
        print('\tRunning Agriculture...')
        ag         = fbState[fbState['RISK_VALUE']==1]
        agBoundary = ag[['STATE', 'BREAK_NAME', 'geometry']]
        dissolveAg = agBoundary.dissolve(by='BREAK_NAME')
        #dissolveAg.to_file(outPath + "\{0}_Agriculture_dis.shp".format(state))
        agBoundary.to_file(outPath + "\{0}_Agriculture.shp".format(state))
        #print(outPath + "\{0}_Agriculture.shp".format(state))
    except:
        print('Error: Agriculture failed!')

    try:
        print('\tRunning High Density Residential...')
        hdr         = fbState[fbState['RISK_VALUE'] == 2]
        hdrBoundary = hdr[['STATE', 'BREAK_NAME', 'geometry']]
        dissolveHdr = hdrBoundary.dissolve(by='BREAK_NAME')
        #dissolveHdr.to_file(outPath + "\{0}_HDR_dis.shp".format(state))
        hdrBoundary.to_file(outPath + "\{0}_HDR.shp".format(state))
        #print(outPath + "\{0}_HDR.shp".format(state))
    except:
        print('Error: High Density Residential failed!')

    try:
        print('\tRunning Medium Density Residential...')
        mdr         = fbState[fbState['RISK_VALUE'] == 3]
        mdrBoundary = mdr[['STATE', 'BREAK_NAME', 'geometry']]
        dissolveMdr = mdrBoundary.dissolve(by='BREAK_NAME')
        #dissolveMdr.to_file(outPath + "\{0}_MDR_dis.shp".format(state))
        mdrBoundary.to_file(outPath + "\{0}_MDR.shp".format(state))
        #print(outPath + "\{0}_MDR.shp".format(state))
    except:
        print('Error: Medium Density Residential failed!')

    try:
        print('\tRunning Low Density Residential...')
        ldr         = fbState[fbState['RISK_VALUE'] == 4]
        ldrBoundary = ldr[['STATE', 'BREAK_NAME', 'geometry']]
        dissolveLdr = ldrBoundary.dissolve(by='BREAK_NAME')
        #dissolveLdr.to_file(outPath + "\{0}_LDR_dis.shp".format(state))
        ldrBoundary.to_file(outPath + "\{0}_LDR.shp".format(state))
        #print(outPath + "\{0}_LDR.shp".format(state))
    except:
        print('Error: Low Density Residential failed!')

    try:
        print('\tRunning Scattered Residential...')
        sr         = fbState[fbState['RISK_VALUE'] == 5]
        srBoundary = sr[['STATE', 'BREAK_NAME', 'geometry']]
        dissolveSr = srBoundary.dissolve(by='BREAK_NAME')
        #dissolveSr.to_file(outPath + "\{0}_SR_dis.shp".format(state))
        srBoundary.to_file(outPath + "\{0}_SR.shp".format(state))
        #print(outPath + "\{0}_SR.shp".format(state))
    except:
        print('Error: Scattered Residential failed!')

    try:
        print('\tRunning Urban...')
        urb         = fbState[fbState['RISK_VALUE'] == 6]
        urbBoundary = urb[['STATE', 'BREAK_NAME', 'geometry']]
        dissolveUrb = urbBoundary.dissolve(by='BREAK_NAME')
        #dissolveUrb.to_file(outPath + "\{0}_Urban_dis.shp".format(state))
        urbBoundary.to_file(outPath + "\{0}_Urban.shp".format(state))
        #print(outPath + "\{0}_Urban.shp".format(state))
    except:
        print('Error: Urban failed!')

    try:
        print('\tRunning Urban Non-Residential...')
        unr         = fbState[fbState['RISK_VALUE'] == 7]
        unrBoundary = unr[['STATE', 'BREAK_NAME', 'geometry']]
        dissolveUnr = unrBoundary.dissolve(by='BREAK_NAME')
        #dissolveUnr.to_file(outPath + "\{0}_UNR_dis.shp".format(state))
        unrBoundary.to_file(outPath + "\{0}_UNR.shp".format(state))
        #print(outPath + "\{0}_UNR.shp".format(state))
    except:
        print('Error: Urban Non-Residential failed!')

    try:
        print('\tRunning Water...')
        h2o         = fbState[fbState['RISK_VALUE'] == 8]
        h2oBoundary = h2o[['STATE', 'BREAK_NAME', 'geometry']]
        dissolveH2o = h2oBoundary.dissolve(by='BREAK_NAME')
        #dissolveH2o.to_file(outPath + "\{0}_Water_dis.shp".format(state))
        h2oBoundary.to_file(outPath + "\{0}_Water.shp".format(state))
        #print(outPath + "\{0}_Water.shp".format(state))
    except:
        print('Error: Water failed!')

    try:
        print('\tRunning Wildland...')
        wl         = fbState[fbState['RISK_VALUE'] == 9]
        wlBoundary = wl[['STATE', 'BREAK_NAME', 'geometry']]
        dissolveWl = wlBoundary.dissolve(by='BREAK_NAME')
        #dissolveWl.to_file(outPath + "\{0}_Wildland_dis.shp".format(state))
        wlBoundary.to_file(outPath + "\{0}_Wildland.shp".format(state))
        #print(outPath + "\{0}_Wildland.shp".format(state))
    except:
        print('Error: Wildland failed!')


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Execute Process
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Notify user and write to log
print("Start time: {0}".format(startTime))

with open(stateList) as f:
    for line in f:

        pStart = dt.now()

        # Pull state abbreviation from text file
        stateAbbrev = line.rstrip()
        print('Started Processing for: {0}'.format(stateAbbrev))

        # Create input path to shapefile
        stateFB = inDir + r'\Firebreak_2022_11_{0}_Internal.shp'.format(stateAbbrev)

        dissolve_BreakName(stateAbbrev, stateFB, outDir)

        print("{0} complete! Runtime: {1}".format(stateAbbrev, dt.now() - pStart))

print("Complete! Total runtime: {0}".format(dt.now()-startTime))