import numpy as np
import pylong as pl

def to_binary(n):
    powers = []
    while n > 0:
        pow = (np.log(n) / np.log(2)).astype(int)
        n -= 2**pow 
        powers.append(pow)
    binary = np.zeros(np.max(powers)+1,dtype=int)
    for p in powers:
        binary[p] = 1
    return binary[::-1]

def palindrome(n):
    digits = pl.digits_from_scalar(n)
    if digits.tolist() == digits[::-1].tolist():
        binary = to_binary(n)
        if binary.tolist() == binary[::-1].tolist():
            return True
    return False

target = 1000000
sum = 0
for i in range(1,target):
    if palindrome(i):
        print(i)
        sum += i 
print()
print(sum)