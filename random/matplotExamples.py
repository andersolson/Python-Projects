import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#x_coords = [1, 2, 3, 7]
#y_coords = [4, 5, 6, 9]

#plt.scatter(x_coords, y_coords)
#plt.show()

# 3 x 3 grid
#x_grid = [1, 2, 3, 1, 2, 3, 1, 2, 3]
#y_grid = [1, 1, 1, 2, 2, 2, 3, 3, 3]

#plt.scatter(x_grid, y_grid)
#plt.show()

# 3 x 3 plot scatter graph
#x_grid = [1, 2, 3, 1, 2, 3, 1, 2, 3]
#y_grid = [1, 1, 1, 2, 2, 2, 3, 3, 3]

#plt.scatter(x_grid, y_grid)
#plt.plot(x_grid, y_grid)
#plt.show()

# 3 x 3 random plot scatter graph
import random

def genVal(inLst):
    for i in range(0,9):
        n = random.randint(1,3)
        inLst.append(n)
    return(inLst)

xLst = []
yLst = []
genVal(xLst)
genVal(yLst)

print(xLst)
print(yLst)

# Set figure size to be a square
figure(figsize=(6,6),dpi=80)

# Show values on grid with lines connecting points
plt.scatter(xLst, yLst)
plt.plot(xLst, yLst)
#plt.show()
plt.savefig(r'C:\Users\andolson\Documents\WORKING\TEMP\tmp3.png')
