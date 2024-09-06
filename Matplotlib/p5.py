import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms

excelfile = "Book2.xlsx"
df = pd.read_excel(excelfile)

excelfile = "Book2.xlsx"
df = pd.read_excel(excelfile)
names = df.iloc[:,0]
totalpower = df.iloc[:,7]
catchrate = df.iloc[:,21] 
fig, ax = plt.subplots()
p = ax.scatter(catchrate, totalpower, c = "g")
ax.grid()
ax.set_xlabel("catch rate")
ax.set_ylabel("Total power")
ax.set_title("pokemon")

trans = transforms.blended_transform_factory(ax.transData,ax.transAxes)
rect = patches.Rectangle((44,0), width=2, height=5,transform = trans, color = "r", alpha= 0.4)
ax.add_patch(rect)
catchratelow = df[df.loc[:,"Catch"]==45]
lowpower = df[df.loc[:,"Total"] <=330]
print(lowpower.loc[:,"Mon"].head(20))
plt.legend([p],["Pokemon"])
#plt.show()