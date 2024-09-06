import pandas as pd

df = pd.DataFrame([[11,202],
                   [33,44]], index=list("AB"),columns=list("PQ"))

df.to_excel("test_file.xlsx", sheet_name="Sheet1")

print(pd.read_excel("test_file.xlsx", "Sheet1"))