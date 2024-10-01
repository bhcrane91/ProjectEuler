import numpy as np 

f = [0,1]
target = 4000000
while f[-1] < target:
    f.append(f[-1]+f[-2])

f = np.array(f)
f = np.sum(f[f %2 == 0])

print("NumPy")
print(f"Sum of even-valued Fibonacci terms < {target}: {f}")
