"""
Define s(n) to be the smallest number that has a digit sum of n. For example s(10) = 19.
Let S(k) = \sum_{n=1}^k s(n). You are given S(20) = 1074.

Further let f_i be the Fibonacci sequence defined by f_0=0, f_1=1 and f_i=f_{i-2}+f_{i-1} for all i \ge 2.

Find \sum_{i=2}^{90} S(f_i). Give your answer modulo 1000000007.
"""

def bastardized(N):
    n = 9 
    m = N % n 
    p = N // n
    print(n,m,p)
    top = sum(10**i for i in range(p))
    return (45 * top) + (((m * (m+1))//2) * 10**p) + (n * (9*(top // 10))) + (m * 9 * top) 
# apply modulus 10e_ + 7 to each of the terms to get rid of 'top'
print(bastardized(317811))

"""
a = 0
f = 1
S = 0
for i in range(2,90+1):
    tmp = f 
    f += a 
    a = tmp
    print("before") 
    S += (bastardized(f) % 1000000007)
    print(i,f)
    print("after")

print(S)

"""
        
    