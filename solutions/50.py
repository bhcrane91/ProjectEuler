import numpy as np
import sys
from tqdm import tqdm

def primes_below(n):
    nums = np.arange(n-1) + 2
    prime = nums[0]
    primes = [prime]
    while len(nums) > 1:
        nums = nums[nums % prime != 0]
        primes.append(nums[0])
        prime = primes[-1]
    return np.array(primes)

def check_prime(n):
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
        
    for i in range(3,np.sqrt(n).astype(int)+1,2):
        if n % i == 0:
            return False
    
    if n > 1:
        return True
    
def pbelow2(n):
    return [i for i in range(2,n) if check_prime(i)]

target = 10000
primes_list = pbelow2(target)
primes_set = set(primes_list)
max = 0
run = []
for i in range(len(primes_list)-2):
    for j in range(i+2,len(primes_list)):
        ps = sum(primes_list[i:j])
        if ps < target and ps in primes_set and (j-i) > max:
            max = j-i
            run = primes_list[i:j]
            print(max,ps,i,j)
            
            
        


