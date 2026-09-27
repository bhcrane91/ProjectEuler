import numpy as np
import pylong as pl

pow = 5
numslist = np.arange(100,10**(pow+1))
print(numslist)
digits = [pl.resize(pl.digits_from_scalar(n),pow+1) for n in numslist]
numsdigs = np.sum(np.array(digits)**pow,axis=1)
numslist = numslist[numslist == numsdigs]
print(numslist)
print(np.sum(numslist))
