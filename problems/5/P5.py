import math as m 
from functools import reduce

def prime_factors(n):
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2 
    for i in range(3,int(m.sqrt(n))+1,2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def gcd(a,b):
    prime_factors_a = prime_factors(a)
    prime_factors_b = prime_factors(b)
    div = 1
    for item in prime_factors_a:
        if item in prime_factors_b:
            div *= item
            prime_factors_b.remove(item)
    return div
            
def lcm(a,b):
    """
    LCM(a,b) = (a * b) / GCD(a,d)
    """
    return a * b // gcd(a,b)

print(reduce(lcm, [i+1 for i in range(10)]))