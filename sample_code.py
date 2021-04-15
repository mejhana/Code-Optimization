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

for i in range(0,x):
    for j in range(0,y):
        for k in range(0,z):
            result[i][j] += A[i][k] * B[k][j]
print(result)