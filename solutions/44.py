from tqdm import tqdm
import sys 

P = lambda n: (3*(n**2) - n) // 2

pentagonal_nums = [P(n) for n in range(1,5000)]
pset = set(pentagonal_nums)
# pentagonal_nums = {22,70,92,48}
D = (float('inf'),0,0)
for jm in range(1,len(pentagonal_nums)):
    for km in range(len(pentagonal_nums[:jm])):
        j = pentagonal_nums[jm]
        k = pentagonal_nums[km]
        s = j + k 
        d = j - k
        if s in pset and d in pset and d < D[0]:
            D = (d,j,k)
            print(D)
            sys.exit(128)


# print(pentagonal_nums)
        
        