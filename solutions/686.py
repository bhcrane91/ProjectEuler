import math as m

def p(L,n):
    i = 0
    j = 0
    digits = len(str(L))
    while i < n: 
        num = 2**j // (10**(int(m.log(2**j,10))-digits+1))
        print(num)
        if L == num:
            i += 1
        j += 1
        print(j)
    return j 

print(p(12,1))
print(p(12,2))
print(p(123,45))
print(p(123,678910))




        