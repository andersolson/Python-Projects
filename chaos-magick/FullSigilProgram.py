# Random Sigil Grid Generator
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
from matplotlib.path import Path
import math
import numpy as np
from datetime import datetime as dt

### Functions ###

# Obfuscate the Intent
def removeDuplicate(str):
    t = ""
    for i in str:
        if (i in t):
            pass
        else:
            t = t + i
    return t

# Define a function for locating letter position in the grid reference table
def find_in_heart_of_hearts(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            return (mylist.index(sub_list))

# Define a function for rotating the angle of the last marker symbol in a sigil
def markerRotation(xLST, yLST):

    # Set the coordinates for the last 2 points in the final sigil line
    startX = xLST[-2:][0]
    endX = xLST[-2:][1]
    startY = yLST[-2:][0]
    endY = yLST[-2:][1]

    # Calculate the angle in radians of the last sigil line
    myradians = math.atan2(endY - startY, endX - startX)

    # Convert radians to degrees to define marker rotation
    mydegrees = math.degrees(myradians)

    return mydegrees

# Generate the Tesla-style Sigil
def createTeslaSigil(intent, output):
    # Create a reference table and a grid for the sigil
    sigilValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Letters of the Alphabet +1 blank to equal 27
    sigilLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*']

    # Create a random codex
    sigilTableHeader = np.random.choice(sigilValues, 9, False)
    sigilTableBody = np.random.choice(sigilLetters, (3, 9), False)
    # print(sigilTableHeader)
    # print(sigilTableBody)

    # Nested list representation of the reference table
    refTable = []

    # Nested list of number values and letters
    for x in range(0, 9):
        nest = []
        nest.append(sigilTableHeader[x])
        nest.append(sigilTableBody[0][x])
        nest.append(sigilTableBody[1][x])
        nest.append(sigilTableBody[2][x])
        refTable.append(nest)
    # print(refTable)

    # Store the sigil position of letters in a list
    refLst = []
    for letter in intent:
        refLst.append(find_in_heart_of_hearts(refTable, letter))

    # Get a list of the numbers linked to the letters
    numberLst = []
    for i in refLst:
        numberLst.append(refTable[i][0])

    # Display matrices
    print('\nRandomized Sigil Table:\n' \
          '=====================================\n' \
          '| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |\n' \
          '|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n' \
          '| {9} | {10} | {11} | {12} | {13} | {14} | {15} | {16} | {17} |\n' \
          '| {18} | {19} | {20} | {21} | {22} | {23} | {24} | {25} | {26} |\n' \
          '| {27} | {28} | {29} | {30} | {31} | {32} | {33} | {34} | {35} |\n' \
          '=====================================\n'.format(sigilTableHeader[0], sigilTableHeader[1],
                                                           sigilTableHeader[2], sigilTableHeader[3],
                                                           sigilTableHeader[4], sigilTableHeader[5],
                                                           sigilTableHeader[6], sigilTableHeader[7],
                                                           sigilTableHeader[8],
                                                           sigilTableBody[0][0], sigilTableBody[0][1],
                                                           sigilTableBody[0][2], sigilTableBody[0][3],
                                                           sigilTableBody[0][4], sigilTableBody[0][5],
                                                           sigilTableBody[0][6], sigilTableBody[0][7],
                                                           sigilTableBody[0][8],
                                                           sigilTableBody[1][0], sigilTableBody[1][1],
                                                           sigilTableBody[1][2], sigilTableBody[1][3],
                                                           sigilTableBody[1][4], sigilTableBody[1][5],
                                                           sigilTableBody[1][6], sigilTableBody[1][7],
                                                           sigilTableBody[1][8],
                                                           sigilTableBody[2][0], sigilTableBody[2][1],
                                                           sigilTableBody[2][2], sigilTableBody[2][3],
                                                           sigilTableBody[2][4], sigilTableBody[2][5],
                                                           sigilTableBody[2][6], sigilTableBody[2][7],
                                                           sigilTableBody[2][8]))

    # Create a random sigil grid
    sigilGrid = np.random.choice(sigilValues, (3, 3), False)

    print('Randomized Sigil Grid:\n' \
          '=============\n' \
          '| {0} | {1} | {2} |\n' \
          '| {3} | {4} | {5} |\n' \
          '| {6} | {7} | {8} |\n' \
          '============='.format(sigilGrid[0][0], sigilGrid[0][1], sigilGrid[0][2], sigilGrid[1][0], sigilGrid[1][1],
                                 sigilGrid[1][2], sigilGrid[2][0], sigilGrid[2][1], sigilGrid[2][2]))

    print('\nNumber associated with letter:\n', numberLst, '\n')

    # List for tracking the order of numbers in the sigil grid
    gridNum = []
    gridNum.append(sigilGrid[0][0])
    gridNum.append(sigilGrid[0][1])
    gridNum.append(sigilGrid[0][2])
    gridNum.append(sigilGrid[1][0])
    gridNum.append(sigilGrid[1][1])
    gridNum.append(sigilGrid[1][2])
    gridNum.append(sigilGrid[2][0])
    gridNum.append(sigilGrid[2][1])
    gridNum.append(sigilGrid[2][2])
    # print('Sigil Grid as a list:\n', gridNum)

    # Get index location of number in the sigil grid
    sigilLocation = []
    for i in numberLst:
        sigilLocation.append(gridNum.index(i))

    xLst = []
    yLst = []

    for position in sigilLocation:
        if position == 0:
            xLst.append(9)
            yLst.append(15)
            # print("x,y = 1,3")
        elif position == 1:
            xLst.append(13)
            yLst.append(14)
            # print("x,y = 2,3")
        elif position == 2:
            xLst.append(15)
            yLst.append(10)
            # print("x,y = 3,3")
        elif position == 3:
            xLst.append(14)
            yLst.append(6)
            # print("x,y = 1,2")
        elif position == 4:
            xLst.append(11)
            yLst.append(3)
            # print("x,y = 2,2")
        elif position == 5:
            xLst.append(7)
            yLst.append(3)
            # print("x,y = 3,2")
        elif position == 6:
            xLst.append(4)
            yLst.append(6)
            # print("x,y = 1,1")
        elif position == 7:
            xLst.append(3)
            yLst.append(10)
            # print("x,y = 2,1")
        elif position == 8:
            xLst.append(5)
            yLst.append(14)
            # print("x,y = 3,1")
        else:
            print("Error: index out of range")

    # Tesla vortex coordinates
    x = [9, 13, 15, 14, 11, 7, 4, 3, 5]
    y = [15, 14, 10, 6, 3, 3, 6, 10, 14]

    # Define the endpoint marker symbol
    verts = [
        (0., 0.),  # Start, Center-Left
        (0., 80.),  # Left, top
        (20., 80.),  # Right, top
        (20., 0.),  # Center, Center-Right
        (20., -80.),  # Right, bottom
        (0., -80.),  # back to left, bottom
        (0., 0.),  # End, Center-Left
    ]

    codes = [
        Path.MOVETO,  # begin drawing
        Path.LINETO,  # straight line
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,  # close shape. This is not required for this shape but is "good form"
    ]

    # The new end point marker symbol
    path = Path(verts, codes)

    # Get the marker rotation angle
    rotate = markerRotation(xLst,yLst)

    # Define the custom marker symbol and the degrees of rotation
    m = MarkerStyle(path)
    m._transform.rotate_deg(rotate)

    # Define the size of the plot
    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.figure(figsize=(9, 9))

    # Add a circle outline. 8 appears to be the best size for these sigils
    circle1 = plt.Circle((9, 9), 8, color='r', fill=False)
    plt.gca().add_patch(circle1)

    # Draw the sigil lines with start point marker
    plt.plot(xLst, yLst, '-o', solid_capstyle="butt", solid_joinstyle="miter",
             color='red', linewidth=lineW, markevery=[0], markersize=markerW, zorder=1)

    # Add the rotated end marker symbol to plot
    plt.plot(xLst, yLst, marker=m, color='red', markevery=[-1], markersize=markerW*2.5)

    plt.margins(0.25)
    #plt.margins(0.50)
    #plt.margins(0.70)
    # plt.tight_layout()
    plt.axis('off')
    plt.savefig(output,
                bbox_inches='tight',
                transparent=True,
                pad_inches=0)

# Generate a Square-style Sigil
def createSquareSigil(intent, output):
    # Create a reference table and a grid for the sigil
    sigilValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    sigilLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*']

    # Create a random codex
    sigilTableHeader = np.random.choice(sigilValues, 9, False)
    sigilTableBody = np.random.choice(sigilLetters, (3, 9), False)

    # Nested list representation of the reference table
    refTable = []

    # Nested list of number values and letters
    for x in range(0, 9):
        nest = []
        nest.append(sigilTableHeader[x])
        nest.append(sigilTableBody[0][x])
        nest.append(sigilTableBody[1][x])
        nest.append(sigilTableBody[2][x])
        refTable.append(nest)

    # Store the sigil position of letters in a list
    refLst = []
    for letter in intent:
        refLst.append(find_in_heart_of_hearts(refTable, letter))

    # Get a list of the numbers linked to the letters
    numberLst = []
    for i in refLst:
        numberLst.append(refTable[i][0])

    # Display matrices
    print('\nRandomized Sigil Table:\n' \
          '=====================================\n' \
          '| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |\n' \
          '|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n' \
          '| {9} | {10} | {11} | {12} | {13} | {14} | {15} | {16} | {17} |\n' \
          '| {18} | {19} | {20} | {21} | {22} | {23} | {24} | {25} | {26} |\n' \
          '| {27} | {28} | {29} | {30} | {31} | {32} | {33} | {34} | {35} |\n' \
          '=====================================\n'.format(sigilTableHeader[0], sigilTableHeader[1],
                                                           sigilTableHeader[2], sigilTableHeader[3],
                                                           sigilTableHeader[4], sigilTableHeader[5],
                                                           sigilTableHeader[6], sigilTableHeader[7],
                                                           sigilTableHeader[8],
                                                           sigilTableBody[0][0], sigilTableBody[0][1],
                                                           sigilTableBody[0][2], sigilTableBody[0][3],
                                                           sigilTableBody[0][4], sigilTableBody[0][5],
                                                           sigilTableBody[0][6], sigilTableBody[0][7],
                                                           sigilTableBody[0][8],
                                                           sigilTableBody[1][0], sigilTableBody[1][1],
                                                           sigilTableBody[1][2], sigilTableBody[1][3],
                                                           sigilTableBody[1][4], sigilTableBody[1][5],
                                                           sigilTableBody[1][6], sigilTableBody[1][7],
                                                           sigilTableBody[1][8],
                                                           sigilTableBody[2][0], sigilTableBody[2][1],
                                                           sigilTableBody[2][2], sigilTableBody[2][3],
                                                           sigilTableBody[2][4], sigilTableBody[2][5],
                                                           sigilTableBody[2][6], sigilTableBody[2][7],
                                                           sigilTableBody[2][8], ))

    # Create a random sigil grid
    sigilGrid = np.random.choice(sigilValues, (3, 3), False)

    print('Randomized Sigil Grid:\n' \
          '=============\n' \
          '| {0} | {1} | {2} |\n' \
          '| {3} | {4} | {5} |\n' \
          '| {6} | {7} | {8} |\n' \
          '============='.format(sigilGrid[0][0], sigilGrid[0][1], sigilGrid[0][2], sigilGrid[1][0], sigilGrid[1][1],
                                 sigilGrid[1][2], sigilGrid[2][0], sigilGrid[2][1], sigilGrid[2][2]))

    print('\nNumber associated with letter:\n', numberLst, '\n')

    # List for tracking the order of numbers in the sigil grid
    gridNum = []
    gridNum.append(sigilGrid[0][0])
    gridNum.append(sigilGrid[0][1])
    gridNum.append(sigilGrid[0][2])
    gridNum.append(sigilGrid[1][0])
    gridNum.append(sigilGrid[1][1])
    gridNum.append(sigilGrid[1][2])
    gridNum.append(sigilGrid[2][0])
    gridNum.append(sigilGrid[2][1])
    gridNum.append(sigilGrid[2][2])

    # Get index location of number in the sigil grid
    sigilLocation = []
    for i in numberLst:
        sigilLocation.append(gridNum.index(i))

    xLst = []
    yLst = []

    for position in sigilLocation:
        if position == 0:
            xLst.append(1)
            yLst.append(3)
            # print("x,y = 1,3")
        elif position == 1:
            xLst.append(2)
            yLst.append(3)
            # print("x,y = 2,3")
        elif position == 2:
            xLst.append(3)
            yLst.append(3)
            # print("x,y = 3,3")
        elif position == 3:
            xLst.append(1)
            yLst.append(2)
            # print("x,y = 1,2")
        elif position == 4:
            xLst.append(2)
            yLst.append(2)
            # print("x,y = 2,2")
        elif position == 5:
            xLst.append(3)
            yLst.append(2)
            # print("x,y = 3,2")
        elif position == 6:
            xLst.append(1)
            yLst.append(1)
            # print("x,y = 1,1")
        elif position == 7:
            xLst.append(2)
            yLst.append(1)
            # print("x,y = 2,1")
        elif position == 8:
            xLst.append(3)
            yLst.append(1)
            # print("x,y = 3,1")
        else:
            print("Error: index out of range")

    # Define the endpoint marker symbol
    verts = [
        (0., 0.),  # Start, Center-Left
        (0., 80.),  # Left, top
        (20., 80.),  # Right, top
        (20., 0.),  # Center, Center-Right
        (20., -80.),  # Right, bottom
        (0., -80.),  # back to left, bottom
        (0., 0.),  # End, Center-Left
    ]

    codes = [
        Path.MOVETO,  # begin drawing
        Path.LINETO,  # straight line
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,  # close shape. This is not required for this shape but is "good form"
    ]

    # The new end point marker symbol
    path = Path(verts, codes)

    # Get the marker rotation angle
    rotate = markerRotation(xLst,yLst)

    # Define the custom marker symbol and the degrees of rotation
    m = MarkerStyle(path)
    m._transform.rotate_deg(rotate)

    # Define the size of the plot
    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.figure(figsize=(9, 9))

    # Add a circle outline
    circle1 = plt.Circle((2, 2), 2, color='r', fill=False)
    plt.gca().add_patch(circle1)

    # Draw the sigil lines with start point marker
    plt.plot(xLst, yLst, '-o', solid_capstyle="butt", solid_joinstyle="miter",
             color='red', linewidth=lineW, markevery=[0], markersize=markerW, zorder=1)

    # Add the rotated end marker symbol to plot
    plt.plot(xLst, yLst, marker=m, color='red', markevery=[-1], markersize=markerW*2.5)

    plt.margins(0.25)
    #plt.margins(0.50)
    #plt.margins(0.70)
    #plt.tight_layout()
    plt.axis('off')
    plt.savefig(output,
                bbox_inches='tight',
                transparent=True,
                pad_inches=0)

# Generate a Trolldom-style Sigil
def createTrolldomSigil(intent, output):
    # Create a reference table and a grid for the sigil, 13 points
    sigilValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Letters of the Alphabet to equal 26
    sigilLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Create a random codex
    sigilTableHeader = np.random.choice(sigilValues, 13, False)
    sigilTableBody = np.random.choice(sigilLetters, (2, 13), False)
    # print(sigilTableHeader)
    # print(sigilTableBody)

    # Nested list representation of the reference table
    refTable = []

    # Nested list of number values and letters
    for x in range(0, 13):
        nest = []
        nest.append(sigilTableHeader[x])
        nest.append(sigilTableBody[0][x])
        nest.append(sigilTableBody[1][x])
        refTable.append(nest)
    # print(refTable)

    # Store the sigil position of letters in a list
    refLst = []
    for letter in intent:
        refLst.append(find_in_heart_of_hearts(refTable, letter))

    # Get a list of the numbers linked to the letters
    numberLst = []
    for i in refLst:
        numberLst.append(refTable[i][0])

    # Display matrices
    print('\nRandomized Sigil Table:\n' \
          '=====================================\n' \
          '| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} | {10} | {11} | {12} |\n' \
          '|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n' \
          '| {13} | {14} | {15} | {16} | {17} | {18} | {19} | {20} | {21} | {22} | {23} | {24} | {25} |\n' \
          '| {26} | {27} | {28} | {29} | {30} | {31} | {32} | {33} | {34} | {35} | {36} | {37} | {38} |\n' \
          '=====================================\n'.format(sigilTableHeader[0], sigilTableHeader[1],
                                                           sigilTableHeader[2], sigilTableHeader[3],
                                                           sigilTableHeader[4], sigilTableHeader[5],
                                                           sigilTableHeader[6], sigilTableHeader[7],
                                                           sigilTableHeader[8], sigilTableHeader[9],
                                                           sigilTableHeader[10], sigilTableHeader[11],
                                                           sigilTableHeader[12],
                                                           sigilTableBody[0][0], sigilTableBody[0][1],
                                                           sigilTableBody[0][2], sigilTableBody[0][3],
                                                           sigilTableBody[0][4], sigilTableBody[0][5],
                                                           sigilTableBody[0][6], sigilTableBody[0][7],
                                                           sigilTableBody[0][8], sigilTableBody[0][9],
                                                           sigilTableBody[0][10], sigilTableBody[0][11],
                                                           sigilTableBody[0][12],
                                                           sigilTableBody[1][0], sigilTableBody[1][1],
                                                           sigilTableBody[1][2], sigilTableBody[1][3],
                                                           sigilTableBody[1][4], sigilTableBody[1][5],
                                                           sigilTableBody[1][6], sigilTableBody[1][7],
                                                           sigilTableBody[1][8], sigilTableBody[1][9],
                                                           sigilTableBody[1][10], sigilTableBody[1][11],
                                                           sigilTableBody[1][12]))

    # Create a random sigil grid
    sigilGrid = np.random.choice(sigilValues, (13,1), False)
    print(sigilGrid)

    print('Randomized Sigil Grid:\n' \
          '=============\n' \
          '| {0} | {1} | {2} |\n' \
          '| {3} | {4} | {5} |\n' \
          '| {6} | {7} | {8} |\n' \
          '| {9} | {10} | {11} |\n' \
          '|    | {12} |    |\n' \
          '============='.format(sigilGrid[0][0], sigilGrid[1][0], sigilGrid[2][0], sigilGrid[3][0], sigilGrid[4][0],
                                 sigilGrid[5][0], sigilGrid[6][0], sigilGrid[7][0], sigilGrid[8][0], sigilGrid[9][0],
                                 sigilGrid[10][0], sigilGrid[11][0], sigilGrid[12][0]))

    print('\nNumber associated with letter:\n', numberLst, '\n')

    # List for tracking the order of numbers in the sigil grid
    gridNum = []
    gridNum.append(sigilGrid[0][0])
    gridNum.append(sigilGrid[1][0])
    gridNum.append(sigilGrid[2][0])
    gridNum.append(sigilGrid[3][0])
    gridNum.append(sigilGrid[4][0])
    gridNum.append(sigilGrid[5][0])
    gridNum.append(sigilGrid[6][0])
    gridNum.append(sigilGrid[7][0])
    gridNum.append(sigilGrid[8][0])
    gridNum.append(sigilGrid[9][0])
    gridNum.append(sigilGrid[10][0])
    gridNum.append(sigilGrid[11][0])
    gridNum.append(sigilGrid[12][0])
    # print('Sigil Grid as a list:\n', gridNum)

    # Get index location of number in the sigil grid
    sigilLocation = []
    for i in numberLst:
        sigilLocation.append(gridNum.index(i))

    xLst = []
    yLst = []

    for position in sigilLocation:
        if position == 0:
            xLst.append(1)
            yLst.append(2)
            # print("x,y = 1,2")
        elif position == 1:
            xLst.append(0)
            yLst.append(1)
            # print("x,y = 0,1")
        elif position == 2:
            xLst.append(-1)
            yLst.append(2)
            # print("x,y = -1,2")
        elif position == 3:
            xLst.append(1)
            yLst.append(1)
            # print("x,y = 1,1")
        elif position == 4:
            xLst.append(0)
            yLst.append(0)
            # print("x,y = 0,0")
        elif position == 5:
            xLst.append(-1)
            yLst.append(1)
            # print("x,y = -1,1")
        elif position == 6:
            xLst.append(1)
            yLst.append(0)
            # print("x,y = 1,0")
        elif position == 7:
            xLst.append(0)
            yLst.append(-1)
            # print("x,y = 0,-1")
        elif position == 8:
            xLst.append(-1)
            yLst.append(0)
            # print("x,y = -1,0")
        elif position == 9:
            xLst.append(1)
            yLst.append(-1)
            # print("x,y = 1,-1")
        elif position == 10:
            xLst.append(-1)
            yLst.append(-1)
            # print("x,y = -1,-1")
        elif position == 11:
            xLst.append(1)
            yLst.append(-2)
            # print("x,y = 1,-2")
        elif position == 12:
            xLst.append(-1)
            yLst.append(-2)
            # print("x,y = -1,-2")
        else:
            print("Error: index out of range")

    # Tesla vortex coordinates
    x = [9, 13, 15, 14, 11, 7, 4, 3, 5]
    y = [15, 14, 10, 6, 3, 3, 6, 10, 14]

    # Define the endpoint marker symbol
    verts = [
        (0., 0.),  # Start, Center-Left
        (0., 80.),  # Left, top
        (20., 80.),  # Right, top
        (20., 0.),  # Center, Center-Right
        (20., -80.),  # Right, bottom
        (0., -80.),  # back to left, bottom
        (0., 0.),  # End, Center-Left
    ]

    codes = [
        Path.MOVETO,  # begin drawing
        Path.LINETO,  # straight line
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,  # close shape. This is not required for this shape but is "good form"
    ]

    # The new end point marker symbol
    path = Path(verts, codes)

    # Get the marker rotation angle
    rotate = markerRotation(xLst, yLst)

    # Define the custom marker symbol and the degrees of rotation
    m = MarkerStyle(path)
    m._transform.rotate_deg(rotate)

    # Define the size of the plot
    plt.rcParams.update({'figure.max_open_warning': 0})
    plt.figure(figsize=(9, 9))

    # Add a circle outline. 8 appears to be the best size for these sigils
    circle1 = plt.Circle((9, 9), 8, color='r', fill=False)
    plt.gca().add_patch(circle1)

    # Draw the sigil lines with start point marker
    plt.plot(xLst, yLst, '-o', solid_capstyle="butt", solid_joinstyle="miter",
             color='red', linewidth=lineW, markevery=[0], markersize=markerW, zorder=1)

    # Add the rotated end marker symbol to plot
    plt.plot(xLst, yLst, marker=m, color='red', markevery=[-1], markersize=markerW * 2.5)

    plt.margins(0.25)
    # plt.margins(0.50)
    # plt.margins(0.70)
    # plt.tight_layout()
    plt.axis('off')
    plt.savefig(output,
                bbox_inches='tight',
                transparent=True,
                pad_inches=0)


### Run Program ###

'''Obfuscate the Intent'''
# Prompt user input
intention = input("What is your intention? >>> ")
#intention = "my flies attract big trout"

# Prompt user input for sigil style 1, 2, or 3
sigilStyle = input("Choose sigil style:\n\t1 = Square Sigil\n\t2 = Nonagon Sigil\n\t3 = Trollrun Sigil\n\t4 = All\n>>>")

# Prompt user input for line width
lineW = input("Input sigil line width: >>>")
markerW = 2 * float(lineW)

# Prompt user for output directory
outPath = input("What is the sigil output location?: >>>")

# Capitalize the input
capIntention = intention.upper()

# Remove the vowels
vowels = ['A','E','I','O','U',' ']
for i in vowels:
    capIntention = capIntention.replace(i,'')

# Define a variable for the obfuscated intent
phrase = removeDuplicate(capIntention)
print("\nObfuscation:", phrase, "\n")

# Create a date time stamp for filename
now      = dt.now()
tdy      = now.strftime('%Y%m')

# Run functions to generate sigil
for i in range(len(phrase)):

    if sigilStyle == '1':
        # Name the output images
        outputImg = r'{0}\{1}_{2}_{3}'.format(outPath, phrase, tdy, i)

        # Call Square Sigil function
        createSquareSigil(phrase, outputImg)

    elif sigilStyle == '2':
        # Name the output images
        outputImg = r'{0}\{1}_{2}_{3}'.format(outPath, phrase, tdy, i)

        # Call the Tesla function
        createTeslaSigil(phrase,outputImg)

    elif sigilStyle == '3':
        # Name the output images
        outputImg = r'{0}\{1}_{2}_{3}'.format(outPath, phrase, tdy, i)

        # Call the Trollrun function
        createTrolldomSigil(phrase,outputImg)

    elif sigilStyle == '4':
        # Name the output images
        outputSqr = r'{0}\square_{1}_{2}_{3}'.format(outPath, phrase, tdy, i)

        # Call Square Sigil function
        createSquareSigil(phrase, outputSqr)

        # Name the output images
        outputNona = r'{0}\nonagon_{1}_{2}_{3}'.format(outPath, phrase, tdy, i)

        # Call the Tesla function
        createTeslaSigil(phrase, outputNona)

        # Name the output images
        outputNona = r'{0}\trollrun_{1}_{2}_{3}'.format(outPath, phrase, tdy, i)

        # Call the Tesla function
        createTrolldomSigil(phrase, outputNona)

    else:
        print('ERROR: User input out of range.')
