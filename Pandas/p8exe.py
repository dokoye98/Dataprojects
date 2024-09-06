import numpy as np
import pandas as pd

sys = ["s1","s1","s1","s1",
       "s2","s2","s2","s2"]
net_day = ["d1","d1","d2","d2",
           "d1","d1","d2","d2"]
spd = [1.3,11.4,5.6,12.3,6.2,1.1,20.0,8.8]

df = pd.DataFrame({"set_name":sys,"spd_per_day":net_day,"speed":spd})

new_df = pd.DataFrame(df.groupby(["spd_per_day","set_name"])["speed"].median())

print(new_df.sort_values("speed"))
print(new_df.head(1))