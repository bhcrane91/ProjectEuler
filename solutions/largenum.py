import numpy as np
import re
from tqdm import tqdm

### CLEAN UP
# When represented in array form, the number will always
# be reverse. Ex 167 = [7 6 1], 1234567 = [7 6 5 4 3 2 1], etc.

def digits_from_string(input):
    digits = re.sub(r'\D','',input)
    return np.array([int(d) for d in digits])

def string_from_digits(input):
    z = np.argmax(input[::-1] != 0)
    input = input[:len(input)-z]
    return ''.join(input[::-1].astype(str))

def scalar_from_digits(digits):
    pow = 10 ** np.arange(len(digits))
    return np.sum(digits*pow)

def singles_from_digits(digits):
    dim = len(digits)
    singles = np.zeros((dim,dim),dtype=digits.dtype)
    for i in range(dim):
        singles[i] = np.roll(rsz_math(num_to_dig_math(digits[i])[::-1],dim),i)
    return singles

def num_to_dig_math(num):
    digits = []
    while num > 0:
        last = num % 10
        digits.append(last)
        num = (num - last) // 10
    return np.array(digits).astype(int)

def num_to_dig_read(num):
    return num_to_dig_math(num)[::-1]

def rsz_math(num,new_len):
    new_num = np.zeros(new_len,dtype=num.dtype)
    new_num[new_len-len(num):] = num
    return new_num[::-1]

def mult_core(a,b):
    if len(a) == len(b):
        newlen = len(a)
        prod = np.zeros(newlen,dtype=a.dtype)
        for i in range(len(a)):
            prod += a[i] * np.roll(b,i)
        while not (prod < 10).all():
            prod = singles_from_digits(prod)
            prod = np.sum(prod,axis=0)
        return prod

def mult_prep(a,b):
    a = num_to_dig_read(a)
    b = num_to_dig_read(b)
    newlen = len(a) + len(b)
    a = rsz_math(a,newlen)
    b = rsz_math(b,newlen)
    return a, b
    
def multiply(a,b):
    a, b = mult_prep(a,b)
    return mult_core(a,b)

def exp_cut(num):
    idx = np.argmax(num[::-1] != 0)
    return num[:len(num)-idx]

def exp_prep(a,b):
    a = exp_cut(a)
    b = exp_cut(b)
    newlen = len(a) + len(b)
    a = rsz_math(a,newlen)
    b = rsz_math(b,newlen)
    return a, b

def mult_core(a,b):
    if len(a) == len(b):
        newlen = len(a)
        prod = np.zeros(newlen,dtype=a.dtype)
        for i in range(len(a)):
            prod += a[i] * np.roll(b,i)
            print(prod)
        while not (prod < 10).all():
            prod = singles_from_digits(prod)
            prod = np.sum(prod,axis=0)
        return prod
    
# a ** b
def expon(a,b):
    if b > 0:
        a, new_a = mult_prep(a,a)
        for i in range(b-1):
            new_a = exp_cut(mult_core(a,new_a))[::-1]
            a, new_a = exp_prep(a,new_a)
    else:
        a, new_a = mult_prep(a,1)
    return new_a

a = 167
b = 25
print(string_from_digits(multiply(a,b)))

c = 2 
d = 1000
# a = string_from_digits(expon(c,d))
# for i in range(20):
#     print(f"2**{i}",string_from_digits(expon(c,i)))

            

