cache = {}
target = 1000000
max = 0
num = 0
for i in range(1,target):
    itr = 1
    x = i
    while x != 1: 
        if cache.get(x):
            cache[i] = cache[x] + itr 
            continue
        if x % 2 == 0:
            x /= 2
        else:
            x = 3*x + 1
        itr += 1
    cache[i] = itr
    if cache[i] > max:
        max = cache[i]
        num = i
print(f"Maximum Collatz Sequence for c[0] < {target}: c[0] = {num} | Length: {max}")