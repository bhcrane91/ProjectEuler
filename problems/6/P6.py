"""
Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.
"""
"""
Sum[k=1][n] k = (n * (n+1)) // 2
Sum[k=1][n] k**2 = (n * (n+1) * (2*n + 1)) // 6 
Sum[k=1][n] k**3 = (n**2 * (n+1)**2) // 4
"""

n = 100

sum_of_squares = (n * (n+1) * (2*n + 1)) // 6
square_of_sums = ((n * (n+1)) // 2) ** 2 

print(square_of_sums - sum_of_squares)