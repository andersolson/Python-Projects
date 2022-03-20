import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x = [3, 1, 2, 5]
y = [5, 2, 4, 7]

plt.plot(x, y, 'r*')
plt.axis([0, 6, 0, 20])

for i, j in zip(x, y):
   plt.text(i, j+0.5, '({}, {})'.format(i, j))

plt.show()