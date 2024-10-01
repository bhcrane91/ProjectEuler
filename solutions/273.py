"""
Consider equations of the form: a^2 + b^2 = N, 0 <= a <= b, a, b and N integer.

For N=65 there are two solutions:
a=1, b=8 and a=4, b=7.
We call S(N) the sum of the values of a of all solutions of a^2 + b^2 = N, 0 <= a <= b, a, b and N integer.
Thus S(65) = 1 + 4 = 5.
Find sum S(N), for all squarefree N only divisible by primes of the form 4k+1 with 4k+1 < 150.
"""

"""
Find primes of the form 4k + 1 < 150
"""
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

p = [4*p+1 for p in range(38) if check_prime(4*p+1)]
print(p)
    