import numpy as np

def eulercoin(n):
    a = np.int64(1504170715041707)
    b = np.int64(4503599627370517)
    return (a*n) % b 
 
coins = [eulercoin(1)]
for i in range(2,6131):
    next = eulercoin(i)
    if next < coins[-1]:
        coins.append(next)
    else:
        print(next)
    
print(coins)
print(np.sum(coins))