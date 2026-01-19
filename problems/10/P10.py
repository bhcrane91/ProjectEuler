"""
Find the sum of all the primes below n (Specifically 10 online)
"""
import math 

def check_prime(n):
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n % 2 == 0: return False
    for i in range(3,(int(math.sqrt(n))+1),2):
        if n % i == 0: 
            return False
    return True

limit = 2000000
num_primes = 1
ans = 2
for i in range(1,limit,2):
    if check_prime(i):
        ans += i 
        num_primes += 1

print(f"Number of Primes below {limit}: {num_primes} | Sum: {ans}")