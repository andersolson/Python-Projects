# importing module
from pandas import *
from pathlib import Path
import csv
import re

# Define csv Path
myCSV = Path(r'C:\Users\andolson\Documents\WORKING\andolson_ML_AZ_Results_Table.csv')

# reading CSV file
data = read_csv(myCSV)

# converting column data to list
cNest = data['Image Name'].tolist()

newList  = []
csv_path = Path(r'C:\Users\andolson\Documents\WORKING\newCSV.csv')

# for n in cNest:
#     # print(type(n))
#     # print(n)
#     newStr = re.sub(r"[\[\]\\']", "", n)
#     #print(newStr)
#     newItem = newStr.split(', ')
#     #print(newItem)
#     newList.append(newItem)
#
# # print(newList)
#
# # Write the results to the CSV file
# with open(csv_path, "w", newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Image Name", "Label", "Water Probability", "Wildland Probability"])  # Write the header
#     writer.writerows(newList)  # Write the data rows
#
# print(newList)

# Write the results to the CSV file
with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Image Name", "Label", "Water Probability", "Wildland Probability"])  # Write the header

    # Loop through rows in csv to reformat string
    for n in cNest:
        # Reformat string for csv table
        newStr = re.sub(r"[\[\]\\']", "", n)
        #print(newStr)
        newItem = newStr.split(', ')
        #print(newItem)

        # Write item row to csv
        writer.writerows([newItem])  # Write the data rows

print('Done.')

