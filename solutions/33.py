def digits(n):
    j = n
    dig = []
    while j > 0:
        l = j % 10 
        dig.append(l)
        j = (j - l) // 10 
    return dig 

for j in range(11,100):
    for i in range(10,j):
        t = digits(i)
        b = digits(j)
        r = set(t) & set(b)
        if r and (i % 10 != 0 and j % 10 != 0):
            # print(i,j)
            r = r.pop()
            t.remove(r)
            b.remove(r)
            if b[0] != 0 and i/j == t[0]/b[0]:
                print(i,j,t[0],b[0],i/j,t[0]/b[0])
                
"""
16 64 1 4 0.25 0.25 -> 1/4
26 65 2 5 0.4 0.4   -> 2/5
19 95 1 5 0.2 0.2   -> 1/5
49 98 4 8 0.5 0.5   -> 1/2
                    ______
                    (1*2*1*1) / (4*5*5*2) = 1/100
Ans = 100
"""
