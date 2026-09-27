p = 2
q = 5
l = 5
d = {}
m = []
i = 10**p
while i < 10**q:
    a = i**3
    b = str(a)
    k = "".join(sorted(b))
    v = d.get(k,[])
    if v:
        d[k].append(i)
        if len(d[k]) > len(m):
            m = d[k]
        if len(m) == l:
            print(m)
            i = float("inf")
    else:
        d[k] = [i]
    i += 1