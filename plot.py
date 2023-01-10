data = [8, 19, 31, 41, 50, 52, 60]
prediction = 68

from matplotlib import pyplot

pyplot.plot(data + [prediction], color='tab:red')
pyplot.plot(data, color='tab:blue')
pyplot.show()
