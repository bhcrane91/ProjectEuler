import numpy as np
from collections import Counter 

def digits_from_scalar(scalar):
    digits = []
    while scalar > 0:
        last = scalar % 10
        digits.append(last)
        scalar = (scalar - last) // 10 
    return digits

N = 1
dom = 0
for i in range(10**N):
    num = Counter(digits_from_scalar(i))
    

