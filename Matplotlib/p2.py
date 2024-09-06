import random 
import numpy as np
import matplotlib.pyplot as plt

clr = np.linspace(0,1,18)
random.shuffle(clr)
color = []

for i in range(0,72,4):
    idx = np.arange(0,18,1)
    random.shuffle(idx)
    r = clr[idx[0]]
    g = clr[idx[1]]
    b = clr[idx[2]]
    a = clr[idx[3]]
    color.append([r,g,b,a])

arr = np.arange(1,6)
bar_width = 0.2
men_sc = [20,30,10,50,90]
err_men_sc = [2,3,4,5,4]
women_sc = [10,123,19,60,40]
err_women_sc= [1,6,2,8,7]
sets = ["A","B","C","D","E"]

bargraph=plt.bar(arr,men_sc,bar_width,alpha = 0.5,color = 
        color,label = "men")
plt.legend(bargraph,sets )
plt.xticks(arr,sets)
plt.show()