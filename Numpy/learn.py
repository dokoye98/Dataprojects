import numpy as np
import pandas as pd

a = np.array([[1,2,3,4,5,6,3,7],[5,6,7,4,5,7,8,3]])
#print(a[0,1:-1:6])
#print(a.shape)
a[1,:] = 5


b = np.array([[[2,3,2],[8,1,4]],[[12,4,4],[323,3,6]]])
#print( b[:,1,:])

b[:,1,:] = [[9,1,2],[1,3,5]]
#print(b)

arr = np.array([[23,43,53],[77,87,97],[54,34,24]])

#print(np.add(arr,np.array([[7],[3],[6]])))


arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

arr2 = np.array([10,11,12])

arr3 = arr1 + arr2

print(arr3.shape)