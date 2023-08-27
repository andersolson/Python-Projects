field  = ["Ford", "Ferrari"]
typ    = ["Focus", "Rich Prick"]
length = [12, 256]
preci  = [4, 0.2]

thisdict = {"Field": field,
            "Type": typ,
            "Length": length,
            "Precision": preci
            }

import pandas

# Create a Pandas dataframe from the data.
df = pandas.DataFrame(thisdict)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pandas.ExcelWriter(r'C:\Users\andolson\Documents\WORKING\pandas_simple.xlsx')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
# Output excel file is written in the same location where the
# script is saved.
writer.save()

print(thisdict)