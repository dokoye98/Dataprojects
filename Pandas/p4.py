import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


size = np.array([[1,693],[1,656],[1,1060],[1,487],[1,1275]])
print(size.shape)

values = np.array([[10190],[223]])
#print(size.dot(values))# 1 *10190 + 693*223

print(np.matmul(size,values))
