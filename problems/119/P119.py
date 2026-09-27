s = 1
r = []
for j in range(1,1000):
    for i in range(1,10):
        k = j**i
        if sum(int(c) for c in str(k)) == j and k > 10:
            r.append(k)
            print(f"{s}: {j}**{i}={k}")
            s += 1


for k,v in enumerate(sorted(r)):
    print(k+1,v)