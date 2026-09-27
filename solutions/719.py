"""

We define an S-number to be a natural number, n, that is a perfect square and its
square root can be obtained by splitting the decimal representation of n into 
2 or more numbers then adding the numbers.

For example, 81 is an S-number because \sqrt{81} = 8+1
6724 is an S-number: \sqrt{6724} = 6+72+4
8281 is an S-number: \sqrt{8281} = 8+2+81 = 82+8+1
9801 is an S-number: \sqrt{9801} = 98+0+1

Further we define T(N) to be the sum of all S numbers n <= N. You are given
T(10^4) = 41333

Find T(10^{12})
"""

N = 10**12

# only need to check for n <= \sqrt{N} bc all n > \sqrt{N}, n**2 > N
def partitions(n, allowed, max_value=None):
    if max_value is None:
        max_value = n
    
    # Base case: when n is 0, return a list containing an empty partition
    if n == 0:
        return [[]]
    
    result = []
    
    # Iterate through all values from 1 to max_value (or less)
    for i in range(min(n, max_value), 0, -1):
        # Recursively call partitions for n - i with max_value as i
        if i in allowed:
            for partition in partitions(n=(n-i), allowed=allowed, max_value=i):
                result.append([i] + partition)
    
    return result

def split_dig(i,j):
    digits = []
    while j > 0:
        last = j % 10
        j = (j - last) // 10
        digits.append(last)
    combos = []
    for i in range(len(digits)):
        combos.extend(digits[i:],digits[:i])
    return combos
    
def split_num(s):
    def split_combos(s, start, current_combo, all_combos):
        if start == len(s):
            all_combos.append(current_combo)
            return

        for i in range(start + 1, len(s) + 1):
            split_combos(s, i, current_combo + [s[start:i]], all_combos)

    all_combos = []
    split_combos(s, 0, [], all_combos)
    return all_combos 

def S(s, target):
    def split_combos(s, start, current_combo, target):
        if start == len(s):
            if sum([int(j) for j in current_combo]) == target:
                return True
            return False

        for i in range(start + 1, len(s) + 1):
            if split_combos(s, i, current_combo + [s[start:i]], target):
                return True
            
        return False

    return split_combos(s, 0, [], target)

def find_S(args):
    s = 0
    print("Start: ",args)
    for i in range(args[0],args[1]):
        n = i**2
        if S(str(n),i):
            s += n
    print(args,s)
    return s 
"""
from tqdm import tqdm
s = 0
for i in tqdm(range(2,10**6+1)):
    n = i ** 2
    if S(str(n),i):
        s += n 
print(s)
"""
import multiprocessing


if __name__ == "__main__":

    c = multiprocessing.cpu_count() - 1
    N = 10 ** 6
    r = [[a*(N//c),(a+1)*(N//c)] for a in range(c)]
    r[0][0] = 2
    r[-1][-1] = N+1 

    # Create a Pool with 4 worker processes
    with multiprocessing.Pool(c) as pool:
        # Apply the function `square` to a list of numbers using map
        results = pool.map(find_S, r)

    print(results)  # Output: [1, 4, 9, 16, 25]
    print(sum(results))
