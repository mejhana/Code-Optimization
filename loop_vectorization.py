import numpy as np
from math import sin as sn
import time
# Number of test points
N_point  = 1000
#custom function
def myfunc(x,y):
    if (x>0.5*y and y<0.3):
        return (sn(x-y))
    elif (x<0.5*y):
        return 0
    elif (x>0.2*y):
        return (2*sn(x+2*y))
    else:
        return (sn(y+x))
# List of stored elements
lst_x = np.random.randn(N_point)
lst_y = np.random.randn(N_point)
lst_result = []
# First for-loop
t1=time.time()
for i in range(len(lst_x)):
    x = lst_x[i]
    y= lst_y[i]
    if (x>0.5*y and y<0.3):
        lst_result.append(sn(x-y))
    elif (x<0.5*y):
        lst_result.append(0)
    elif (x>0.2*y):
        lst_result.append(2*sn(x+2*y))
    else:
        lst_result.append(sn(y+x))
t2=time.time()
print("\nTime taken by for loop method\n---------------------------------------\n")
print(time.time()*1000000) 
print("micro seconds")
# Numpy.vectorize method
vectfunc = np.vectorize(myfunc,otypes=[np.float],cache=False)
print("\nTime taken by vectorization method\n----------------------------------------------\n{} micro seconds".format(1000000*(t2-t1)))