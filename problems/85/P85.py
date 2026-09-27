N = 100
L = 2000000
A = [(0,0),L]
F = lambda k,j: (k * (k+1) * j * (j+1)) // 4 

for m in range(1,N+1):
    for n in range(1,m+1):
        s = F(m,n)
        D = abs(L - s)
        if D < A[-1]:
            A = [n,m,s,D]
            # print(A)

print(A[0]*A[1])