import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)


ftails = []
counter =0
for i in range(10000):
    tails=[0]
    for i in range(10):
        
        coins = np.random.randint(0,2)
        tails.append(tails[i]  + coins)
    ftails.append(tails[-1])
print(ftails)        
        
plt.hist(ftails, bins=10)

plt.show()