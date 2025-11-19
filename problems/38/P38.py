max = 0
nmx = 0
for n in range(1,3):
    pds = []
    for i in range(9*10**(n-1),10**n):
        s = [1]*9
        c = [0]*9
        j = 0
        ps = ""
        while c != s and j < 9:
            j += 1
            k = i*j
            ps += str(k)
            # print(i,k,ps)
            while k > 0:
                l = k % 10 
                c[l-1] += 1
                k = (k - l) // 10
                if l-1 < 0:
                    print(i,k,ps)

        # print(i,j,c)
        if c == s:
            pds.append((i,ps))
    for p in pds:
        print(p)
    # print(pds)