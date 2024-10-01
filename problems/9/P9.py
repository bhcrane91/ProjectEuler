"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which 
a**2 + b**2 = c**2. There exists exactly one Pythagorean triplet for which 
a + b + c = 1000. Find the product abc.
"""
import numpy as np
"""
a**2 + b**2 = c**2
a + b + sqrt(a**2 + b**2) = 1000
sqrt(a**2 + b**2) = 1000 - b - a
a**2 + b**2 = (1000 - b - a)**2
a**2 + b**2 = 1000**2 - 1000b - 1000a - 1000b + b**2 + ab - 1000a + ab + a**2
0 = 1000**2 - 2000a - 2000b + 2ab
2000(a + b) = 1000**2 + 2ab
"""
def euclid(m,n):
    a = m**2 - n**2
    b = 2*m*n 
    c = m**2 + n**2
import sys 
i = 0
for a in range(1,1000):
    for b in range(a,1000-a):
        c =1000-a-b
        print(a,b,c)
        left = (a**2 + b**2)
        right = c**2
        val = (left == right)
        if val:
            print(f"Answer: abc = {a*b*c}")
            sys.exit(0)
        elif left > right:
            break 
    else:
        continue 
        
        
        
        
    