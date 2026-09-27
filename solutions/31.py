"""
In the United Kingdom the currency is made up of pound (£) and pence (p). 
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, $1 (100p), and $2 (200p).

It is possible to make $2 in the following way:

$1 + 1x50p + 2x20p + 1x5p + 1x2p + 3

How many different ways can £2 be made using any number of coins?
"""
from tqdm import tqdm 

def partitions(n, max_value=None):
    allowed = {200,100,50,20,10,5,2,1}
    if max_value is None:
        max_value = n
    
    # Base case: when n is 0, return a list containing an empty partition
    if n == 0:
        return [[]]
    
    result = []
    
    # Iterate through all values from 1 to max_value (or less)
    for i in range(min(n, max_value), 0, -1):
        # Recursively call partitions for n - i with max_value as i
        if i in allowed:
            for partition in partitions(n - i, i):
                result.append([i] + partition)
    
    return result

possible = partitions(200)
# print(possible)
print(len(possible))
        