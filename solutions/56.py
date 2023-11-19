"""
A googol (10**100) is a massive number: one followed by one-hundred zeros; 
100**100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, a**b, where a, b < 1000, 
what is the maximum digital sum?
"""
import numpy as np
import pylong as pl
from tqdm import tqdm

max = 0
ans = (0,0)
for a in range(2,101):
    for b in range(2,101):
        curr = np.sum(pl.digits_from_scalar(a**b))
        if curr > max:
            max = curr 
            ans = (a,b)
print(ans, max)
        
