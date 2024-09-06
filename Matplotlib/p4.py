import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

excelfile = "Book2.xlsx"
df = pd.read_excel(excelfile)
names = df.iloc[:,0]
totalpower = df.iloc[:,7]
catchrate = df.iloc[:,21] 

newdata = pd.DataFrame({"names":names,"totalpower":totalpower,"catch rate":catchrate})

fig, ax = plt.subplots()
p = ax.scatter(catchrate, totalpower, c = "r")
ax.grid()
ax.set_xlabel("catch rate")
ax.set_ylabel("Total power")
ax.set_title("pokemon")
plt.legend([p],["Pokemon"])
plt.show()