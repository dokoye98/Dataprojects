import pandas as pd

df = pd.DataFrame([[10*.23j,"f1","hello"],[100*5.36j,"f2",2**8],[100* 12.45j,"f3",True]],
                  index=list("PQx"),columns=list("ABc"))
print((df))


lst = ["f50", "f40","f1","f33"]
for i in lst:
    x = lst[i]
    print(df[:,1] ==x)