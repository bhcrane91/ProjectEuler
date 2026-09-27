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

def f(p,n):
    return (((p - 1) ** n) + ((p + 1) ** n)) % (p**2)


L = 10**9
n = 10
p = [(i+1,j,f(j,i+1)) for i,j in enumerate(sieve(100000))]
print([k for k in p if k[0] == 7037])