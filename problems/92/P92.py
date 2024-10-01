q = 0
S = 0
for i in range(1,10000000):
    s = i
    while s not in [1,89]:
        while s > 0:
            l = s % 10
            q += l ** 2 
            s = (s-l) // 10
        s = q 
        q = 0
    # print(i,s)
    if s == 89:
        S += 1

print(S)

# Answer
# 8581146
# /usr/local/bin/python3.11 92.py  47.25s user 0.02s system 99% cpu 47.305 total