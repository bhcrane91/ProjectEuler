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
    up = "".join(sorted(str(total)))
    down = up[::-1]
    if total != int(up) and total != int(down):
        bouncy += 1
    else:
        pass 
        # print("".join(num),"".join(up),"".join(down))

print(bouncy/total,total,bouncy)

# v2 

    