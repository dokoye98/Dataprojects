import numpy as np
b = np.array([[[2,3,2],[8,1,4]],[[12,4,4],[323,3,6]]])
#print(np.zeros((2,3)))
#print(np.ones((4,2,2), dtype= int))
#print(np.full_like(b,4))
print(np.random.random_sample(b.shape))
print("new")
print(np.random.rand(4,2,6))

print(np.random.randint(4,7, size = (3,3))) #randint required or size wont work

print(np.identity(3))

arr = np.array([[1,2,3]])
re = np.repeat(arr,3,axis=0)


output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9
output[1:4,1:4] = z
print(output)
x = np.array([1,2,3,4])
y = x.copy() #copy function allows single change
y[0] = 23
#print(y,x)