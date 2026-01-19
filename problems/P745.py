S = 0
Q = 10**7
sqmx = 1
for n in range(1,Q+1):
    sqn = int(n**(1/2))
    if sqmx < sqn:
        sqmx = sqn
    for i in range(sqmx,0,-1):
        if n % (i**2) == 0:
            S += i**2
            print(i**2,n)
            break 

print(sqmx)
print(f"S({Q})={S}")
