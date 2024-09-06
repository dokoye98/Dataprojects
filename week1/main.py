import matplotlib.pyplot as plt
import numpy as np

x = [24,25,26]
y = [23,24,25]
lst = [123,True,"hello world", 9*10]
arrr = np.array(x)
print (arrr.nbytes)
net = np.array(lst)
print(type(net[0]), type(net[1]), type(net[3]),net[2])

plt.plot(x,y)
plt.show()
