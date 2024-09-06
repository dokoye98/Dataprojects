import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr = np.arange(1,6)
bar_width = 0.2
men_sc = [20,30,10,50,90]
err_men_sc = [2,3,4,5,4]
women_sc = [10,123,19,60,40]
err_women_sc= [1,6,2,8,7]
sets = ["A","B","C","D","E"]

plt.bar(arr,men_sc,bar_width,alpha = 0.6,color = 
        "g",label = "men")
plt.bar(arr+bar_width,women_sc,bar_width,alpha = 0.6,color = 
        "r",label = "women")
plt.bar(arr+(bar_width*2),err_women_sc,bar_width,alpha = 0.6,color = 
        "y",label = "error women")
plt.bar(arr-(bar_width),err_men_sc,bar_width,alpha = 0.6,color = 
        "y",label = "error men")
plt.legend(loc = "best")
plt.xticks(arr,sets)
plt.show()