import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

excelfile = "Book2.xlsx"
df = pd.read_excel(excelfile)

bulbasaur = df.iloc[0,1:8]
charmander = df.iloc[4,1:8]
squirtle = df.iloc[7,1:8]

mons = [bulbasaur, charmander,squirtle]

bulweigh = df.iloc[0,13]
charweigh = df.iloc[4,13]
squwiegh = df.iloc[7,13]

weights  = [bulweigh, charweigh,squwiegh]

fig = plt.figure(0)
ax1 = plt.subplot2grid((4,3),(0,0),colspan = 3)

ax1.plot(bulbasaur,"g-",bulbasaur, "go")
ax1.plot(charmander,"r-",charmander, "ro")
ax1.plot(squirtle,"b-",squirtle, "bo")
ax1.set_xlim(-0.3,6.3)

ax2 = plt.subplot2grid((4,3),(1,0),colspan = 1)
ax3 = plt.subplot2grid((4,3),(2,0),colspan = 1)
ax4 = plt.subplot2grid((4,3),(3,0),colspan = 1)
ax = [ax2,ax3,ax4]
color = ["r","g","b"]
for i in range(0,3):
    bp = ax[i].boxplot(mons[i][1:], patch_artist=True)

ax2.annotate("median", xy = (1.09,49), xytext=(1.2,60), arrowprops=dict(facecolor = "wheat", shrink = 0.001))
ax3.annotate("median", xy = (1.09,64.5), xytext=(1.2,74), arrowprops=dict(facecolor = "wheat", shrink = 0.001))
ax4.annotate("median", xy = (1.09,64), xytext=(1.2,74), arrowprops=dict(facecolor = "wheat", shrink = 0.001))


plt.show()