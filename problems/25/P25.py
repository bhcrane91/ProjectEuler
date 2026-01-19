a = 1
b = 1 
c = 2
n = 1000
while len(str(b)) < n:
    t = a + b 
    a = b 
    b = t 
    c += 1

print(f"First Fibonacci term with {n} digits: F_n -> n = {c}")