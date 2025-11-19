import numpy as np

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

def n_primes(n):
    primes = []
    i = 1
    while len(primes) < n:
        if check_prime(i):
            primes.append(i)
        i += 1
    return primes

def primes_below(n):
    primes = []
    for i in range(1000):
        if check_prime(i):
            primes.append(i)
    return primes 

i = 11
trunks = []
primes = set([p for p in n_primes(100000) if (p > 10)])
for p in primes:
    sprime = str(p)
    sprimes = [int(sprime[i:]) for i in range(1,len(sprime))] + [int(sprime[:i]) for i in range(1,len(sprime))]
    sprime = set([check_prime(s) for s in sprimes])
    if sprime == set([True]):  
        trunks.append(p)
    if len(trunks) == i:
        break

print(len(trunks),trunks,sum(trunks))


    
    
    
    
