"""
Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.
"""
import numpy as np 

nums = np.linspace(1,100,num=100,dtype=int)
square_of_sum = np.sum(nums) ** 2
sum_of_square = np.sum(nums ** 2)
print("N -> :",square_of_sum - sum_of_square)