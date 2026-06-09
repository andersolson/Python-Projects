# --- Module Header and Imports  ---
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
from matplotlib.path import Path
from datetime import datetime as dt
import os
from datetime import datetime as dt

# --- Helper Functions ---
def removeDuplicate(s):
    t = ""
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

# Main function
def generate_sigil(intent_text, style, line_width, output_dir):
    # Clean input
    intention = intent_text.upper()
    vowels = ['A','E','I','O','U',' ']
    for i in vowels:
        intention = intention.replace(i,'')
    phrase = removeDuplicate(intention)

    # Build filename
    now = dt.now()
    tdy = now.strftime('%Y%m')
    filename = f"{phrase}_{tdy}.png"
    output_path = os.path.join(output_dir, filename)

    # Placeholder for actual sigil generation based on style
    with open(output_path, 'w') as f:
        f.write("Sigil placeholder. Replace with Matplotlib generated image.")

    return output_path

