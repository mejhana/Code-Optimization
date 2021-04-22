import numpy as np
A = np.random.randint(1000, size=(100, 100))
B = np.random.randint(1000, size=(100, 100))
C = np.random.randint(1000, size=(100, 100))

# A = [[12, 72, 53],
#     [84, 52, 69 ],
#     [71, 18, 79]]

# B = [[50, 86, 11],
#     [62, 87, 33],
#     [44, 50, 95]]

# C = [[2390, 8736, 1561],
#     [6242, 8657, 3653],
#     [4434, 5430, 9535]]

    
# result = [[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]]

x = len(A)
y = len(B)
z = len(C)


result = np.zeros([1000,1000])

for i in range(0,3,x): 
    for j in range(0,3,y): 
        for k in range(0,3,z): 
            for var25 in range(i,min(x,x+3)): 
                for var26 in range(j,min(y,y+3)): 
                    for var27 in range(k,min(z,z+3)): 
                        result[var25][var26] += A[var25][var27] * B[var27][var26]

print(result)
