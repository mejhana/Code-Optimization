import numpy as np
import time 
a = np.random.rand(1000000)
b = np.random.rand(1000000)
c = np.dot(a,b)
d = np.cross(a,b)
print(c)

c=0
for i in range(1000000):
    c+= a[i]*b[i]

print(c)

d = 0
for i in range(1000000):
    d+= a[i]*b[i]

print(d)
