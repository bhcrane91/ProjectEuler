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

def partitions(n, allowed, max_value=None):
    if max_value is None:
        max_value = n
    
    # Base case: when n is 0, return a list containing an empty partition
    if n == 0:
        return [[]]
    
    result = []
    
    # Iterate through all values from 1 to max_value (or less)
    for i in range(min(n, max_value), 0, -1):
        # Recursively call partitions for n - i with max_value as i
        if i in allowed:
            for partition in partitions(n=(n-i), allowed=allowed, max_value=i):
                result.append([i] + partition)
    
    return result

def primes_below(n):
    primes = []
    for i in range(n):
        if check_prime(i):
            primes.append(i)
    return primes 

def next_prime(n):
    n += 1
    while not check_prime(n):
        n += 1 
    return n 

"""pdict = {}
p = 41 
pl = primes_below(p)

ps = 0
p = 0
for i in range(10):
    p = next_prime(p)
    ps += p 
    pdict[i] = {"sum": ps, "prime": p}
"""
# print(pdict)


def sumz(n):
    smax = 0
    L = 0
    i = 0
    j = len(n)
    S = []
    for i in range(len(n)):
        for j in range(len(n),i,-1):
            lc = j-i
            ac = n[i:j]
            sc = sum(ac)
            S.append((lc,sc,ac[0],ac[-1]))
            if lc > L and check_prime(sc):
                smax = sc
                L = lc
                print(smax,L,ac[0],ac[-1])
    return S, smax, L, ac[0], ac[-1]

P = primes_below(10000)
S, smax, L, A, B = sumz(P)
q = 0
l = 0
for k in S[::-1]:
    if k[1] < 1000000 and check_prime(k[1]) and k[0] > l:
        print(k)
        l = k[0]
# print(S)