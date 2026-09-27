import numpy as np
from tqdm import tqdm 

T = 12000
S = 0
fracs = {'1/3','1/2'}
for d in tqdm(range(4,T+1)):
    b = d // 3 + 1
    t = d // 2
    for f in range(b,t+1):
        frac = np.array([f,d])
        # print(frac)
        g = np.gcd.reduce(frac)
        while g != 1:
            frac //= g 
            g = np.gcd.reduce(frac)
        F = "/".join(frac.astype(str))
        if F not in fracs:
            S += 1 
            fracs.add(F)


print(S)
# print(fracs)