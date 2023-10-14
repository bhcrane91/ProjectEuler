"""
Find the sum of all the primes below n (Specifically 10 online)
"""
import numpy as np

def primes_below(n):
    prime = 2
    sum = 2
    nums = np.arange(n-1) + 2
    while len(nums) > 1:
        nums = nums[nums % prime != 0]
        prime = nums[0]
        sum += nums[0]
    print(sum)
 
def primes_two(n):
    nums = np.arange(n-1) + 2
    # print(nums)
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i+nums[i]::nums[i]] = 0
    # print(nums)
    print(np.sum(nums,dtype=np.int64))
    
def primes_three(n):
    primes = []
    nums = np.arange(n)
    for i in range(2, n):
        if nums[i] != 0:
            primes.append(nums[i])
            nums[i::nums[i]] = 0
    
    return sum(primes)

    
num = 2000000
# primes_below(num)
primes_two(num)
primes_three(num)