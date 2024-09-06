import numpy as np

mat = np.array([[10,5,9],[2,20,6],[8,3,30]]).reshape(3,3)
#print(mat)

n1 = mat[0,:].max()
n2 = mat[1,:].max()
n3 = mat[2,:].max()
print(n1 + n2 + n3)

arr = np.cumsum((mat),axis= 1)
np.tri

print(arr)