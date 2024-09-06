import numpy as np
import re

text = "data science is cool"

import pandas as pd

area = pd.Series({"alaska":172337,"Texas":695662,"california":423967},name="area")
pop = pd.Series({"california":38332521,"Texas":26448193,"new york":19651127},name="pop")
print(pop/area)



arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2)
print(newarr)