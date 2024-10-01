"""
For a positive integer d, let f(d) be the number created by sorting the digits 
of d in ascending order, removing any zeros. For example, f(3403) = 334.

Let S(n) be the sum of f(d) for all positive integers d of n digits or less. 
You are given S(1) = 45 and S(5) = 1543545675.

Find S(18). Give your answer modulo 1123455689.
"""

def f(d):
    digits = []
    while d > 0: 
        l = d % 10
        d = (d - l) // 10
        if l != 0:
            digits.append(str(l))
    return "".join(sorted(digits))

digits = 7
base = "0" * digits
total = 10 ** digits
