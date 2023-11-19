import numpy as np
import math as m

def check_prime(n):
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
        
    for i in range(3,np.sqrt(n).astype(int)+1,2):
        if n % i == 0:
            return False
    
    return True
    
sum = 0
target = 10
for i in range(1,target+1):
    if not check_prime(i):
        a = i-1
        while i % a != 0:
            a -= 1
        sum += a 
        print(i, a, sum)
    else:
        sum += 1
        print(i, 1, sum)