import math as m
# n = 1000000 : 10**6
n = 10
s = ""
c = 0
p = 0
for i in range(2):
    for j in range(10**i,10**(i+1)):
        q = c + i + 1
        # print(i,j,c,q)
        if q >= 10**p and c <= 10**p:
            s += str((j // (10**(q - c))) % 10)
            p += 1
            print(i,j,s,p,c,q)
        c = q
        


