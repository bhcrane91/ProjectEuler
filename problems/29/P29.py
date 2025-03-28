import numpy as np
"""
for i in range(3,15):
    nums = np.arange(2,i,dtype=np.int64)
    table = nums[:, np.newaxis] ** nums
    dim = i-2
    unq = len(np.unique(table.flatten()))
    print(dim,unq)
"""

def ijsq(n):
    return len({i**j for i in range(2, n+1) for j in range(2, n+1)})

# for i in range(101):   
print(100, ijsq(100))