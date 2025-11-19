import math

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
	n += 1
	while not check_prime(n):
		n += 1
	return n

truncatable = 11
prime = next_prime(10)
s = 0 

while truncatable > 0:
	trunc = True 
	for i in range(1,len(str(prime))):
		if not (check_prime(prime % (10**i)) and check_prime(prime // (10**i))):
			trunc = False 
	if trunc:
		print(prime)
		truncatable -= 1
		s += prime 
	prime = next_prime(prime)
		
print(s)
