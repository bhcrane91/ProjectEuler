"""
Find the 10001st prime
"""
import numpy as np

# Finds nth prime
def prime(n):
    primes = [2]
    while len(primes) < n:
        a = primes[len(primes)-1]
        b = a ** 2
        nums = np.linspace(a,b,num=b-a+1,dtype=int)
        for p in primes:
            nums = nums[nums % p != 0]
        primes += nums.tolist()
    print(primes[n-1])
        
# prime(100)
# prime(1000)
prime(10001)