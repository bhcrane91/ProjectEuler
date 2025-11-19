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

n = 1
i = 3
t = 10001
while n < t:
    n += check_prime(i)
    i += 2

print(f"{n}st prime = {i-2}")