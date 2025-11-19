from functools import reduce
n = 100
print(f"Sum of digits of {n}! = {sum(int(i) for i in str(reduce(lambda x,y: x*y, [j for j in range(1,n+1)])))}")