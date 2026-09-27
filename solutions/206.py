from itertools import permutations 

n = "1_2_3_4_5_6_7_8_9_0".split("_")
p = [i for i in range(1,10)]
for c in permutations(p):
    s = n 
    for k in range(len(s)):
        if s[k] == "_":
            s[k] = str(c[k-1])
    b = int("".join(s))
    q = b**0.5
    if q == int(q):
        print(b,q)
        break
    
