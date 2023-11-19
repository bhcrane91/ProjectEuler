from tqdm import tqdm 

N = 100
U_n = 0
for n in range(3,N+1):
    S_n = []
    mn = 0
    for k in range(0,(n*(n-2))+1):
        curr = n+k
        mn += curr
        if mn % curr == 0:
            S_n.append(k)
    print(n,S_n[1:],sum(S_n))
    U_n += sum(S_n) #T(n)
    
print(U_n)