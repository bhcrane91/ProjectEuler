import numpy as np
from tqdm import tqdm 

n = np.arange(1,10000)
p_n = n * (3*n - 1) // 2
min = p_n[len(p_n)-1]
for i in tqdm(range(len(p_n))):
    for j in range(i+1,len(p_n)):
        sum = p_n[i] + p_n[j]
        dif = np.abs(p_n[i] - p_n[j],dtype=int)
        if sum in p_n and dif in p_n and dif < min:
            min = dif 
            
print(dif)
        