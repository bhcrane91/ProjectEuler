from functools import reduce
import numpy as np
n = 100
print(f"Sum of digits of {n}! = {sum(int(i) for i in str(reduce(lambda x,y: x*y, np.linspace(1,n,n).astype(int))))}")

