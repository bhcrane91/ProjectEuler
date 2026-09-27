import numpy as np

eulercoin = lambda n: (1504170715041707 * n) % 4503599627370517
    

coins = [(1,eulercoin(1))]
min = coins[0][1]
for i in range(2,4):
    next = eulercoin(i)
    if next < min:
        coins.append((i,next))
        min = next
    
print(coins)
print(sum(coin[1] for coin in coins))
print([coin[0] for coin in coins])