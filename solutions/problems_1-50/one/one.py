"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6, and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import numpy as np

nums = np.arange(1000)
threes = nums[nums % 3 == 0]
fives = nums[nums % 5 == 0]
combined = np.union1d(threes,fives)
print(np.sum(combined))