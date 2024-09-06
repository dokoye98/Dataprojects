import numpy as np
import pandas as pd

df = pd.DataFrame([["IND","Gold","Game1",9.9],
                   ["IND","silver","Game1",8],
                   ["IND","bronze","Game2",8],
                   ["USA","silver","Game1",9.5],
                   ["USA","Gold","Game2",8.6],],columns=["country","medal","game","score"],index=["Year 1", "Year 1","Year 2", "Year 1","year 2"]
                  )

#print(df.pivot(index="country",columns="medal"))
print(df.pivot_table(index="country",columns="medal",values="score",aggfunc=np.max))