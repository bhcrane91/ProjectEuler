import numpy as np

# Diagonal Sequence
# Binomial Coefficients
def binomial():
    pass

# (via) Pascals Triangle
def pascal(s):
    if s == 0:
        return 1
    pascal_row = np.zeros(2*s,dtype=np.int64)
    pascal_row[0] = 1
    for row in range(2*s):
        pascal_row = pascal_row + np.roll(pascal_row,1)
    return np.max(pascal_row)

t = 20
print(f"Paths in {t}x{t} square: {pascal(t)}")
        
