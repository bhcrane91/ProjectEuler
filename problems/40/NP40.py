import numpy as np

num = 1000000
digits = ''
nums = np.arange(num).astype(str)
i = 0
while len(digits) < num+1:
    digits += nums[i]
    i += 1
    # print(i,digits)
    
# print(digits)
    
digits = np.array([digit for digit in digits]).astype(int)
pows = 10 ** np.arange(7)
print(digits[pows])
chosen = np.prod(digits[pows])
print(chosen)
