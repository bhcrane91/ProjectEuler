a = 1
b = 2
sum = 0
target = 4000000
while b < target:
    curr = b + a
    a = b
    b = curr
    if a % 2 == 0:
        sum += a
        
print(f"Sum of even-valued Fibonacci terms < {target}: {sum}")