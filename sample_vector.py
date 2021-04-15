import numpy as np

a = np.random.rand(1000000)
b = np.random.rand(1000000)

for i in range(0,1000000):
	c = c + a[i]*b[i]

#dot and cross! 