
A = [[12, 72, 53 ,15],
    [84, 52, 69 , 14],
    [71, 18, 79, 89]]

B = [[50, 86, 11, 27],
    [62, 87, 33, 90],
    [44, 50, 95, 11]]

C = [[8, 6, 1, 7],
    [2, 7, 3, 9],
    [4, 0, 9, 1]]
    
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

Len_A = len(A)
Len_B = len(B[0])
Len_C = len(B)

for one in range(0,2+2,Len_A):
    for two in range(0,3+2,Len_B):
        for three in range(0,1+2,Len_C):
            for var21 in range(one,2,min(Len_A,Len_A+2)):
                for var22 in range(two,3,min(Len_B,Len_B+2)):
                    for var23 in range(three,1,min(Len_C,Len_C+2)):
                        result[var21][var22] += A[var21][var23] * B[var23][var22] + C[var23][var22]

print(result)