import numpy as np
a = np.arange(15).reshape(3,5)
print(a)
print(type(a))
print(a.shape)
print(a.ndim)
print(a.itemsize)
print(a.size)
b = np.array([6,7,8])
print(b)
for i in b :
    print(i+2)
    print(type(i))
