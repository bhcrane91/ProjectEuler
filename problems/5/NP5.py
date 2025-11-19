"""
2520 is the smallest number that can be divided by each of the numbers from 1 
to 10. What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""
import numpy as np

print(f"{np.lcm.reduce(np.arange(20)+1)}")

