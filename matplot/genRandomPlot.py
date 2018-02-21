from matplotlib import pyplot as plt # for plotting
from random import randint # for sorting and creating data pts
from math import atan2 # for computing polar angle

# Returns a list of (x,y) coordinates of length 'num_points',
# each x and y coordinate is chosen randomly from the range 
# 'min' up to 'max'.
def create_points(ct,min=0,max=50):
    return [[randint(min,max),randint(min,max)] for _ in range(ct)]

#print(create_points(5)) #test create_points function with 5 random generated points: [[45, 37], [40, 7], [45, 5], [29, 1], [10, 9]]

# Creates a scatter plot, input is a list of (x,y) coordinates.
# The second input 'convex_hull' is another list of (x,y) coordinates
# consisting of those points in 'coords' which make up the convex hull,
# if not None, the elements of this list will be used to draw the outer
# boundary (the convex hull surrounding the data points).
def scatter_plot(coords,convex_hull=None):
    xs,ys=zip(*coords) # unzip into x and y coord lists
    plt.scatter(xs,ys) # plot the data points

    if convex_hull!=None: #If the hull does not equal None, then ...
        # plot the convex hull boundary, extra iteration at
        # the end so that the bounding line wraps around
        for i in range(1,len(convex_hull)+1):
            if i==len(convex_hull): i=0 # wrap
            c0=convex_hull[i-1]
            c1=convex_hull[i]
            plt.plot((c0[0],c1[0]),(c0[1],c1[1]),'r')
    plt.show()

scatter_plot(create_points(10)) #test the functions and display the scatter plot

somePoints = [[4,5],[20,3],[12,80],[30,180]]

scatter_plot(somePoints) #test the function and display a known list of points on scatter plot