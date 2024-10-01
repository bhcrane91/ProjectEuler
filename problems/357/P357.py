"""
Consider the divisors of 30: 1,2,3,5,6,10,15,30
It can be seen that for every divisor d of 30, d + 30/d is prime.
Find the sum of all positive integers not exceeding 100000000 (1e8)
such that for every divisor d of n, d + n/d is prime.
"""
import numpy as np
import pylong as pl

n = int(1e8)
nums = []
for i in range(1,n):
    for j in range(1,i):
        
        