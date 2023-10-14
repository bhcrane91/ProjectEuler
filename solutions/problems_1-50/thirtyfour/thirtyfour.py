"""
145 is curious because: 1! + 4! + 5! = 1 + 24 + 120 = 145
Find the sum of tal the numbers which are equal to the sum of the 
factorial of their digits.
"""
import numpy as np
import pylong as pl 

nums = np.arange(3,10**6)
digit_factorials = []
for n in nums:
    digits = pl.digits_from_scalar(n)
    sum = 0
    for d in digits:
        sum += pl.scalar_from_digits(pl.factorial(d))
    if sum == n:
        digit_factorials.append(n)
   
digit_factorials = np.array(digit_factorials) 
print(digit_factorials)
print(np.sum(digit_factorials))

    