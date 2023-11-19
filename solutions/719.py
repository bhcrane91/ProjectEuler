import numpy as np
import pylong as pl

def splits(digits):
    l = len(digits)
    if l < 3:
        return np.sum(digits)
    if l == 3:
        pass
    
    
target = 10**4
for i in range(np.sqrt(target)+1):
    n = i**2
    s = pl.digits_from_scalar(n)[::-1]
    
    