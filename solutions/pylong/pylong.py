import numpy as np
import re 
from tqdm import tqdm

class Pylong: 

    def __init__(self):
        self.attribute = "initialized"

    def string_from_digits(self,input):
        z = np.argmax(input[::-1] != 0)
        input = input[:len(input)-z]
        return ''.join(input[::-1].astype(str))

    def scalar_from_digits(self,digits):
        pow = 10 ** np.arange(len(digits))
        return np.sum(digits*pow)

    def digits_from_string(self,input):
        digits = re.sub(r'\D','',input)
        return np.array([int(d) for d in digits])[::-1]

    def digits_from_scalar(self,scalar):
        digits = []
        while scalar > 0:
            last = scalar % 10
            digits.append(last)
            scalar = (scalar - last) // 10 
        return np.array(digits)

    def to_singles(self,num):
        while not (num < 10).all():
            dim = len(num)
            singles = np.zeros((dim,dim),dtype=num.dtype)
            for i in range(dim):
                j = i
                while num[i] > 0:
                    last = num[i] % 10
                    num[i] = (num[i] - last) // 10
                    singles[i][j] = last
                    j += 1 
            num = np.sum(singles,axis=0)
        return num

    def resize(self,digits,new_len):
        digits = np.pad(digits, (0,new_len-len(digits)),'constant',constant_values=0)
        return digits

    def cut(self,digits):
        idx = np.argmax(digits[::-1] != 0)
        return digits[:len(digits)-idx]

    def operation_prep(self, digits_a, digits_b, operation):
        if operation == '*':
            new_len = len(digits_a) + len(digits_b)
        elif operation == '+':
            new_len = max(len(digits_a), len(digits_b)) + 1
        digits_a = resize(digits_a, new_len)
        digits_b = resize(digits_b, new_len)
        return digits_a, digits_b

    def add(self,a,b):
        a, b = operation_prep(a, b, '+')
        return to_singles(a + b)
    
    # a*b
    def multiply(self,a,b):
        a, b = operation_prep(a, b, '*')
        steps = len(a)
        prod = np.zeros(steps,dtype=a.dtype)
        for i in range(steps):
            prod += a[i] * np.roll(b,i)
        prod = to_singles(prod)
        return prod
   
    # a ** b     
    def exponentiate(self,a,b):
        a = digits_from_scalar(a)
        if b > 0:
            a, new_a = operation_prep(a,a,'*')
            for i in tqdm(range(b-1)):
                new_a = cut(multiply(a,new_a))
                a, new_a = operation_prep(a,new_a,'*')
        else:
            new_a = np.array([1])
        return new_a

    def exp_mod(self,a,b,c):
        a = digits_from_scalar(a)
        if b > 0:
            a, new_a = operation_prep(a,a,'*')
            for i in tqdm(range(b-1)):
                new_a = multiply(a,new_a)[:c]
                a, new_a = operation_prep(a,new_a,'*')
        else:
            new_a = np.array([1])
        return new_a

    # a ** b     
    def exponentiate_digits(self,a,b):
        if b > 0:
            a, new_a = operation_prep(a,a,'*')
            for i in tqdm(range(b-1)):
                new_a = cut(multiply(a,new_a))
                a, new_a = operation_prep(a,new_a,'*')
        else:
            new_a = np.array([1])
        return new_a

    # a!
    def factorial(self,a):
        if a == 0:
            return digits_from_scalar(1)
        digits_a = digits_from_scalar(a)
        while a > 1:
            digits_b = digits_from_scalar(a-1)
            digits_a, digits_b = operation_prep(digits_a,digits_b,'*')
            digits_a = cut(multiply(digits_a,digits_b))
            a -= 1
        return digits_a

        