import numpy as np 


d1 = np.array([[1,2,3],[9,-1,-4]])
d2 = np.array([[5,31,2], [0,2,4]])

#print(d2+d1)

a = np.add(d1, d2)
#print(a)

m = np.array([1,2,4])
n = np.array([6,44,1])


mn = np.inner(m,n)
#print(mn)


p1 = np.array([[3],[-1],[2]])
p2 = np.array([[2],[4],[-1]])
p3 = np.array([[3],[5]])
p4 = np.array([[-5],[3]])
v1 = p1.transpose()
v2 = p2.transpose()
v3 = p3.transpose()
print(np.dot(v2,p1))

print(np.dot(v3,p4))

def angle(vec1, vec2):
    dotp1 = vec1.dot(vec2)
    norms  = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    
    return np.rad2deg(np.arccos(dotp1 / norms))


vec1 = np.array([1,0,0])
vec2 = np.array([0,0,1])

print(angle(vec1 , vec2))