# (a*b) % n = ((a%n) * (b%n)) % n
from tqdm import tqdm
def factorial(n):
    if n < 2:
        return 1
    else:
        f = 1
        while n > 1:
            f *= n 
            n -=1 
        return f 

def sieve(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
           
    primes = [p for p in range(2, n + 1) if prime[p] and p > 4]
    return primes

S = 0
primes = sieve(10**8)
for i in tqdm(primes):
    fs = [factorial(i-j) % i for j in range(1,6)]
    S += (sum(fs) % i)
print(S)    