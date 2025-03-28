import numpy as np

def coprime(a,b):
    return np.gcd(a,b) == 1

def triple(k,m,n):
    a = k * (m**2 - n**2)
    b = k * (2*m*n)
    c = k * (m**2 + n**2)
    return [a,b,c]

target = 1000
triangles = {str(i):[] for i in range(1,target)}
for m in range(2,100):
    for n in range(1,m):
        for k in range(1,100):
            if coprime(m,n) and (m + n) % 2 != 0:
                t = triple(k,m,n)
                p = sum(t)
                if p < target:
                    triangles[str(p)].append(t)

max = 0
for k,v in triangles.items():
    if len(v) > max:
        # print(k,len(v),v)
        max = len(v)
        print(max, k, v)

