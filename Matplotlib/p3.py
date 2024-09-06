import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from scipy.stats import itemfreq

#HP	Atk	SpA	Def	SpD	Speed
excelfile = "Book2.xlsx"
df = pd.read_excel(excelfile)

df_pie = df[["Type1","Atk","SpA","Speed"]].copy() 
entries = df_pie.iloc[:,0]
unique = np.unique(entries)
print(unique)

