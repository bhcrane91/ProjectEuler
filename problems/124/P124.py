import math

def radical(n):
    if n < 2:
        return 1 
    if n == 2:
        return 2
    
    r = []
    if n % 2 == 0:
        r.append(2)
        while n % 2 == 0:
            n //= 2 
        
    for i in range(3,int(math.sqrt(n)+1),2):
        if n % i == 0:
            r.append(i)
            while n % i == 0:
                n //= i 
    
    if n > 1:
        r.append(n)

    p = 1 
    for f in r:
        p *= f
    return p

N = 100000
rads = sorted([(i,radical(i)) for i in range(1,N+1)], key=lambda x: (x[1],x[0]))
print(rads[10000-1])
