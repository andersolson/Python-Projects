# Compare field names from two input shapefiles and print out any differences

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
getFieldName(r"C:\Users\andolson\Documents\WORKING\UST_LUST\Data\MA\BWP_PT_UST.shp", fldLST_1)
getFieldName(r"C:\Users\andolson\Documents\WORKING\UST_LUST\Data\IN\UST_IDEM_IN.shp", fldLST_2)

print(fldLST_1)
print(fldLST_2)
print(diffLST(fldLST_1,fldLST_2))