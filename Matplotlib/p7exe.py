import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0.0, 5.0, 0.1)
y = np.cos(2 * np.pi * x*1) * np.exp(-x)

plt.plot(x,y, color = "r")

fig = plt.figure(0)
ax1 = plt.subplot2grid((4,3),(0,0),colspan = 3)
ax1.set_xlim(-0.3,6.3)
plt.show()