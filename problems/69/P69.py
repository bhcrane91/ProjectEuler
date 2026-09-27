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
	if check_prime(n):
		return n - 1
	return sum([relative_prime(n,i) for i in range(1,n)])	

def sieve_phi(n):
    phi = list(range(n+1))
    for p in range(2, n+1):
        if phi[p] == p:  # p is prime
            phi[p] = p - 1
            for i in range(2 * p, n + 1, p):
                phi[i] = (phi[i] // p) * (p - 1)
    return phi

	
N = 1000000
m = [-1,-1,-1]
for i, x in enumerate(sieve_phi(N)):
	try:
		if i/x > m[2]:
			m = [i,x,i/x]
			print(m)
	except Exception as e:
		pass