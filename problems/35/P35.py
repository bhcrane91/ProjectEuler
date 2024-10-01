import numpy as np
import pylong as pl 

def primes_below(n):
    prime = 2
    primes = [2]
    nums = np.arange(n-1) + 2
    while len(nums) > 1:
        nums = nums[nums % prime != 0]
        prime = nums[0]
        primes.append(prime)
    return np.array(primes)

def prime_factors(n):
    primes = [1]
    
    if n == 2:
        return np.array([1,2])
    
    while n % 2 == 0:
        primes.append(2)
        n //= 2
        return primes
        
    for i in range(3,np.sqrt(n).astype(int)+1,2):
        while n % i == 0:
            primes.append(i)
            n //= i
            return primes
    
    if n > 1:
        primes.append(n)
        
    return np.array(primes)

def primes_below_2(n):
    primes = []
    for i in range(2,n):
        if type(prime_factors(i)) != list:
            primes.append(i)
    return np.array(primes)

def check_prime(n):
    return type(prime_factors(n)) == np.ndarray

def pb_dict(n):
    primes = {}
    for i in range(2,n):
        if primes.get(i) == None and check_prime(i):
            digits = pl.digits_from_scalar(i)
            d = len(digits)
            perm = np.array([np.sum(np.roll(digits,j)*(10**np.arange(d))) for j in range(d)])
            perm = [p for p in perm if check_prime(p)]
            if len(perm) == d:
                for p in perm:
                    primes[p] = 0
    print(len(primes))
                
pb_dict(1000000)  
    
# Logical check
"""
a = primes_below(100)
b = np.array([n for n in range(2,100) if type(prime_factors(n)) != list])
print(np.sum(a != b))
"""