from tqdm import tqdm 
import math 

def sieve(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
           
    primes = [p for p in range(2, n + 1) if prime[p]]
    return primes

L = 10**6
primes = sieve(L)
pset = set(primes)
doubles = 0
last = 0
for i in tqdm(range(2,L+1)):
    if i in pset:
        d = 2
    else:
        x = 0
        n = i
        d = 0
        while primes[x] <= i and n > 1:
            if n % primes[x] == 0:
                d += 1
            while n % primes[x] == 0:
                d += 1
                n //= primes[x]
            x += 1
        # print(i,d)
        if d == last:
            doubles += 1
        else:
            last = d 


    
        
            
            


