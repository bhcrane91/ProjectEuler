import numpy as np 
from itertools import permutations
import math
from tqdm import tqdm 

"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
Abundant numbers are those whose propers divisors to sum to greater than the number, deficient numbers are the opposite.
All primes are deficient.
All integers greater than 28123 can be expressed as the sum of two abundant numbers.
"""

"""
Find the all abundant numbers < 28123.
Add them all to each other and remove from set until left with non abundantly summed
"""

def partitions(n, max_value=None):
    if max_value is None:
        max_value = n
    
    # Base case: when n is 0, return a list containing an empty partition
    if n == 0:
        return [[]]
    
    result = []
    
    # Iterate through all values from 1 to max_value (or less)
    for i in range(min(n, max_value), 0, -1):
        # Recursively call partitions for n - i with max_value as i
        for partition in partitions(n - i, i):
            result.append([i] + partition)
    
    return result

def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,int(n/i)])
    return list(set(divs))

cutoff = 28124  
abundants = []
doubles = []
for i in tqdm(range(12,cutoff)):
    if sum(divisors(i)) > i:
        abundants.append(i)
        for j in abundants:  
            doubles.append(j+i)

non_abundant = sum(list(set([i for i in range(cutoff)]) - set(doubles)))
print(non_abundant)