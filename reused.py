import math as m 

def check_prime(n):
    if n <= 1:
        return False 
    if n == 2: 
        return True
    if n % 2 == 0:
        return False 
    for i in range(3,int(m.sqrt(n))+1,2):
        if n % i == 0:
            return False 
    return True 

def prime_factors(n):
    factors = 0
    nums = []

    while n % 2 == 0:
        nums.append(2)
        n //= 2
        
    for i in range(3,int(m.sqrt(n))+1,2):
        while n % i == 0:
            nums.append(i)
            n //= i

    if n > 1:
        nums.append(n)
        
    return nums