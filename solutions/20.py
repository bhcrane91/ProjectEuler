"""
n! = n * (n-1) * ... * 3 * 2 * 1
For example, 10! = 10*9*...*3*2*1=362880
and the sum of the digits is 3+6+2+8+8+0=27
Find the sum of the digits in the number 100!
"""
import pylong as pl 
import numpy as np

a = 100
b = pl.factorial(100)
c = np.sum(b)
d = pl.string_from_digits(b)
print(d,c)