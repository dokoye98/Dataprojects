import numpy as np
mat = np.arange(4).reshape(2,2)
mat1 = np.arange((4)*2).reshape(2,4)
mat2 = np.arange((4)*3).reshape(2,6)

a = np.array([[3,1],[1,2]])
b = np.array([9,8])
print(np.linalg.det(a))

print(np.linalg.solve(a,b))
arr = np.ones((6,6)).reshape(6,6)
arr1 =np.zeros((2,2))
arr[2:4,2:4] = arr1

a = np.arange(12).reshape(3,4)
b = np.ceil(np.linspace(7,15,9)).reshape(3,-1)
#print(np.count_nonzero(np.greater_equal(a,b)))
#print(np.floor(np.linspace(0,5,5)))

print(b)

c = np.copy(a)
print(c)
print(np.hsplit(c,4))
print(np.vsplit(a,3))
d = np.split(a,3)

e = np.hstack(d)
print(e)
