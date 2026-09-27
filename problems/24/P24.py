from functools import reduce 

n = 9
digits = [i for i in range(n+1)]

target = 1000000
perms = 0
x = 0

factorial = lambda z: reduce(lambda x,y: x*y, [i for i in range(1,z+1)]) if z > 1 else 1

