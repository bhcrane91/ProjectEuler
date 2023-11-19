import numpy as np

def prime_factors(n):
    n_primes = 0
    primes = [1]
    factors = []
    together = []
    
    while n % 2 == 0:
        primes.append(2)
        n_primes += 1
        n //= 2
        factors.append(n)
        together.append((2,n))
        
    for i in range(3,np.sqrt(n).astype(int)+1,2):
        while n % i == 0:
            primes.append(i)
            n_primes += 1
            n //= i
            factors.append(n)
        together.append((i,n))

    if n > 1:
        primes.append(n)
        n_primes += 1
        together.append((n,n))
        
    return np.array(primes)

def generate_pairs(lst):
    n = len(lst)
    all_pairs = []

    def generate_combinations(start, current_pair):
        if len(current_pair) > 0:
            all_pairs.append(list(current_pair))
        for i in range(start, n):
            current_pair.append(lst[i])
            generate_combinations(i + 1, current_pair)
            current_pair.pop()

    generate_combinations(0, [])
    return all_pairs

def factorize(primes):
  evens = primes[primes < 3]
  odds = generate_pairs(primes[primes > 2])
  factors = []
  # print(evens,odds)
  for e in range(len(evens)):
    pow = 2**e
    factors.append(pow)
    for o in odds:
      factors.append(pow*np.prod(o))
  return np.unique(factors)[:-1]

def amicable(n):
    primes = prime_factors(n)
    factors = factorize(primes)
    return np.sum(factors)

target = 10000
sum = 0
amnums = {}
for i in range(2,target):
    a = amicable(i)
    if amnums.get(i) == None and amnums.get(a) == None:
        b = amicable(a)
        if i == b and a != b:
            amnums[i] = a 
            amnums[a] = b 
            sum += (i+a)
print(sum)
        
    

