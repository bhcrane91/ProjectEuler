from itertools import permutations 

myset = [n for n in range(1,10)]
for perm in permutations(myset):
    print(list(perm),sum([j*10**(8-i) for i,j in enumerate(perm)]))