"""
Triangle, pentagonal, and hexagonal numbers are generated 
by the following formulae:

Triangle    T[n] = n(n+1)/2     -> 1,3,6,10,15
Pentagonal	P[n] = n(3n-1)/2    -> 1,5,12,22,35
Hexagonal	H[n] = n(2n-1)      -> 1,6,15,28,45
 	
It can be verified that T[285] = P[165] = H[143]

Find the next triangle number that is also pentagonal and hexagonal.
"""

# Note T[a] = H[b] for all a = 2b-1, or when a is odd
# therefore n has to be 

import numpy as np 

n = np.arange(1,100001,2,dtype=np.int64)
pen = n*(3*n-1)//2
hex = n*(2*n-1)
shared = np.intersect1d(pen,hex)
print(shared)