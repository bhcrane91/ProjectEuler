def gcd(a,b):
    while b != 0:
        t = b 
        b = a % b 
        a = t 
    return a

def valid(m,n):
    # coprime and odd-even pair
    return gcd(n,m) == 1 and (n+m) % 2 == 1

def triple(m,n):
    # S = a+b+c = 2m**2 + 2mn = 2m * (m+n)
    a = (m**2 - n**2)
    b = (2*m*n)
    c = (m**2 + n**2)
    return [a,b,c]

M = 100
l = 15
tri = {}
for a in range(1,l):
    for b in range(1,a):
        t = triple(a,b)
        if valid(a,b) and sum(i<=M for i in t) == 3:
            print(a,b,t)

# D = sqrt(x^2 + c^2) + sqrt((a-x)^2 + b)
# (x,c) and (a-x,b) must form valid triples