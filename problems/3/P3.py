import math as m 

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

num = 600851475143
factors = prime_factors(num)
print(f"Python -> Prime Factors of {num}: {factors} | Largest -> {factors[-1]}")

