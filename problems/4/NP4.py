import numpy as np
    
def product(digits):
    low = (10**(digits-1))
    high = (10**digits)-1
    x = np.arange(low,high+1)
    y = x
    from_table = np.unique(np.outer(x,y)).astype(str)
    pals = np.array([int(n) for n in from_table if n[::-1] == n]).astype(int)
    print(f"NumPy | Max: {np.max(pals)}")
    
product(3)