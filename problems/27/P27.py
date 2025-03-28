"""
Euler discovered the remarkable quadratic formula: f(n) = n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer
values 0 <= n <= 39. 

However, when n = 40: 
40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when 
n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes
for the consecutive values 0 <= n <= 79. The product of the coefficients, 
-79 and 1601, is -126479.

Considering quadratics of the form:
f(n) = n^2 + an + b
, where |a| < 1000 and |b| <= 1000
where |n|is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""
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