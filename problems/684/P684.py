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
import math as m

MOD = 1000000007
def C(k):
    d = k - (k % 9)
    kd = k - d 
    # 1 -> d 
    F = lambda y: 10 ** ((y-9)//9)
    expr_1 = sum([(9 * (6*F(9*i) - 1)) % MOD for i in range(1,d//9+1)])
    # d -> k
    Q = 10 ** (k // 9)
    sum_i = lambda i: (i+1)*i // 2
    expr_2 = Q * (kd + sum_i(kd)) - kd
    return expr_1 + expr_2

a = 0
b = 1 
i = 1
l = 90
SA = 0
while i < l:
    t = a + b 
    a = b 
    b = t
    i += 1
    SA += C(b) % MOD
    print(i,b,SA)
    

# min n dig sum = (n%9) -> 9x(n/9)