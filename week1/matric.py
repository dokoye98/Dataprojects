import numpy as np

arr = np.array([25,56,12,85,34,75],dtype= int)
arr1 = [42,3,86,32,856,46]

Narr = np.array([27,564,0,852,341,7],dtype= int)

ar1 = np.ones(10)
ar2 = np.arange(10,dtype=np.float64)

ar3 = ar1 + ar2
print(np.result_type(ar1))
print(np.result_type(ar3))

ar = np.arange(4)
print (ar)
ar7 = ar.reshape(2,2)
print(ar7.shape)
ml = np.arange(4).reshape(4,-1)
print(ml.shape)