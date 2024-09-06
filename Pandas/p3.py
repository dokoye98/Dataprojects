import pandas as pd

df = pd.DataFrame([[15,12,90],
                   [33,54,11],
                   [10,32,1111]],index=list("ABC"),columns=list("EFG"))
lst = [15,22,5]

print(df.iloc[1:,:]) #iloc uses numerical identifiers

print("new")
print(df.loc[["C","A"],:])

df1 = pd.DataFrame([[15,12,90],
                   [33,54,11],
                   [10,32,1111]],index=("dwa","ani","nemi"),columns=("col1","col2","col3"))

print("regex")
print(df1.filter(regex="^d", axis=0)) #axis 1 = column name axis 0 = row name
#^ start of the word $ = end of the word

print("boolean")
print(df[df/12 >= 17])