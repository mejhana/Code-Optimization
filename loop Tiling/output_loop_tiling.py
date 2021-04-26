import numpy as np
A = np.random.randint(1000, size=(100, 100))
B = np.random.randint(1000, size=(100, 100))
C = np.random.randint(1000, size=(100, 100))


Len_A = len(A)
Len_B = len(B)
Len_C = len(A)

result = np.zeros([100,100])
for one in range(0,50,Len_A): 
    for two in range(0,50,Len_B): 
        for three in range(0,50,Len_C): 
            for var11 in range(one,min(Len_A,Len_A+50)): 
                for var12 in range(two,min(Len_B,Len_B+50)): 
                    for var13 in range(three,min(Len_C,Len_C+50)): 
                        result[var11][var12] += A[var11][var13] * B[var13][var12] + C[var13][var12]

