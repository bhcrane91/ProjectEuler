"""
2520 is the smallest number that can be divided by each of the numbers from 1 
to 10. What is the samllest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""
import numpy as np

# Formula for LCM of  a and b: lcm(a,b) = a*b / gcd(a,b)
lcm = 1
nums = np.arange(20) + 1
for num in nums:
    lcm = np.lcm(num,lcm)
    # gd = np.gcd(lcm,num,dtype=np.int64)
    # lcm = lcm * num // gd
    # print(lcm,gd)
print(lcm)

