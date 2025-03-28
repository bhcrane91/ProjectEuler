"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which 
a**2 + b**2 = c**2. There exists exactly one Pythagorean triplet for which 
a + b + c = 1000. Find the product abc.
"""
import numpy as np

"""
a**2 + b**2 = c**2 | a+b+c = 1000
-> a+b+c = a+b+np.sqrt(a**2+b**2) = 1000
"""

a = np.arange(100,901)
b = 1000-a
c1 = np.add.outer(a**2,b**2)
c2 = (1000-np.add.outer(a,b))**2
ans = np.where(c1==c2)
ans = list(zip(ans[0],ans[1]))

print(f"N -> Triple: ({ans[0][0]+100},{ans[1][0]+100},{np.sqrt(c1[ans[0][0]][ans[0][1]]).astype(int)}) | Product: {(ans[0][0]+100)*(ans[1][0]+100)*np.sqrt(c1[ans[0][0]][ans[0][1]]).astype(int)}")



        
        
        
        
    