def P(n): 
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        p = 0 
        a = 1
        b = 1
        k = 1
        while not a and not b:
            a = P(n-k*(3*k-1)//2)
            b = P(n+k*(3*(-k)-1)//2)
            s = -1 if k % 2 == 0 else 1 
            p += s * (a + b)
            k += 1
        return p

n = 5
L = 1_000_000
p = P(n)
