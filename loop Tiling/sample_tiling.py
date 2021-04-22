import numpy as np
A = np.random.randint(1000, size=(1000, 1000))
B = np.random.randint(1000, size=(1000, 1000))
C = np.random.randint(1000, size=(1000, 1000))

# A = [[12, 72, 53],
#     [84, 52, 69 ],
#     [71, 18, 79]]

# B = [[50, 86, 11],
#     [62, 87, 33],
#     [44, 50, 95]]

    
# result = [[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]]

x = len(A)
y = len(B)
z = 3


result = np.zeros([1000,1000])

for i in range(0,x):
    for j in range(0,y):
        for k in range(0,z):
            result[i][j] += A[i][k] * B[k][j]
print(result)
