"""
Fibonacci Sequence: F[n] = F[n-1] + F[n-2], F[1] = F[2] = 1
What is the index of the first term in the sequence with 1000 digits?
"""
import numpy as np 
import pylong as pl 

a = pl.digits_from_scalar(1)
b = pl.digits_from_scalar(1)
i = 2
while len(b) < 1000:
    next = pl.add(a,b)
    a = pl.cut(b) 
    b = pl.cut(next)
    i += 1
    print(i,len(b))
    
ans = pl.string_from_digits(b)
print(i,ans,len(ans))