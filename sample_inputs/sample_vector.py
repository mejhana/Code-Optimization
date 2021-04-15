import numpy as np
n = 3
def dotProduct(vect_A, vect_B):
    product = 0
    #dot product
    for i in range(0, n):
        product = product + vect_A[i] * vect_B[i]
  
    return product
#cross product
def crossProduct(vect_A, vect_B, cross_P):
  
    cross_P.append(vect_A[1] * vect_B[2] - vect_A[2] * vect_B[1])
    cross_P.append(vect_A[2] * vect_B[0] - vect_A[0] * vect_B[2])
    cross_P.append(vect_A[0] * vect_B[1] - vect_A[1] * vect_B[0])
  
  

    vect_A = np.random.rand(3)
    vect_B = np.random.rand(3)
    cross_P = []
  

    print("Dot product:", end =" ")
    print(dotProduct(vect_A, vect_B))
    print("Cross product:", end =" ")
    crossProduct(vect_A, vect_B, cross_P)
# cross product of two vector array.
    for i in range(0, n):
        print(cross_P[i], end =" ")
  