import numpy as np
import pylong as pl
from tqdm import tqdm

def prime_factors(n):
    factors = 0
    nums = []

    while n % 2 == 0:
        nums.append(2)
        factors += 1
        n //= 2
        
    for i in range(3,np.sqrt(n).astype(int),2):
        while n % i == 0:
            nums.append(i)
            factors += 1
            n //= i

    if n > 1:
        nums.append(n)
        factors += 1
        
    return factors, nums


target = 10**8
sum = np.int64(1)
for i in tqdm(range(2,target+1)):
    exp = prime_factors(i)
    sum += np.power(2,exp,dtype=np.int64)
print(sum)

print(prime_factors(43))
    
    
    