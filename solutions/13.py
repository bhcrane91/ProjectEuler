"""
Find the first ten digits of the sum of the following 
one-hundred 50-digit numbers (digits.txt)
"""
import pylong as pl
import numpy as np

with open("digits.txt","r") as f:
    numbers = f.read().split("\n")
    

sum = np.zeros(len(numbers[0]),dtype=int)
i = 1
for n in numbers:
    sum = pl.add(sum,n)
    sum = pl.cut(sum)
    i+=1
    
botten = sum[:10]
topten = sum[::-1][:10]
print(sum)
print(np.sum(topten),np.sum(botten),pl.string_from_digits(sum))





    

