import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms
from mpl_toolkits.mplot3d import Axes3D

excelfile = "Book2.xlsx"
df = pd.read_excel(excelfile)

x,y,z = np.random.rand(3,50)

fig = plt.figure()
ax = fig.add_subplot(111, projection = "2d")

ax.scatter(x,y,z , color = "r" , marker= "o")

for angle in range(0,360):
    #ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)

ax.set_xlabel("x")
ax.set_ylabel("y")
#ax.set_zlabel("z")
plt.show()
