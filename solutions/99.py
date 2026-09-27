"""
Comparing two numbers written in index form like 2**11 and 3**7 is not difficult, 
as any calculator would confirm that 2^**11 = 2048 < 3**7 = 2187.

However, confirming that 632382**518061 > 519432**525806 would be much more
difficult, as both numbers contain over three million digits.

Using txtF/base_exp.txt, a file containing one thousand lines with a base/exponent
pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
import math as m 

with open("txtF/base_exp.txt", "r") as f:
    data = [int(num) for line in f.read().split("\n") for num in line.split(",")]

bases = data[0::2]
expts = data[1::2]

pairs = [[bases[i],expts[i]] for i in range(len(bases))]

max = 0
maxVal = 0

for pair in pairs:
    n = pair[-1] * m.log(pair[0])
    if n > maxVal:
        maxVal = n
        max = pairs.index(pair)
        print(max+1,maxVal)

print(f"Answer -> Max Value: {maxVal} | Line Number: {max+1}")


