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


a = 90
print(prime_factors(a*1))
print(prime_factors(a*2))
print(prime_factors(a*3))
print(prime_factors(a*4))
print(prime_factors(a*5))

    

    
    
    