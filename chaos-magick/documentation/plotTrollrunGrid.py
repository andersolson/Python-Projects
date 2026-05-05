import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [9, 9]
plt.rcParams["figure.autolayout"] = True

x = [1, 0, -1, 1, 0, -1, 1, 0, -1, 1, -1, 1, -1]
y = [2, 1, 2, 1, 0, 1, 0, -1, 0, -1, -1, -2, -2]

xCen = [p for p in x]
yCen = [p for p in y]
centroid = (sum(xCen) / len(x), sum(yCen) / len(y))
print(centroid)

plt.plot(x, y,'o')
plt.axis([-3, 3, -3, 3])

for i, j in zip(x, y):
   plt.text(i, j+0.5, '({}, {})'.format(i, j))

plt.show()