from tqdm import tqdm
import math

def check_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True 

def gcd(a,b):
    while b != 0:
        t = b 
        b = a % b 
        a = t 
    return a 

def reduce_frac(n,d):
    g = gcd(n,d)
    while g != 1:
        n //= g
        d //= g 
        g = gcd(n,d)
    return n,d

"""N = 30
ts = lambda x,y: f"{x}/{y}"
S = 0
primes = []
pset = set()
red = []
for d in range(2,N+1):
    if check_prime(d):
        S += (d-1)
        primes.append(d)
        print(d,d-1)
    else:
        s = []
        z = []
        a = 0
        p = 0
        m = d // 2
        while primes[p] <= m:
            if gcd(primes[p],d) != 1:
                a += 1
                s.append(ts(primes[p],d))
            else:
                z.append(ts(primes[p],d))
            p += 1
        q = (1 + len(primes) - a)
        print(len(primes),d,q,len(s),s,len(z),z)
        S += q
        """


def sieve_phi(n):
    S = 0
    phi = list(range(n+1))
    for p in range(2, n+1):
        if phi[p] == p:  # p is prime
            phi[p] = p - 1
            for i in range(2 * p, n + 1, p):
                phi[i] = (phi[i] // p) * (p - 1)
        S += phi[p]
    return S

sieve_phi(1000000)