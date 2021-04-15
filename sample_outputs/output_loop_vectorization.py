import numpy as np

# dot
vector_a = np.random.rand(3)
vector_b = np.random.rand(3)
product = np.dot(vector_a, vector_b)
print("Dot Product : \n", product)

# cross
x = np.random.rand(3)
y = np.random.rand(3)
result = np.cross(x, y)
print("Cross Product : \n ",result)
