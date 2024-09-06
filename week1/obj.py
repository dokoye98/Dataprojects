import numpy as np

arr = np.array([1,2,3,5,6] , dtype=int)
print(arr)
print(type(arr))
print(np.result_type(arr))

print(np.arange(0,10,1.33, dtype=np.float64))

print(np.linspace(0,156,6, dtype=np.float64))

print(np.array([5,6,8,45,12,52,23,46,44]).reshape(3,3)) #splits array the number of ((,this one) and the number of values in (this one,)
print()
arr1 = np.matrix([[12,34],[3,5]])
print(arr1)
print()
print(np.eye(3))
print(np.zeros((5,5),dtype=int))
print("vector of 1")
print(np.ones((3,3) , dtype= np.float64))