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
                if len(partition) < 3:
                    result.append([i] + partition)
    
    return [r for r in result if len(r) == 3]         

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
                if len(partition) < 3:
                    result.append([i] + partition)
    
    return [r for r in result if len(r) == 3]     

def partition_with_k_parts(n, k, allowed, max_value=None):
    """
    Partition a number n into exactly k parts.
    
    :param n: The number to be partitioned
    :param k: The exact number of parts
    :param max_value: The maximum value for any part (used for recursion)
    :return: A list of all partitions of n into exactly k parts
    """
    if max_value is None:
        max_value = n  # By default, the maximum value of any part is n
    
    if k == 0:
        return [[]] if n == 0 else []
    if n == 0:
        return []
    
    partitions = []
    
    # Iterate from the minimum possible value for a partition part to max_value
    for i in range(min(n, max_value), 0, -1):
        # Recur by reducing both the target sum n and the number of parts k
        if i in allowed:
            for p in partition_with_k_parts(n - i, k - 1, allowed, i):
                partitions.append([i] + p)
    
    return partitions

primes = []
square = [1]
N = 10000
first = 0
for i in range(2,N):
    if check_prime(i):
        primes.append(i)
    elif i % 2 != 0:
        parts = partition_with_k_parts(i,2,allowed=set(primes+square))
        if len(parts) == 0:
            first = i
        # print(i,len(parts))
    if np.sqrt(i) == np.sqrt(i).astype(int):
        square.append(i*2)
    if first > 0:
        break 
print("First:", first)
