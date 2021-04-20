import numpy as np
## This program is to rotate an array by d elements

## It is for this tutorial https://www.geeksforgeeks.org/array-rotation/
def arrayrotation(A,d):
    S = np.empty(A.shape)
    S[:len(A)-d] = A[d:len(A)]
    S[-d:]=A[:d]
    return S

A  = np.array([1,5,7,8,3,5,2,7])
d = 2
S = arrayrotation(A,d)
for x in S:
    print(x)
