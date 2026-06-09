
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

