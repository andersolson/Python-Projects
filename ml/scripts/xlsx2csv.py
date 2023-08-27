import pandas as pd
import os

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define variables and environments
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

dirPath = r'D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_BreakNames\ReDo\TestPoints'

#List to store path locations of files
fileLst = []

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##


def myFileLocations (fileEnding, directory, inLST):
    #Loop the directory and subdirectories for all .shp file endings and store them in a list
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(fileEnding):
                inLST.append(os.path.join(root, file))


def xlsx2csv(Infile, Outdir):
    # Get the name of the file
    name = Infile.split('\\')
    csvName = (name[-1].split('.',1)[0])

    # Read and store content
    # of an excel file
    read_file = pd.read_excel(Infile)

    # Write the dataframe object
    # into csv file
    read_file.to_csv('{0}\{1}.csv'.format(Outdir,csvName), index=None, header=True)

    print('Finished:\n{0}\{1}.csv\n'.format(Outdir, csvName))


##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Call Functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##


#Run myFileLocations() function
myFileLocations(".xlsx", dirPath, fileLst)
#print(fileLst)

for fName in fileLst:
    xlsx2csv(fName,dirPath)



