import numpy as np

p0 = 5
pN = 100
k0 = 1 
kN = 6 

def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return int(np.prod(np.arange(1,n+1)))
    
sig_n = [fac(p0-k) for k in range(k0,kN)]
prevSig = sum(sig_n)
ans = prevSig % p0
print(ans)
first = sig_n[0]
last = sig_n[-1]
for p in range(p0+1,pN):
    sig_n = [first*(p-1)] + sig_n[:-1]
    first = sig_n[0]
    prevSig = first + prevSig 
    ans += prevSig % (p-1)
    prevSig -= last 
    last = sig_n[-1]
    
    
print(ans)
    
    