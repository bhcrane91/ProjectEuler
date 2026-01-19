"""
We shall say that an n-digit number is pandigital if it makes use of all the digits
1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can 
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def partition_with_k_parts(n, k, allowed, max_value=None):
    """
    Partition a number n into exactly k parts.
    
    :param n: The number to be partitioned
    :param k: The exact number of parts
    :param max_value: The maximum value for any part (used for recursion)
    :return: A list of all partitions of n into exactly k parts
    """
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
        if i in allowed:
            for p in partition_with_k_parts(n - i, k - 1, allowed, i):
                partitions.append([i] + p)
    
    return partitions

p = [q for q in partition_with_k_parts(9,3,allowed=[n for n in range(1,9)])] # if q[0] == (sum(q[1:]) - 1) or q[0] == sum(q[1:]) or q[0] == sum(q[1:]) + 1]
print(p)
u = set()
a = 0
b = {str(q) for q in range(1,10)}
for g in p:
    for i in range(10**(g[1]-1),10**g[1]):
        for j in range(10**(g[2]-1),10**g[2]):
            k = i * j
            s = str(k)+str(j)+str(i)
            if k not in u and set(s) == b and len(s) == 9:
                print(i,j,k,s)
                u.add(k)
                a += k 

print(a)


