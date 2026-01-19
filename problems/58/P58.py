import numpy as np

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
    
s = 4
n = 9
corners = 5
primes = 3
while (primes / corners) > 0.1:
    for i in range(4):
        n += s 
        if check_prime(n):
            primes += 1
        corners += 1
    s += 2
    
print(s, primes, corners, primes/corners)