import numpy as np

def permutate(sequence,j):
    if len(sequence) == 0:
        # Base case: Return a list with a single empty sequence
        return [[]]
    
    all_permutations = []
    
    for i, elem in enumerate(sequence):
        # Choose the current element as the first element
        first_elem = [elem]
        
        # Recursively generate permutations for the remaining elements
        rest_permutations = permutate(sequence[:i] + sequence[i+1:])
    
        # Combine the chosen element with each of the generated permutations
        for perm in rest_permutations:
            all_permutations.append(first_elem + perm)
    
    return all_permutations

# rewrite faster using axes
def dig_to_num(nums):
    numbers = []
    for num in nums:
        pows = (10 ** np.arange(len(num))[::-1]).astype(np.int64)
        numbers.append(np.sum(num*pows))
    return np.array(numbers)
        
digits = np.arange(10).tolist()
newnum = np.array(permutate(digits))
lexsrt = np.sort(dig_to_num(newnum))
print(newnum)
print(lexsrt, len(lexsrt), lexsrt[1000000-1])
# print(lexsrt[1000000])
