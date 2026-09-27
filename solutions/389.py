import numpy as np 

def roll_die(rolls,sides):
    rolled = np.random.randint(low=1,high=sides+1,size=rolls)
    print(rolled)

# T = X_1 + X_2 + ... + X_N
# Var(T) = Var(X_1 + X_2 + ... + X_N) = Sum^{N}_{i=1} Var(X_i) = N * Var(X_i)
# Var(X_i) = (n**2 - 1) / 12
# Var(T) = N * (n**2 - 1)/12

sides = [4,6,8,12,20]
rolls = 1
for side in sides:
   outcomes = np.arange(1,side+1,dtype=int)
   expected = np.sum(outcomes) / side
   rolled = np.random.randint(low=1,high=side+1,size=rolls)
   variance = rolls * (np.sum((outcomes - expected)**2) / side)
   rolls = np.sum(rolled)
   print(variance)
    
