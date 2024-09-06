import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import random



excelfile = "Book2.xlsx"
df = pd.read_excel(excelfile)
entries = df.iloc[:,1]
unique = np.unique(entries)
#print(len(unique))
unicount = len(unique)
pokemonnames  = df.iloc[:,0]
entrycount = len(entries)
doubletype = df.iloc[:,1].notna()
dcount = len(doubletype)
#print(dcount)
type1 = np.arange(unicount)
bar_width = 0.5

clr = np.linspace(0,1,18)
random.shuffle(clr)
choice = []

for i in range(0,72,4):
    idx = np.arange(0,18,1)
    random.shuffle(idx)
    r = clr[idx[0]]
    g = clr[idx[1]]
    b = clr[idx[2]]
    a = clr[idx[3]]
    choice.append([r,g,b,a])
plt.bar(type1, unicount,bar_width,alpha = 0.1,color = choice,label = unique)
plt.legend(loc = "best")
plt.xticks(type1 + bar_width/2,unique)
plt.show()

