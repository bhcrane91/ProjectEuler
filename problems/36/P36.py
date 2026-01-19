palindrome = lambda x: x == x[::-1]
N = 1000000
print(sum(i if palindrome(str(i)) and palindrome(bin(i)[2:]) else 0 for i in range(N)))
