"""
Consider the fraction, n/d, where n and d are positive integers. 
If n < d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
                                          ^
                                          |

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d <= 1000000 in ascending 
order of size, find the numerator of the fraction immediately to the left of \dfrac 3 7.</p>
"""

# Lowkewy prob couldve searched from the top down instead of bottom up but w/e

n = 3 
d = 7 
frac = n/d
a = 1
b = 3 
D = 1000000 
diff = float("inf")

while b < D:
    tmpb = b + 1 
    l = (tmpb*a)//b 
    r = (tmpb*n)//d
    if l != r:
        for i in range(l,r+1):
            newfrac = i/tmpb 
            if newfrac < frac and (frac - newfrac) < diff:
                b = tmpb
                a = i 
                diff = frac - newfrac
                # print(a,b)
            elif newfrac > frac or newfrac < (a/b):
                b += 1
    else:
        b += 1 
  
print(f"{a}/{b}") 