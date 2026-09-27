import numpy as np 

def fib(n):
    a = 1 
    b = 1 
    i = 2
    while i != n:
        hold = b 
        b += a 
        a = hold 
        i += 1 
        print(i,b)
        
def fibLT(n):
    a = 1 
    b = 1 
    fibs = [0,a,b]
    while fibs[-1] < n:
        hold = b 
        b += a 
        a = hold 
        fibs.append(b)
    return np.array(fibs)

a = fibLT(500000)
"""
print(a)
b = a % 3
c = a % 38 
d = a % 76
print(b)
print(c)
print(d)
"""

print(a % 3)
print(a % 4)
print(a % 5)
print(a % 6)




