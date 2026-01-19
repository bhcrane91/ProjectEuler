import numpy as np 

def factorials(a,b):
    facts = {0:1}
    i = a 
    prod = 1
    while i <= b:
        prod *= i 
        facts[i] = prod
        i += 1
    return facts 

a = 1
b = 100
n = 1
r = 1
nums = factorials(a,b)
print(nums)
ans = 0
target = 1e6
for n in range(a,b+1):
    for r in range(a,n+1):
        top = nums[n]
        bot = nums[r] * nums[n-r]
        if top / bot > target:
            ans += 1
print(ans)



