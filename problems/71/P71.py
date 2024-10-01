t = 3 
b = 7
d = 1000000
D = (float('inf'),0,0)

for i in range(1,d+1):
    x = (3 * i) // 7
    for j in range(1,x+1):
        # print(j,i)
        s = (t/b) - (j/i)
        if s < D[0] and s != 0:
            D = (s,j,i)
            print(D)

print(D)

## only search between the last found and 3/7