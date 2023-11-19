import numpy as np
import pylong as pl

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


def check_prime(n):
    if n % np.floor(n) > 0:
        return False
    return type(prime_factors(n)) == np.ndarray

def rev_primes_below(n):
    prime = 2
    rev_primes = []
    primes = [2]
    nums = np.arange(n**3-1) + 2
    while len(rev_primes) < n:
        nums = nums[nums % prime != 0]
        prime = nums[0]
        primes.append(prime)
        original = prime**2
        reverse = pl.scalar_from_digits(pl.digits_from_scalar(original)[::-1])
        reverse_rt = np.sqrt(reverse)
        if check_prime(reverse_rt) and original != reverse:
            rev_primes.append(original)
            rev_primes.append(reverse)
            nums = nums[nums % reverse_rt != 0]
            primes.append(reverse_rt)
    return np.array(rev_primes), np.sum(rev_primes)

def revp(n):
    rev = []
    i = 2
    while len(rev) < n:
        if check_prime(i):
            forward = np.int64(i)**2
            reverse = pl.scalar_from_digits(pl.digits_from_scalar(forward)[::-1].astype(np.int64))
            if forward != reverse and check_prime(np.sqrt(reverse)):
                print(i)
                rev.append(forward)
                rev.append(reverse)
        i += 1
    rev = np.array(rev)
    return rev, np.sum(rev)
    
print(revp(50))