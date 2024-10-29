"""
The following iterative sequence is defined for the set of positive integers:
f(n) =  { n/2   if n % 2 == 0
        { 3n+1  if n % 2 != 0
Ex: n = 13
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
What is the 
"""
import numpy as np
from tqdm import tqdm 

def collatz(n):
    i = 1
    x = n
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3*x + 1
        i += 1
    return i,n

max = 0
num = 0
target = 1000000
for i in range(1,target):
    curr, cn = collatz(i)
    if curr > max:
        max = curr
        num = cn
        
print(f"Maximum Collatz Sequence for c[0] < {target}: c[0] = {num} | Length = {max}")
    