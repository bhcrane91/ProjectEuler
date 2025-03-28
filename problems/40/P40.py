i = 1000000
n = 1
j = 0
pow = 0
ans = 1

while j < i:
    ans *= (n % 10)
    for p in range(10**pow,10**(pow+1)):
        n += 1
        j += (p+1)
    pow += 1
    print(n,ans,j,pow)

