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

for i in range(0,100):
    p = partitions(i,allowed=sieve(i))
    if len(p) > 5000:
        print(i,len(p))
        break

