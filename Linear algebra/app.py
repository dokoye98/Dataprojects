import numpy as np


num  =50
mass = 1.989e30
len = 21196

arr = np.zeros(6).reshape(3,2)
df = np.array([3,3])

print(arr)
print(np.transpose(arr)) #transpose switches matrix shape eg 2,3 to 3,2
dai = np.diag((1,4,6,7,78,3))
dia = np.diag(np.arange(1,9,3))


mn = np.identity(9)

xm = np.eye(4)
a = np.array([[1,2,3],[3,4,5],[5,63,5]])

tr = a.transpose()

compare = (a ==tr)
equal = compare.all()
print(a)
print(tr)