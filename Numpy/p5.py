import numpy as np

mat1 = np.matrix([[111,1322],[785,554]])
arr = np.array([10,6,5,7]).reshape(2,-1)
arr3 = np.random.randint(8, size=(3,3))
print(arr3)
arr1 = np.arange(9, dtype= "float").reshape(3,3)
in1 = np.array([[1,2],[0,1]])
in2 = np.array([[0,2],[1,2]])
print(arr1)
print(arr1[in1, in2].sum())
#print(arr.sum(axis= 0))

#print(mat1.sum(axis=0))