import numpy as np

"""
powers = np.arange(10)
sum = 0
for p in powers:
    print(p)
    for i in range(10**p,10**(p+1)):
        root = np.power(i,1/(p+1),dtype=np.float64)
        if root % np.ceil(root) == 0:
            sum += 1
            print(i,root,sum,p+1)
"""

nums = np.arange(1,22,dtype=np.int64)
sum = 0
for i in range(1,22):
    powers = nums ** i
    powersbtw = powers[(powers >= np.int64(10**(i-1))) & (powers < np.int64(10**i))]
    sum += len(powersbtw)
    print(powersbtw, sum)    
    
c = 0
for n in range(1,10):
    for k in range(1,22):
        if np.floor(1 + k * np.log10(n)) == k:
            c += 1
print(c)