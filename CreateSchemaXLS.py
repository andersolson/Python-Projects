import arcpy
import pandas

# Lists for pandas dictionary
fieldName   = []
fieldType   = []
fieldLength = []
fieldPrecis = []

# For each field in the feature class, print
# the field name, type, length, and precision.
fields = arcpy.ListFields(r"C:\Users\andolson\Documents\WORKING\UST_LUST\Data\MA\BWP_PT_UST.shp")

for field in fields:
    # Print field properties
    # print("Field:       {0}".format(field.name))
    # print("Type:        {0}".format(field.type))
    # print("Length:      {0}".format(field.length))
    # print("Precision:   {0}".format(field.precision))

    fieldName.append(field.name)
    fieldType.append(field.type)
    fieldLength.append(field.length)
    fieldPrecis.append(field.precision)

# print(fieldName)
# print(fieldType)
# print(fieldLength)
# print(fieldPrecis)


thisdict = {"Field": fieldName,
            "Type": fieldType,
            "Length": fieldLength,
            "Precision": fieldPrecis
            }

# Create a Pandas dataframe from the data.
df = pandas.DataFrame(thisdict)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pandas.ExcelWriter(r'C:\Users\andolson\Documents\WORKING\pandas_simple0.xlsx')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
# Output excel file is written in the same location where the
# script is saved.
writer.save()

print(thisdict)