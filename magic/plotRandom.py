import matplotlib.pylplot as plt

edges = [(0,1), (2,3), (3,0), (2,1)]

x = [-5, 0, 5, 0]
y = [0, 5, 0, -5]

lx = []
ly = []
for edge in edges:
    lx.append(x[edge[0]])
    lx.append(x[edge[1]])
    ly.append(y[edge[0]])
    ly.append(y[edge[1]])

plt.figure()
plt.plot(x, y, 'ro')
plt.plot(lx, ly, '-', color='#000000')
plt.show()

