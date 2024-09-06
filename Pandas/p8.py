import numpy as np
import pandas as pd


df = pd.DataFrame([["Laptop", 1200],
                   ["Laptop", 1600],
                   ["Laptop", 1100],
                   ["Computer", 1777],
                   ["Computer", 117],
                   ["Computer", 117],
                   ["Computer", 828],
                   ["PS5",750],
                   ["Xbox", 350]],columns=["Gadget", "price"])

print(df.groupby(["Gadget"], sort=False).sum())
print(df)