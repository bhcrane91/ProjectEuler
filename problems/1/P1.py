# import sys

# arg = int(sys.argv[1])
arg = 1000
ans = sum([i for i in range(arg) if i % 3 == 0 or i % 5 == 0])

print(f"Python: Sum of multiples of 3 or 5 below {arg}: {ans}")