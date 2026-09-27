"""
145 is curious because: 1! + 4! + 5! = 1 + 24 + 120 = 145
Find the sum of tal the numbers which are equal to the sum of the 
factorial of their digits.
"""
import numpy as np
from tqdm import tqdm

def fctrl(n):
    if n == 0 or n == 1:
        return 1
    else:
        return int(np.prod(np.arange(1,n+1)))

factorials = {i:fctrl(i) for i in range(10)}

digit_factorials = []
for n in range(3,10**6):
    num = n
    sum = 0
    while num > 0:
        d = num % 10
        num = (num - d) // 10
        sum += factorials[d]
        if sum > n:
            num = 0       
    if sum == n:
        digit_factorials.append(n)
        print(n)
   
digit_factorials = np.array(digit_factorials) 
print(digit_factorials)
print(np.sum(digit_factorials))

    