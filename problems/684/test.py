def partition_with_k_parts(n, k, max_value=None):
    if max_value is None:
        max_value = n  # By default, the maximum value of any part is n
    
    if k == 0:
        return [[]] if n == 0 else []
    if n == 0:
        return []
    
    partitions = []
    
    # Iterate from the minimum possible value for a partition part to max_value
    for i in range(min(n, max_value), 0, -1):
        # Recur by reducing both the target sum n and the number of parts k
        
        for p in partition_with_k_parts(n - i, k - 1, i):
            partitions.append([i] + p)
    
    return partitions

# print(partition_with_k_parts(10000,2))
"""import math as m
a = 0
b = 1 
i = 1
l = 50
while i < l:
    t = a + b 
    a = b 
    b += 1 
    i += 1  
    k = []
    j = int(m.log10(b))+1
    while not k:
        k = partition_with_k_parts(b,j,9)
        j += 1
    kq = k[0]
    kmin = sum([j*10**i for i,j in enumerate(k[0])])
    for r in k[1:]:
        q = sum([j*10**i for i,j in enumerate(r)])
        if q < kmin:
            kq = r
            kmin = q 

    d = b // 9
    f = (10**(d) * (b % 9)) + (10**d-1)
    
    print(i,b,j,kq,kmin,f,10**d)
    # print(i,a,b)

# min n dig sum = (n%9) -> 9x(n/9)"""

def s(n):
    if n > 9:
        d = n // 9
        f = 10**d
        a = (f * (n % 9))
        b = (f - 1)
        c = f * ((n%9) + 1) - 1
        return a+b
    else:
        return n
    
import math as m 

def C(k):
    d = k - (k % 9)
    kd = k - d 
    # 1 -> d 
    F = lambda y: 10 ** ((y-9)//9)
    expr_1 = sum([9 * (6*F(9*i) - 1) for i in range(1,d//9+1)])
    # d -> k
    Q = 10 ** (k // 9)
    sum_i = lambda i: (i+1)*i // 2
    expr_2 = Q * (kd + sum_i(kd)) - kd
    return expr_1 + expr_2

S = 0
x = []
nines = []
for i in range(1,36):
    A = S//9
    q = s(i)
    S += q  
    """if i % 9 == 0:
        F = lambda y: 10 ** ((y-9)//9)
        expr = sum([9 * (6*F(9*i) - 1) for i in range(1,i//9+1)])
        x.append(S)
        print(i,q,S,F(i),expr,i//9)
    else:"""
    print(i,q,S,C(i))


F = lambda y: 10 ** ((y-9)//9)
expr = [9 * (6*F(i) - 1) for i in [9,18,27]]

# print(expr)