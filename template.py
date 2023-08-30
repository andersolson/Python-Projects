#---------------------------------------------------------------------------
# <name of script.py>
#
# Author: Anders Olson 
#
# Usage:  Requires arcpy and python 3, run as stand-alone script.
#
# Description: Script creates x,y,z... add description of script...
# ---------------------------------------------------------------------------

import arcpy
import datetime
from datetime import datetime

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define variables and environments
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Set the arcpy overwriteOutput ON
arcpy.gp.overwriteOutput = True

# Create output messages for arcpy
def outputMessage(msg):
    print(msg)
    arcpy.AddMessage(msg)

def outputError(msg):
    print(msg)
    arcpy.AddError(msg)

# Start a timer
startTime = datetime.now()

# Define some variables
varX = 'Some text'
varY = 45.2
workspace = r'C:\Users\andolson\someGDB.gdb'

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

'''
Summary: Function creates x,y,z thing...

Parameters:
inputData -- <Description of input data>
inVar     -- <Description of input variable> 

Returns:
outputData -- <Description of output data>  

'''

def someFunction0 (inputData, inVar, outputData):
    varSum = inputData + inVar
    outputMessage(varSum)
    return outputData

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Call Functions & Run Code
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Run a function
someFunction0(4, 3, r'C:\Users\andolson')

# Run some code
x = len(varX)

for n in range(x):
    outputMessage(n)

# Print timer progress
outputMessage('Task Completed!\nFinal run time is: {}'.format(datetime.now() - startTime))
