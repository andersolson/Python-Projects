# Python3 code to demonstrate
# to get random number from list
# using random.choice()
import random
import arcpy

# initializing list
test_list = [1, 4, 5, 2, 7]

# printing original list
print("Original list is : " + str(test_list))

# using random.choice() to
# get a random number
random_num = random.choice(test_list)

# printing random number
print("Random selected number is : " + str(random_num))

# Input table or shapefile to convert into list
inputTable = r'C:\Users\andolson\Documents\WORKING\WildFire\AI_Images\FirebreakData\QGIS\CO_ML_Validation.shp'

# List copy of table based on Break Name
agLst    = []
hdrLst   = []
ldrLst   = []
mdrLst   = []
srLst    = []
urLst    = []
unrLst   = []
waterLst = []
wildLst  = []

# Make a python list of all desired table attributes found in the input table
print("Reading Classes from Table...")
for row in arcpy.da.SearchCursor(inputTable, ['BREAK_NAME','TF_ID',]):

    if row[0] == 'Agriculture':
        agLst.append(row[1])
    elif row[0] == 'High Density Residential':
        hdrLst.append(row[1])
    elif row[0] == 'Low Density Residential':
        ldrLst.append(row[1])
    elif row[0] == 'Medium Density Residential':
        mdrLst.append(row[1])
    elif row[0] == 'Scattered Residential':
        srLst.append(row[1])
    elif row[0] == 'Urban':
        urLst.append(row[1])
    elif row[0] == 'Urban Non-Residential':
        unrLst.append(row[1])
    elif row[0] == 'Water':
        waterLst.append(row[1])
    elif row[0] == 'Wildland':
        wildLst.append(row[1])
    else:
        print('Error with: {0}'.format(row[0]))

print("Reading 50 Random IDs from Class List...")

# get a random 50 IDs from the input list
random_AG   = random.sample(agLst,50)
random_HDR  = random.sample(hdrLst,50)
random_LDR  = random.sample(ldrLst,50)
random_MDR  = random.sample(mdrLst,50)
random_SR   = random.sample(srLst,50)
random_UR   = random.sample(urLst,50)
random_UNR  = random.sample(unrLst,50)
random_W    = random.sample(waterLst,50)
random_Wild = random.sample(wildLst,50)

# print the random queries by class
print('\tAg :\n{0}'.format(random_AG))
print('\tHDR :\n{0}'.format(random_HDR))
print('\tLDR :\n{0}'.format(random_LDR))
print('\tMDR :\n{0}'.format(random_MDR))
print('\tSR :\n{0}'.format(random_SR))
print('\tUR :\n{0}'.format(random_UR))
print('\tUNR :\n{0}'.format(random_UNR))
print('\tWater :\n{0}'.format(random_W))
print('\tWild :\n{0}'.format(random_Wild))
