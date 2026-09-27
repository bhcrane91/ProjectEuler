"""
The first known prime found to exceed one million digits was discovered in 1999, 
and is a Mersenne prime of the form (2**6972593)-1; it contains exactly 
2098960 digits. Subsequently other Mersenne primes, of the form (2**p)-1, 
have been found which contain more digits. However, in 2004 there was found a 
massive non-Mersenne prime which contains 2357207 digits: 
-> 28433 * (2**7830457) + 1

Find the last ten digits of this prime number.
"""
import pylong as pl
from tqdm import tqdm

"""
a**b = (a**c) * (a**(b-c))
"""

"""
2**7830457  = (2**57) * (2**7830400)
            = (2**57) * (2**(78304))**100
            = (2**57) * (2**(783*100 + 4))**100
            = (2**57) * [((2**783)**100)**100 * (2**4)**100)]**100
            = c       * [((d)**100)**100 * e] **100

2**783 = 2**(700+83) = 2**7**100 * 2**83
"""
a = pl.digits_from_scalar(28433)
b = 7830457
c = pl.exp_mod(2,b,10)
d = pl.multiply(c,a)
e = pl.add(d,pl.digits_from_scalar(1))
print(pl.string_from_digits(e))

