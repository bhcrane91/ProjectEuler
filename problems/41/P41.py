from itertools import permutations
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

def p41():
    max = 0
    for i in range(9,1,-1):
        for p in permutations([j for j in range(i,0,-1)]):
            q = sum([m*(10**n) for n, m in enumerate(p[::-1])])
            # print(p,q)
            if check_prime(q) and q > max:
                print("Prime: ",q)
                return q
    return None
    
ans = p41()
            
# ans = 7652413