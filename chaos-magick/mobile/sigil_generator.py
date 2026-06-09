
# --- Module Header and Imports (Appended Step 1) ---
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
from matplotlib.path import Path
from datetime import datetime as dt

# --- Helper Functions ---
def removeDuplicate(s):
    t = ''
    for i in s:
        if i not in t:
            t += i
    return t

def find_in_heart_of_hearts(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            return mylist.index(sub_list)
    return None

def markerRotation(xLST, yLST):
    if len(xLST) < 2 or len(yLST) < 2:
        return 0
    startX = xLST[-2]
    endX = xLST[-1]
    startY = yLST[-2]
    endY = yLST[-1]
    radians = math.atan2(endY - startY, endX - startX)
    degrees = math.degrees(radians)
    return degrees


# --- Square Sigil Plotting Function (Appended Step 2) ---
def createSquareSigil(intent, line_width, output_path):
    marker_width = line_width * 2
    sigilValues = [1,2,3,4,5,6,7,8,9]
    sigilLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','*']
    sigilTableHeader = np.random.choice(sigilValues, 9, False)
    sigilTableBody = np.random.choice(sigilLetters, (3,9), False)
    refTable = []
    for x in range(0,9):
        nest = [sigilTableHeader[x], sigilTableBody[0][x], sigilTableBody[1][x], sigilTableBody[2][x]]
        refTable.append(nest)
    refLst = []
    for letter in intent:
        refLst.append(find_in_heart_of_hearts(refTable, letter))
    numberLst = []
    for i in refLst:
        numberLst.append(refTable[i][0])
    sigilGrid = np.random.choice(sigilValues, (3,3), False)
    gridNum = [sigilGrid[0][0], sigilGrid[0][1], sigilGrid[0][2], sigilGrid[1][0], sigilGrid[1][1], sigilGrid[1][2], sigilGrid[2][0], sigilGrid[2][1], sigilGrid[2][2]]
    sigilLocation = []
    for i in numberLst:
        sigilLocation.append(gridNum.index(i))
    xLst = []
    yLst = []
    for position in sigilLocation:
        if position == 0: xLst.append(1); yLst.append(3)
        elif position == 1: xLst.append(2); yLst.append(3)
        elif position == 2: xLst.append(3); yLst.append(3)
        elif position == 3: xLst.append(1); yLst.append(2)
        elif position == 4: xLst.append(2); yLst.append(2)
        elif position == 5: xLst.append(3); yLst.append(2)
        elif position == 6: xLst.append(1); yLst.append(1)
        elif position == 7: xLst.append(2); yLst.append(1)
        elif position == 8: xLst.append(3); yLst.append(1)
    verts = [(0.,0.), (0.,80.), (20.,80.), (20.,0.), (20.,-80.), (0.,-80.), (0.,0.)]
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
    path = Path(verts, codes)
    rotate = markerRotation(xLst, yLst)
    m = MarkerStyle(path)
    m._transform.rotate_deg(rotate)
    plt.rcParams.update({'figure.max_open_warning':0})
    plt.figure(figsize=(9,9))
    circle1 = plt.Circle((2,2), 2, color='r', fill=False)
    plt.gca().add_patch(circle1)
    plt.plot(xLst, yLst, '-o', solid_capstyle='butt', solid_joinstyle='miter', color='red', linewidth=line_width, markevery=[0], markersize=marker_width, zorder=1)
    plt.plot(xLst, yLst, marker=m, color='red', markevery=[-1], markersize=marker_width*2.5)
    plt.margins(0.25)
    plt.axis('off')
    plt.savefig(output_path, bbox_inches='tight', transparent=True, pad_inches=0)
    plt.close()

