import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms


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

textx = [0.045,.19,0.34,0.49,0.795,0.945]
testy = [0.7,0.57,0.65,0.75,0.75,0.75,0.72]
rot = [0,45,45,45,45,45,45]
txt=[r'$T_{OTAL}$', r"$HP$",r"$A_{TTACK}$",r"$D_{EFFENCE}$",r"$S_{P}\_A_{TK}$",r"$S_{P}\_D_{EF}$",r"$S_{PEED}$"]
#trans = transforms.blended_transform_factory(ax1.transData,ax1.transAxes)
for i in range(0,6):
    ax1.text(textx[i], testy[i],txt[i], 
             va = "top",
             rotation = rot[i],
             bbox = dict(boxstyle = "round", facecolor = "wheat", alpha = 0.5))


plt.show()
#print(bulbasaur)