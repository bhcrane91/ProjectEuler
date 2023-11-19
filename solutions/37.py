import numpy as np 
import pylong as pl

def check_prime(n):
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
        
    for i in range(3,np.sqrt(n).astype(int)+1,2):
        if n % i == 0:
            return False
    
    return True 

i = 11pip
trunks = []
while len(trunks) != 11:
    if check_prime(i):
        num = pl.digits_from_scalar(i)
        nums = 0
        for j in range(num.size):
            nums += check_prime(pl.scalar_from_digits(num[j:]))
            nums += check_prime(pl.scalar_from_digits(num[:j+1]))
        if nums == num.size:
            trunks.append(i)
    i += 1
    
print(trunks)
print(sum(trunks))

          
        
         
        
    
    
    
