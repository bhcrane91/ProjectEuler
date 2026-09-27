import numpy as np 
import pylong as pl

sqrs = (np.arange(10) + 1) ** 2
nums = np.array([n for n in range(1,101) if n not in sqrs])
nums = [2]
total = 0
for num in nums:
    s = f'{np.sqrt(num):.100f}'[2:]
    print(s)
    numstr = pl.digits_from_string(s)
    total += np.sum(numstr)
    
print(total)
