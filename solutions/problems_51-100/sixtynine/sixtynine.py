"""
Euler's totient function, phi(n), is defined as the number of positive integers not
exceeding n which are relatively prime to n. For example, as 1,2,4,5,7,8 are all 
<= 9 and relatively prime to 9 => phi(9) = 6

n  | Relatively Prime | phi(n) | n / phi(n) |
2  |        1         |    1   |     2      |
3  |       1,2        |    2   |    1.5     |  
4  |       1,3        |    2   |     2      |
5  |     1,2,3,4      |    4   |    1.25    |
6  |       1,5        |    2   |     3      |
7  |   1,2,3,4,5,6    |    6   |   1.166..  |
8  |     1,3,5,7      |    4   |     2      |
9  |   1,2,4,5,7,8    |    8   |    1.5     |
10 |     1,3,7,9      |    4   |    2.5     |

It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.
Find the maximum value of n/phi(n) for n <= 1e6
"""
import numpy as np

def totient(n):
    prime = np.arange(n-1) + 1
    primes = prime[n % prime != 0]
    if n % 2 == 0:
        primes = primes[primes % 2 != 0]
    print(n,len(primes)+1,prime,primes) 


def totient_max(n):
    input = np.arange(n) + 1
    
for i in range(2,11):
    totient(i)
    