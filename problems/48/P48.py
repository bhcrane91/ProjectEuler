def modexp(a,b,d):
    if b == 0:
        return 1
    s = 1
    for i in range(b):
        s = (s*a) % (10**d)
    return s 

S = 0 
for i in range(1,1001):
    S += modexp(i,i,10)

print(S % 10**10)
