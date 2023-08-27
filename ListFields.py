import arcpy

# For each field in the feature class, print
#  the field name, type, length, and precision.
fields = arcpy.ListFields(r"C:\Users\andolson\Documents\WORKING\UST_LUST\Data\MA\BWP_PT_UST.shp")

for field in fields:
    # Print field properties
    print("Field:       {0}".format(field.name))
    print("Alias:       {0}".format(field.aliasName))
    print("Type:        {0}".format(field.type))
    print("Is Editable: {0}".format(field.editable))
    print("Required:    {0}".format(field.required))
    print("Scale:       {0}".format(field.scale))
    print("Precision:   {0}".format(field.precision))

