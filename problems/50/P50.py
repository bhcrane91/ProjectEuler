import numpy as np

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
            for partition in partitions(n=(n-i), allowed=[j for j in allowed if j != i], max_value=i):
                    try:
                        if [partition[0],i] == [allowed[-2],allowed[-1]]:
                            result.append([i] + partition)
                    except Exception as e:
                        pass

    
    return result

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

N = 41
primes = [p for p in range(N) if check_prime(p)][::-1]

            
        


