import matplotlib.pyplot as plt
import numpy as np

# Prompt user input
intention = "I need to go beer"

# Capitalize the input
capIntention = intention.upper()

# Remove the vowels
vowels = ['A','E','I','O','U',' ']
for i in vowels:
    capIntention = capIntention.replace(i,'')

# Obfuscate the Intent
def removeDuplicate(str):
    t = ""
    for i in str:
        if (i in t):
            pass
        else:
            t = t + i
    return t

# Define a variable for the obfuscated intent
phrase = removeDuplicate(capIntention)
print("\nObfuscation:", phrase, "\n")

# Create a reference table and a grid for the sigil
sigilValues = [1,2,3,4,5,6,7,8,9]

sigilLetters = ['A','B','C','D','E','F','G','H','I',
                'J','K','L','M','N','O','P','Q','R',
                'S','T','U','V','W','X','Y','Z','*']

# Create a random codex
sigilTableHeader = np.random.choice(sigilValues, 9, False)
sigilTableBody = np.random.choice(sigilLetters, (3,9), False)

#print(sigilTableHeader)
#print(sigilTableBody)

# Nested list representation of the reference table
refTable = []

# Nested list of number values and letters
for x in range(0,9):
    nest = []
    nest.append(sigilTableHeader[x])
    nest.append(sigilTableBody[0][x])
    nest.append(sigilTableBody[1][x])
    nest.append(sigilTableBody[2][x])
    refTable.append(nest)

print('Reference table as list:\n',refTable,"\n")
#print('\n{0}\n'.format(codex))

# Define a function for locating letter position in the reference table
def find_in_heart_of_hearts(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            #print(mylist.index(sub_list), sub_list.index(char))
            #print(mylist.index(sub_list))
            return (mylist.index(sub_list))

# Store the sigil position of letters in a list
refLst = []
for letter in phrase:
    refLst.append(find_in_heart_of_hearts(refTable,letter))
print('Letter position in reference table:\n',refLst,'\n')

# Get a list of the numbers linked to the letters
numberLst =[]
for i in refLst:
    #print(refTable[i][0])
    numberLst.append(refTable[i][0])
print('Number associated with letter:\n',numberLst,'\n')

# Display matrices
print('Randomized Sigil Table:\n'\
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

# Create a random sigil grid
sigilGrid = np.random.choice(sigilValues, (3,3), False)

print('Randomized Sigil Grid:\n'\
      '=============\n'\
      '| {0} | {1} | {2} |\n'\
      '| {3} | {4} | {5} |\n'\
      '| {6} | {7} | {8} |\n'\
      '============='.format(sigilGrid[0][0], sigilGrid[0][1], sigilGrid[0][2], sigilGrid[1][0], sigilGrid[1][1], sigilGrid[1][2], sigilGrid[2][0], sigilGrid[2][1], sigilGrid[2][2]))

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
print('Sigil Grid as a list:\n', gridNum)

# Get index location of number in the sigil grid
for i in numberLst:
    print(i)


'''
xLst = []
yLst = []

for i in refLst:
    position = i
    print(i)
    if position == 0:
        xLst.append(1)
        yLst.append(3)
        print("x,y = 1,3")
    elif position == 1:
        xLst.append(2)
        yLst.append(3)
        print("x,y = 2,3")
    elif position == 2:
        xLst.append(3)
        yLst.append(3)
        print("x,y = 3,3")
    elif position == 3:
        xLst.append(1)
        yLst.append(2)
        print("x,y = 1,2")
    elif position == 4:
        xLst.append(2)
        yLst.append(2)
        print("x,y = 2,2")
    elif position == 5:
        xLst.append(3)
        yLst.append(2)
        print("x,y = 3,2")
    elif position == 6:
        xLst.append(1)
        yLst.append(1)
        print("x,y = 1,1")
    elif position == 7:
        xLst.append(2)
        yLst.append(1)
        print("x,y = 2,1")
    elif position == 8:
        xLst.append(3)
        yLst.append(1)
        print("x,y = 3,1")
    else:
        print("Error: index out of range")

print(xLst, yLst)

plt.plot(xLst, yLst, 'o', color='black')

plt.plot(xLst, yLst, '-ok')
plt.show()
'''