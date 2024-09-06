import numpy as np

sx = np.array([[2,5,6,5],[4,6,4,6]])

arr = np.array([[4,6,1,3],[9,7,5,6]])

arr2 = np.ones((2,4)) *4

#print(np.less(arr **sx, arr2**sx))

arr3 = np.cumsum(arr, axis=1)
arr4 = np.cumsum(sx,axis=1)
print(arr3)
print(arr3 > arr4)
print(np.mean((sx),axis=0))