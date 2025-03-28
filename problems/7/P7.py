import math as m 

def check_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(m.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True 

n = 0
i = 1
t = 10001
while n < t:
    i += 1
    n += check_prime(i)

print(f"P -> {n}st prime = {i}")