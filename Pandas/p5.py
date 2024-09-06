import pandas as pd
import numpy as np

data = pd.DataFrame([[15,12,90],
                   [33,54,11],
                   [10,32,1111]],columns=("A","B","C"))

data1 = pd.DataFrame([[15,12,90],
                   [33,54,11],
                   [10,32,1111]],columns=("E","F","G"))

#print(pd.concat([data,data1], axis=1))

data2 = pd.DataFrame(np.random.randint(9,size=(3,3)),columns=list("ABC"))
arr = pd.DataFrame(np.ceil(np.linspace(7,15,9)).reshape(3,-1),columns=list("DEF"))
data3 = pd.DataFrame(np.arange(36).reshape(6,6),columns=list("ABCDEF"))

#print(pd.concat([data2,data3], axis=1))
#print(arr)
mer = pd.concat([data2,arr],axis=1)
#print(mer)
print(pd.concat([mer,data3],axis=0))
