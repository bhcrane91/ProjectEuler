import pylong as pl
import numpy as np 

nums = np.arange(1,1001,dtype=np.int64)
expn = np.zeros((len(nums),10),dtype=np.int64)
for i,n in enumerate(nums):
    curr = pow(n,n)%(10**10)
    if curr == 0:
        curr = np.zeros(10,dtype=np.int64)
    else:
        curr = pl.digits_from_scalar(curr)
        if len(curr) != 10:
            curr = pl.resize(curr,10)
    expn[i] = curr 
print(expn)
a = expn[0]
for e in expn[1:]:
    a = pl.add(a,e)

print(a)
print(pl.string_from_digits(a))
    