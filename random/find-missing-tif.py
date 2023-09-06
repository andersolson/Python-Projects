import pathlib

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

'''
Summary:
Function that creates a path object for all desired files in a directory that match the pattern/file ending.

Parameters:
fileEnding -- string for desired file ending e.g. '.tif'
directory  -- string location of the parent directory to search recursively

Returns:
fileLst  -- python list of files within the directory that match file ending
'''
def findFilePaths(fileEnding, directory):
    # Create a path object for the directory
    data_dir = pathlib.Path(directory)

    # Recursive search within directory for file endings
    myFiles = list(data_dir.rglob(fileEnding))

    return myFiles

'''
Summary:
Function that checks if a file paths from list already exists and returns a list of file paths that do not exist.

Parameters:
lstInput    -- python list of file path names

Returns:
missingLst  -- python list of all missing file path names
'''
def findMissing(lstInput):
    missingLst = []

    # Loop through list for pathnames
    for i in lstInput:

        # Check if file already exists
        if not os.path.isfile(i):
            missingLst.append(i)
        # else:
        #     outputMessage("\tFile already exists:\n\t{0}".format(i))

    print(f'Found {len(missingLst)} missing files.')

    return missingLst

'''
Summary:
Function that checks if a file paths from list already exists and returns a list of file paths that do not exist.

Parameters:
fileEnding -- string for desired file ending e.g. '.tif'
directory  -- string 

Returns:
fileLst  -- python list of files within the directory that match file ending
'''
def myFileLocations(fileEnding, directory):
    fileLst = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(fileEnding):
                fileLst.append(os.path.join(root, file))

    return fileLst

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Call Functions & Execute Code
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Parent directory for where files are stored.
main_dir = r'C:\Users\andolson\Documents\WORKING\WildFire\Tensorflow_Images\images'

data_dir = pathlib.Path(main_dir)
print(data_dir)

myFiles = list(data_dir.glob('*.tif'))
print(myFiles)
