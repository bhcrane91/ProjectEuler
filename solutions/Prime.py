import numpy as np

def prime_factors(n):
    n_primes = 0
    primes = [1]
    factors = []
    together = []
    
    while n % 2 == 0:
        primes.append(2)
        n_primes += 1
        n //= 2
        factors.append(n)
        together.append((2,n))
        
    for i in range(3,np.sqrt(n).astype(int)+1,2):
        while n % i == 0:
            primes.append(i)
            n_primes += 1
            n //= i
            factors.append(n)
        together.append((i,n))

    if n > 1:
        primes.append(n)
        n_primes += 1
        together.append((n,n))
        
    return np.array(primes)


def check_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
        
    for i in range(3,np.sqrt(n).astype(int)+1,2):
        if n % i == 0:
            return False
    
    return True 


def primes_below(n):
    prime = 2
    primes = [2]
    nums = np.arange(n-1) + 2
    while len(nums) > 1:
        nums = nums[nums % prime != 0]
        prime = nums[0]
        primes.append(prime)
    return np.array(primes)


def primes_below(n):
    prime = 2
    sum = 2
    nums = np.arange(n-1) + 2
    while len(nums) > 1:
        nums = nums[nums % prime != 0]
        prime = nums[0]
        sum += nums[0]
    print(sum)