def product(digits):
    bot = 10**(digits-1)
    top = 10**digits
    top = top - (top % 11)
    max = (0,0,0)
    for i in range(top,bot-1,-11):
        for j in range(top,bot-1,-1):
            p = i*j
            if p > max[0] and str(p) == str(p)[::-1]:
                max = (p,i,j)
    return max

ans = product(3)
print(f"P -> Max: {ans[0]} | Factors: ({ans[1]},{ans[2]})")

import numpy as np 

def gcd(l):
    g = np.gcd(l[0],l[1])
    for d in l[2:]:
        g = np.gcd(d,g)
    return g 

def base_palindrome_terms(n):
    s = [1] * (n*2)

10000001 + 1000010 + 100100 + 11000
1000000001,100000010,10000100,1001000,110000