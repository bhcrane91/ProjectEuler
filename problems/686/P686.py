import math as m
import sys 

def p(L,n):
    num = 2.0
    i = 0
    l = int(m.log10(L))
    j = 0
    # print(l)
    while i < n: 
        if int(num*(10**l)) == L:
            # print(i,num)
            i += 1
        num *= 2
        if num > 10:
            num /= 10
        j += 1
    return j

# print(p(123,45))
# print(p(123,45))
"""
time py 686.py 123 678910
193060223
/usr/local/bin/python3.11 686.py 123 678910  40.77s user 0.02s system 99% cpu 40.802 total
"""
print(p(int(sys.argv[1]),int(sys.argv[2])))




        