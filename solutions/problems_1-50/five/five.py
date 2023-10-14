"""
2520 is the smallest number that can be divided by each of the numbers from 1 
to 10. What is the samllest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""
import numpy as np

nums = np.arange(20) + 1
i = 300000
while np.sum(i % nums) != 0:
    print(i)
    i += 1
    
        

    