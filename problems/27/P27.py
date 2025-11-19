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

# primes > 1 by definition -> n = 0, b must be positive -> b = {primes < 1000}

primes = set(n_primes(200))
bees = primes_below(1000)
# print(bees)
        
f = lambda a,b,n: n**2 + (a*n) + b 

streak = (0,0,0)
for a in range(-999,1000):
    for b in bees:
        i = f(a,b,1)
        run = 1
        while i in primes:
            run += 1
            i = f(a,b,run)
        if run > streak[0]:
            streak = (run,a,b)             

print(streak,streak[1]*streak[2])