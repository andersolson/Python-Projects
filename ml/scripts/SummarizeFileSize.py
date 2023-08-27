import os
import csv

# Define the directory path
directory = r'B:\projects\FirebreakML\Firebreak_Water_Wildland\imagery\CO_Water_Wildland\wildland'

# Create a dictionary to store file sizes and their counts
file_sizes = {}

# Iterate over the files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    # Check if the item is a file
    if os.path.isfile(filepath):
        # Get the file size
        size = os.path.getsize(filepath)

        # Add the file size to the dictionary
        if size in file_sizes:
            file_sizes[size] += 1
        else:
            file_sizes[size] = 1

# Define the path for the CSV file
csv_file = r'B:\projects\FirebreakML\Firebreak_Water_Wildland\imagery\CO_Water_Wildland\wildland\file_sizes_summary.csv'

# Write the file sizes and counts to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["File Size", "Count"])

    for size, count in file_sizes.items():
        writer.writerow([size, count])

print(f"File sizes summary has been saved to {csv_file}.")