"""
2**15 = 32768 and the sum of the digits is 3+2+7+6+8=26
What is the sum of the digits of 2**1000?
"""
b = 2 
e = 1000
print(f"Sum of digits of {b}^{e}: {sum(int(i) for i in str(b**e))}")
