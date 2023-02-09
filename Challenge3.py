import functools
import matplotlib.pyplot as plt
import numpy as np
import random
#Comparator
def compare(item1, item2):
    if item1[1] > item2[1] or (item1[1] == item2[1] and item1[2] > item2[2]):
        return 1
    elif item1[1] < item2[1] or (item1[1] == item2[1] and item1[2] < item2[2]):
        return -1
    else:
        return 0
#Compute Skyline
def getWindow(dataSet):
    # dataSet = [id, x, y]
    dataSet = sorted(dataSet, key=functools.cmp_to_key(compare)) # O(n*log(n))
    minY = dataSet[0][2]
    ret = []
    ret.append(dataSet[0]) #Amortized O(1)
    for i in range(1, len(dataSet)): #O(n)
        if dataSet[i][2] < minY:
            minY = dataSet[i][2]
            ret.append(dataSet[i]) #Amortized O(1)
    return ret

#dataSet = [["Novotel", 0.15, 0.1],["Crillon", 0.25, 0.1],["Ibis", 0.08, 0.3],["Sheraton", 0.2, 0.2],["Hilton", 0.175, 0.3]]
#print(getWindow(dataSet))

N = random.randint(100, 1000)
dataSet = []
#Generates random points
for i in range(0, N):
	dataSet.append([i, random.randint(0, 5000), random.randint(0, 5000)])
window = getWindow(dataSet)
print(window)
x = []
y = []
for el in dataSet:
	x.append(el[1])
	y.append(el[2])
plt.scatter(np.array(x), np.array(y))	
x = []
y = []
for el in window:
	x.append(el[1])
	y.append(el[2])
plt.plot(np.array(x), np.array(y), color = 'r', linestyle = '--')
plt.show()
