import pandas as pd

lst = [{"c1":23,"c2":45},{"c1":32,"c2":33,"c3":44}]
print(pd.DataFrame(lst,index=["R1","R2"]))

dc = {"c1":["1","3"],
      "c2":["2","4"]}

print(pd.DataFrame(dc,index=["R1","R2"]))
print(pd.DataFrame(dc["c1"],index=["R1","R2"]))


arr = [[54,42],[22,531]]
print(pd.DataFrame(arr,index=list("pq"),columns=list("ab")))

a = [{"A":[2*2j,23,0.2],
      "B":["hello","world"]}]
print()