import numpy as np
import math as m

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
    
squares = [1]
S = 0
T = 100
for i in range(1,T+1):
    if check_prime(i):
        S += 1 
    elif np.sqrt(i) == np.sqrt(i).astype(int):
        squares.append(i)
        S += i 
    else:
        for n in squares[::-1]:
            if i % n == 0:
                S += n 
                break 

print(S)