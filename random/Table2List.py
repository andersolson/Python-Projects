import arcpy

# Input table or shapefile to convert into list
inputTable = r'C:\Users\andolson\Documents\WORKING\WildFire\Tensorflow_Images\FirebreakData\QGIS\CO_ML_Image_Footprints.shp'

# Nested list copy of table
myList = []

# Make a python list of all desired table attributes found in the input table
print("Creating List from Table...")
for row in arcpy.da.SearchCursor(inputTable, ['STATE','BREAK_NAME','RISK_VALUE','FLAG','TF_ID','Shape_Leng','Shape_Area']):

    # Store row's attributes as a temporary list to nest in the main list
    tmpLst = []
    tmpLst.append(row[0]) #State
    tmpLst.append(row[1]) #Break_Name
    tmpLst.append(row[2]) #Risk_Value
    tmpLst.append(row[3]) #Flag
    tmpLst.append(row[4]) #TF_ID
    tmpLst.append(row[5]) #Shape_Leng
    tmpLst.append(row[6]) #Shape_Area

    # Write all the attribute values to my list copy
    myList.append(tmpLst)

print(myList)

#Sample list
'''
[['Colorado', 'Urban Non-Residential', 7, ' ', 1664019, 0.0164639999998, 1.66476919996e-05], 
['Colorado', 'Wildland', 9, 'Assigned on 062021', 1664152, 0.016714, 1.72299419999e-05], 
['Colorado', 'Wildland', 9, 'Assigned on 062021', 1664155, 0.016714, 1.72299419999e-05], 
['Colorado', 'Wildland', 9, 'Assigned on 062021', 1664160, 0.016712, 1.7225284e-05], 
['Colorado', 'Wildland', 9, 'Assigned on 062021', 1664162, 0.0167140000001, 1.72299420002e-05]]
'''