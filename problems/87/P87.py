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

L = 50000000
primes = sieve(int(L**(1/2)))
A = primes
B = [p for p in primes if p < (L**(1/3))]
C = [p for p in primes if p < (L**(1/4))]
x = lambda a,b,c: a**2 + b**3 + c**4

ans = set()
for a in A:
    for b in B:
        for c in C:
            k = x(a,b,c)
            if k < L:
                ans.add(k)
print(len(ans))