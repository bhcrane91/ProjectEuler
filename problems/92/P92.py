q = 0
S = 0
l89 = set()
l1 = set()
for i in range(1,10000000):
    s = i
    # print(i)
    while s not in [1,89] and s not in l89 and s not in l1:
        while s > 0:
            l = s % 10
            q += l ** 2 
            s = (s-l) // 10
        s = q 
        q = 0
        # print("\t",i,s)
    # print(i,s)
    if s == 89 or s in l89:
        l89.add(i)
        S += 1
    else:
        l1.add(i)

print(S)

# Answer
# 8581146
# /usr/local/bin/python3.11 92.py  47.25s user 0.02s system 99% cpu 47.305 total