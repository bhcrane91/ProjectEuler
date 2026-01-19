import math

next_odd = lambda x: x + 1 if x % 2 == 0 else x + 2

def check_prime(n):
	if (n <= 1):
		return False
	if (n == 2):
		return True
	if (n % 2 == 0):
		return False
	for i in range(3,int(math.sqrt(n))+1,2):
		if (n % i == 0):
			return False
	return True

def next_prime(n):
	n = next_odd(n)
	while not check_prime(n):
		n = next_odd(n)
	return n

def gcd(a,b):
    while b != 0:
        t = b
        b = a % b 
        a = t 
    return a 

def relative_prime(a,b):
	return gcd(a,b) == 1

def totient(n):
	return sum([relative_prime(n,i) for i in range(1,n)])		
	
n = 2
t = totient(n)
f = n / t  

N = 1000000
c = 3


	
