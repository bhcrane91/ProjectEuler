"""
If we take 47, reverse and add, 47 + 74 = 121, which is a palindrome.
Not all numbers produce palindromes so quickly. For example,
349 + 943 = 1292
1292 + 2921 = 4213
4213 + 3124 = 7337
-> 349 took 3 iterations to arrive at a palindrome. Although no one has 
proved it yet, it is thought that some numbers, like 196, never produce 
a palindrome. A number that never forms a palindrome through the reverse
and add process is called a Lychrel number. Due to the theoretical nature
of these numbers, and for the purpose of this problem, we shall assume 
that a number is Lychrel until proven otherwise. In addition you are 
given that for every number below ten-thousand, it will either 
(i) become a palindrome in less than fifty iterations
(ii) no one, with all the computing power that exists, has managed so 
    far to map it to a palindrome.

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; 
the first example is 4994.
How many Lychrel numbers are there below ten-thousand?
"""
import numpy as np 

def rev(n):
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n //= 10
    return r 

lychrel = 0
N = 10000
for i in range(1,N):
    n = i
    l = True
    for j in range(50):
        print(i,n)
        n = n + rev(n)
        if n == rev(n):
            l = False
            
            break
    lychrel += l

print(lychrel)


        
