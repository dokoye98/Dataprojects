import numpy as np
import pandas as pd

multi = pd.MultiIndex.from_tuples([("IND","GAME1"),
                                   ("IND","GAME2"),
                                   ("IND","GAME3"),
                                   ("IND","GAME4"),
                                   ("AME","GAME1"),
                                   ("AME","GAME2"),
                                   ("AME","GAME3"),
                                   ("AME","GAME4"),
                                   ],names=["country","game"])
df = pd.DataFrame(np.random.randn(8,2),index = multi,columns=["Year","Year2"])

print(df.stack())
print(df.unstack())