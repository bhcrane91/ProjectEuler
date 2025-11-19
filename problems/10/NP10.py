"""
Find the 10001st prime
"""
import numpy as np

def primes(n):
    primearr = [2]
    nums = np.linspace(3,n,num=n-3+1,dtype=int)
    # print(primearr,nums)
    while len(nums) > 0:
        nums = nums[nums % primearr[-1] != 0]
        try:
            primearr.append(nums.item(0))
            # print(primearr,nums)
        except Exception as e:
            return primearr
    return primearr    

limit = 2000000
p = primes(limit)
print(f"Number of Primes below {limit}: {len(p)} | Sum: {sum(p)}")