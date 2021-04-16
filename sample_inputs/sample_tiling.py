
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

for one in range(0,2,Len_A):
    for two in range(0,3,Len_B):
        for three in range(0,1,Len_C):
            result[one][two] += A[one][three] * B[three][two] + C[three][two]
print(result)