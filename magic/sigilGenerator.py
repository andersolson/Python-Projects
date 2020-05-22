# Random Sigil Grid Generator

import numpy as np

# Obfuscate Intent

intention = input("What is your intention?: ")

vowels = ['A','E','I','O','U',' ']

capIntention = intention.upper()

for i in vowels:
    capIntention = capIntention.replace(i,'')

def removeDuplicate(str):
    t = ""
    for i in str:
        if (i in t):
            pass
        else:
            t = t + i
    print("\nObfuscation:", t)

removeDuplicate(capIntention)


# Manifest Sigil

sigilValues = [1,2,3,4,5,6,7,8,9]

sigilLetters = ['A','B','C','D','E','F','G','H','I',
                'J','K','L','M','N','O','P','Q','R',
                'S','T','U','V','W','X','Y','Z','*']

sigilTableHeader = np.random.choice(sigilValues, 9, False)
sigilTableBody = np.random.choice(sigilLetters, (3,9), False)
sigilGrid = np.random.choice(sigilValues, (3,3), False)

print('\nRandomized Sigil Table:\n'\
      '=====================================\n'\
      '| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |\n'\
      '|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n'\
      '| {9} | {10} | {11} | {12} | {13} | {14} | {15} | {16} | {17} |\n'\
      '| {18} | {19} | {20} | {21} | {22} | {23} | {24} | {25} | {26} |\n'\
      '| {27} | {28} | {29} | {30} | {31} | {32} | {33} | {34} | {35} |\n'\
      '=====================================\n'.format(sigilTableHeader[0], sigilTableHeader[1], sigilTableHeader[2], sigilTableHeader[3], sigilTableHeader[4], sigilTableHeader[5], sigilTableHeader[6], sigilTableHeader[7], sigilTableHeader[8],
                                                       sigilTableBody[0][0], sigilTableBody[0][1], sigilTableBody[0][2], sigilTableBody[0][3], sigilTableBody[0][4], sigilTableBody[0][5], sigilTableBody[0][6], sigilTableBody[0][7], sigilTableBody[0][8],
                                                       sigilTableBody[1][0], sigilTableBody[1][1], sigilTableBody[1][2], sigilTableBody[1][3], sigilTableBody[1][4], sigilTableBody[1][5], sigilTableBody[1][6], sigilTableBody[1][7], sigilTableBody[1][8],
                                                       sigilTableBody[2][0], sigilTableBody[2][1], sigilTableBody[2][2], sigilTableBody[2][3], sigilTableBody[2][4], sigilTableBody[2][5], sigilTableBody[2][6], sigilTableBody[2][7], sigilTableBody[2][8],))

print('Randomized Sigil Grid:\n'\
      '=============\n'\
      '| {0} | {1} | {2} |\n'\
      '| {3} | {4} | {5} |\n'\
      '| {6} | {7} | {8} |\n'\
      '============='.format(sigilGrid[0][0], sigilGrid[0][1], sigilGrid[0][2], sigilGrid[1][0], sigilGrid[1][1], sigilGrid[1][2], sigilGrid[2][0], sigilGrid[2][1], sigilGrid[2][2]))

