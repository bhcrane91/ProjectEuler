import numpy as np

def prime_factors(n):
    primes = []
    
    if n == 2:
        np.array([2])
    
    while n % 2 == 0:
        primes.append(2)
        n //= 2
        
    for i in range(3,np.sqrt(n).astype(int)+1,2):
        while n % i == 0:
            primes.append(i)
            n //= i
    
    if n > 1:
        primes.append(n)
        
    return np.array(primes)

streak = 0
distinct = 4
n = 2
nums = []
while streak != distinct:
    n_prfacs = np.unique(prime_factors(n))
    if len(n_prfacs) == distinct:
        streak += 1
        nums.append(n)
    elif streak > 0 and len(n_prfacs) != distinct:
        streak = 0
        nums = []
    n += 1

print(nums)
    