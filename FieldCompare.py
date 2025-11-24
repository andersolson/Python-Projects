'''****************************************************************
FieldCompare.py
Author(s): Anders Olson
Usage: Run script using python IDE or similar
Description:
        Compare field names from two input shapefiles and print out any differences
****************************************************************'''

import arcpy

# Function to find all field properties of a shapefile
def getFieldName(inSHP,inLST):

    # For each field in the feature class, print
    #  the field name, type, length, and precision.
    fields = arcpy.ListFields(inSHP)

    # Print name of shapefile being processed in function
    print("Field properties for: {}".format(inSHP))
    for field in fields:
        # Print field properties
        print("Field:       {0}".format(field.name))
        print("Alias:       {0}".format(field.aliasName))
        print("Type:        {0}".format(field.type))
        print("Is Editable: {0}".format(field.editable))
        print("Required:    {0}".format(field.required))
        print("Scale:       {0}".format(field.scale))
        print("Precision:   {0}".format(field.precision))
        inLST.append(field.name)

# Function to compare field properties of two lists and output differences
def diffLST(inLST1,inLST2):
    return (list(set(inLST1) - set(inLST2)))

fldLST_1 = []
fldLST_2 = []
getFieldName(inSHP=r'C:\Users\is_olson\Documents\Projects\Central-Square\Reports_Project\SQLServer-C3GISPROD4-CORE_GIS(sde).sde\SDE.GIS_APPLICATIONS\SDE.ACTIVE_DEVELOPMENT_PROJECTS',
             inLST=fldLST_1)
getFieldName(inSHP=r'C:\Users\is_olson\Documents\Projects\Central-Square\Reports_Project\SQLServer-C3GISDB-C3GIS(sde).sde\C3GIS.SDE.AdministrativeAreas\C3GIS.SDE.ACTIVE_DEVELOPMENT_PROJECTS',
             inLST=fldLST_2)

print(fldLST_1)
print(fldLST_2)
print(diffLST(fldLST_1,fldLST_2))
print(diffLST(fldLST_2,fldLST_1))