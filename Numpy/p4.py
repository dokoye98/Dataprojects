import numpy as np

mat = np.array([[10,5,9],[2,20,6],[8,3,30]]).reshape(3,3)
#print(mat)
mt1 = np.cumsum(mat,axis=1)
print(mt1)
n1 = mt1.diagonal()
n4 = np.cumsum(n1,axis=0)
n2 = mat.max()
n3 = mat[2,:].max()
#x = n1 + n2 + n3
print(n4)
#arr = np.zeros((x), dtype=int)
#print(arr)