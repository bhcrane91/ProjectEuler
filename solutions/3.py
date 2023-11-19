"""
What is the largest prime factor of 600851475143?
"""
import numpy as np 

def prime(n):
    nums = np.arange(n-1) + 2
    # print(nums)
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i+nums[i]::nums[i]] = 0
    nums = nums[nums != 0]
    return nums

primes = []
num = 600851475143
highest = prime(np.sqrt(num).astype(np.int64))
highest = highest[num % highest == 0]
print(highest)
   

