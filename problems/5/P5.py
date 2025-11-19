import math as m 
from functools import reduce

# EUCLIDEAN ALGORITHM 

def GCD(a,b):
    while b != 0:
        t = b
        b = a % b 
        a = t 
    return a 

def LCM(a,b):
    return a * b // GCD(a,b)

print(f"{reduce(LCM, [i+1 for i in range(20)])}")

