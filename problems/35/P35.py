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

N = 1000000
print(f"Number of Circular Primes below {N}: {len([i for i in range(N) if sum([check_prime(int(str(i)[j:]+str(i)[:j])) for j in range(len(str(i)))]) == len(str(i))])}")