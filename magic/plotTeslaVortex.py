import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [9, 9]
plt.rcParams["figure.autolayout"] = True

x = [9, 13, 15, 14, 11, 7, 4, 3, 5]
y = [15, 14, 10, 6, 3, 3, 6, 10, 14]

plt.plot(x, y,'o')
plt.axis([0, 18, 0, 18])

for i, j in zip(x, y):
   plt.text(i, j+0.5, '({}, {})'.format(i, j))

plt.show()