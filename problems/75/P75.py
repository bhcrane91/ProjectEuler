from pprint import pprint 
from tqdm import tqdm
import math

def gcd(a,b):
    while b != 0:
        t = b 
        b = a % b 
        a = t 
    return a 

def valid(n):
    # coprime and odd-even pair
    return [i for i in range(1,n) if gcd(i,n) == 1 and (i+n) % 2 == 1]

def triple(m,n):
    # S = a+b+c = 2m**2 + 2mn = 2m * (m+n)
    a = (m**2 - n**2)
    b = (2*m*n)
    c = (m**2 + n**2)
    return a+b+c

L = 1500000
tri = {}
for m in range(2,int(math.sqrt(L))):
    for n in valid(m):
        t = triple(m,n)
        k = t 
        while k < L:
            if tri.get(k):
                tri[k] += 1
            else:
                tri[k] = 1 
            k += t
print(len([v for v in tri.values() if v==1]))

        

