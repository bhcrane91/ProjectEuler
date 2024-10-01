from pylong.pylong import Pylong
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

def digits_from_scalar(scalar):
        digits = []
        while scalar > 0:
            last = scalar % 10
            digits.append(last)
            scalar = (scalar - last) // 10 
        return np.array(digits)

def D(n):
    i = 0
    j = 2
    num = 0
    while i != n:
        num = digits_from_scalar(j)
        if check_prime(np.sum(num)):
            i += 1 
            print(i,j,num)
        j += 1
    

D(100000000)