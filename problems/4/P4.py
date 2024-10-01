"""
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91*99
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def product(digits):
    bot = 10**(digits-1)
    top = 10**digits
    max = (0,0,0)
    for i in range(top,bot-1,-1):
        for j in range(top,bot-1,-1):
            p = i*j
            if p > max[0] and str(p) == str(p)[::-1]:
                max = (p,i,j)
    return max

print(product(3))