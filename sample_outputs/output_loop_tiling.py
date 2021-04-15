
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
    
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

x = len(A)
y = len(B[0])
z = len(B)

for i in range(0,2,x): 
    for j in range(0,2,y): 
        for k in range(0,2,z): 
            for var17 in range(i,min(x,x+2)): 
                for var18 in range(j,min(y,y+2)): 
                    for var19 in range(k,min(z,z+2)): 
                        result[var17][var18] += A[var17][var19] * B[var19][var18]

print(result)