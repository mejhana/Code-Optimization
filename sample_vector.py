import numpy as np

# dot
vector_a = np.array([[1, 4], [5, 6]])
vector_b = np.array([[2, 4], [5, 2]])
product = np.dot(vector_a, vector_b)
print("Dot Product : \n", product)

# cross
x = [[1, 2], [3, 4]]
y = [[5, 6], [7, 8]]
result = np.cross(x, y)
print("Cross Product : \n ",result)