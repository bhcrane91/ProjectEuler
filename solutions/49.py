import numpy as np
from collections import Counter 

def check_prime(n):
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
        
    for i in range(3,np.sqrt(n).astype(int)+1,2):
        if n % i == 0:
            return False
    
    return True

def prime_digits(n):
    return {i for i in range(10**(n-1),10**n) if check_prime(i)}

primes = prime_digits(4)
target = 3330
triplets = []
for a in primes:
    for b in primes:
        if a < b:
            diff = b - a
            if (b + diff) in primes and diff == target:
                nums = [a,b,b+diff]
                news = np.unique([Counter(str(n)) for n in nums])
                if len(news) == 1:
                    triplets.append(nums)          
        
print(triplets)