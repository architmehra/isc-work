import numpy as np 
x = range(1,11)
a1 = np.array(x, np.int32)
a2 = np.array(x, np.float32)

print a1.dtype
print a2.dtype

arr = np.zeros((2,3,4))
arr = np.ones((2,3,4))
arr = np.arange(1000)

a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
print a[1]
print a[1:4]

a = np.array ([[2, 3.2, 5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]])

print a[:, 3]
print a[1:4, 0:4]
print a[1:, 2]

arr = np.array([range(4), range(10,14)])

print arr.shape

print arr.size 

print arr.max()

print arr.min()

print np.reshape(arr,(2,2,2))

print np.transpose(arr) 

print np.ravel(arr)

print arr.astype(np.float64)

