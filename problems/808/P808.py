import numpy as np
# import pylong as pl

"""
Both 169 and 961 are the square of a prime. 169 is the reverse of 961.

We call a number a reversible prime square if:

1) It is not a palindrome.
2) It is the square of a prime.
3) Its reverse is also the square of a prime.

169 and 961 are not palindromes, so both are reversible prime squares.

Find the sum of the first 50 reversible prime squares.
"""

# print(revp(5))

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

def n_primes(n):
    primes = []
    i = 1
    while len(primes) < n:
        if check_prime(i):
            primes.append(i)
        i += 1
    return primes

def digits(n):
    nums = []
    while n > 0:
        l = n % 10
        nums.append(l)
        n = (n - l) // 10
    return nums

def is_palindrome(n):
    num = digits(n)
    return num == num[::-1]


rps = set()
cutoff = 50
i = 0
"""
while len(rps) < cutoff:
    if check_prime(i):
        isq = i ** 2
        isq_digits = digits(isq)
        if isq_digits != isq_digits[::-1]:
            rev = sum(j*(10**i) for i,j in enumerate(isq_digits[::-1]))
            revsqrt = rev**(0.5)
            if revsqrt == int(revsqrt):
                if check_prime(int(revsqrt)):
                    rps.add(isq)
                    rps.add(rev)
                    print(len(rps),i,isq,rev,revsqrt)
    i += 1
"""

while len(rps) < cutoff:
    if check_prime(i):
        rev = sum(j*(10**i) for i,j in enumerate(digits(i)[::-1]))
        if check_prime(rev):
            print(i,rev)
            rps.add(i)
            rps.add(rev)
    i += 1
# if p == prime, n**2 = p**2[::-1] -> p
print(rps)
print(sum(rps))






