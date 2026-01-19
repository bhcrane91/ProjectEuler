def gcd(a,b):
    while b != 0:
        t = b
        b = a % b 
        a = t 
    return a 

a = 1 
b = 1
for i in range(1,10):
    for j in range(1, 10):
        n = (i * 10) + j
        for k in range(9,i,-1):
            m = (j * 10) + k 
            if k*n == m*i:
                a *= i
                b *= k
                # print(n, m)

g = gcd(a,b)
while g != 1:
    a //= g 
    b //= g 
    g = gcd(a,b)

print(b)

