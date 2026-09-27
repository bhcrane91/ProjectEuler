# 
import math 

def long_div(a,b):
    i = a // b 
    rem = a - (b*i)
    r = []
    while len(r) < 100:
        if rem < b:
            rem *= 10
        else:
            f = (rem//b)
            rem -= (f*b)
            r.append(f)
    return i,r 


# print(long_div(73,6))
# sq = set([i*i for i in range(10)])

def sqrt_heron(s, precision, guess):
    if s == 0:
        return 0
    s = float(s)

    if s < 0:
        raise ValueError("sqrt(s) is not defined for negative numbers.")

    # Silently enforce minimum precision
    if precision < 2:
        precision = 2

    guard = 25  # temporary extra digits for internal stability
    max_iter = 10_000
    
    guess = (guess + s / guess) / 2
    for _ in range(max_iter):
        next_guess = (guess + s / guess) / 2

        # Stop when improvement is small enough
        if guess - next_guess < 10**(-precision):
            break
        guess = next_guess
    return guess
    
print(sqrt_heron(2,1000,1))