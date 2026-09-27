# back
a = 1
b = 1
# front 
c = 1 
d = 1 
# mod
m = 1000000000
n = 2
s = set([1,2,3,4,5,6,7,8,9])

def pandigital(k):
    q = set()
    while k > 0:
        l = k % 10 
        if l in q or l == 0:
            return False 
        else:
            q.add(l)
        k //= 10
    return len(q) == 9

import math

def F(k):
    f = math.sqrt(5)
    a = 1 / f 
    b = (1 + f) / 2
    c = (1 - f) / 2 
    return a * ((b ** k) -  (c ** k))

# logb(a-c) = logb(a) + logb(1 - c/a)
"""

"""
def f(k):
    f = math.sqrt(5)
    a = 1 / f 
    return math.log10(a) + (k * math.log10((1 + f) / 2))
"""
The Mathematical MethodTo find the leading digits of a very large number \(N\):Calculate the logarithm: Find \(x = \log_{10}(N)\).Example: If \(N = 2^{1000}\), then \(x = 1000 \times \log_{10}(2) \approx 301.029995\).Isolate the fractional part: Take the decimal part (mantissa) of \(x\), which we'll call \(f\).Example: \(f = 0.029995\).Calculate the antilogarithm: Compute \(10^{f}\).Example: \(10^{0.029995} \approx 1.0715\).Extract the digits: The whole numbers (and the first few decimals) give you the leading digits of your large number.Example: \(2^{1000}\) begins with 10715...
"""

def q(k):
    return int((10**(k - int(k)))*m/10)



while not pandigital(b) or not pandigital(d):
    t = b 
    b = (a + b) % m
    a = t

    n += 1
    d = q(f(n))

    if pandigital(b):
        print(n,"->",b,d)
    if pandigital(d):
        print(n,b,"->",d)

print(n,b,d)


    

