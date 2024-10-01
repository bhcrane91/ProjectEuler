import numpy as np 

def digits_from_scalar(scalar):
    digits = []
    while scalar > 0:
        last = scalar % 10
        digits.append(last)
        scalar = (scalar - last) // 10 
    return digits

bouncy = 0
total = 99
while (bouncy/total) < 0.99:
    total += 1
    num = digits_from_scalar(total)
    up = sorted(num)
    down = up[::-1]
    if num != up and num != down:
        # print(num,up,down)
        bouncy += 1

print(bouncy/total,total,bouncy)
    