import numpy as np

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
