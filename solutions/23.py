import numpy as np 

def factors_from_primes(n):
    factors = [1]
    
    i = 1
    while n % 2 == 0:
        factors.append(2**i)
        n //= 2
        factors.append(n)
        i += 1
        
    for i in range(3,np.sqrt(n).astype(int)+1,2):
        while n % i == 0:
            factors += (np.array(factors)*i).tolist()
            factors.append(i)
            n //= i
            factors += ((np.array(factors)<i)*n).tolist()
            factors.append(n)
            
        
    return np.sort(np.unique(np.array(factors)))

print(factors_from_primes(28))

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

def abundant():
    return [n for n in range(2,28123) if n < np.sum(factorize(prime_factors(n)))]

nums = abundant()
setn = set(nums)
abund = set()
sum = 0
for i in range(len(nums)-1):
    for j in range(i,len(nums)):
        curr = nums[i] + nums[j]
        if curr in setn:
            sum += curr
            abund.add(nums[i])
            abund.add(nums[j])
            
print(sum)
print(abund)
            
            

    