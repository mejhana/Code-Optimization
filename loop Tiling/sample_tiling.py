import numpy as np
A = np.random.randint(1000, size=(100, 100))
B = np.random.randint(1000, size=(100, 100))
C = np.random.randint(1000, size=(100, 100))


Len_A = len(A)
Len_B = len(B)
Len_C = len(A)

result = np.zeros([100,100])
for one in range(0,Len_A):
    for two in range(0,Len_B):
        for three in range(0,Len_C):
            result[one][two] += A[one][three] * B[three][two] + C[three][two]
