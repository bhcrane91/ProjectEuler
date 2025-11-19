import numpy as np

with open('matrix.txt','r') as f:
    matrix = f.read() 
    
matrix = np.array([row.split(",") for row in matrix.split("\n")][:-1]).astype(int)
# print(len(matrix),len(matrix[0]))
# print(matrix)

mat = np.array([row[:4] for row in matrix[:4]])
print(mat)

def to_pyramid(matrix):
    s = len(matrix)
    pyramid = []
    matmax = np.max(matrix)
    
    for row in range(s):
        curr = np.ones(s,dtype=int) * matmax
        for col in range(row+1):
            curr[col] = matrix[row-col][col]
        pyramid.append(curr)
        
    for i in range(s-1,0,-1):
        curr = np.ones(s,dtype=int) * matmax
        for j in range(i):
            curr[j] = matrix[s-j-1][s-i+j]
        pyramid.append(curr)
            
    return np.array(pyramid)

def min_path_sum(pyr):
  top = pyr[0:len(pyr[0])]
  bot = pyr[len(pyr[0])-1:]
  
  for row in range(1,len(top)):
    left = np.roll(top[row-1],1) + top[row]
    right = top[row-1] + top[row]
    top[row] = np.minimum(left,right)
  
  
  for row in range(len(bot)-1):
    right = np.roll(bot[row],-1)+bot[row+1]
    left = (bot[row]+bot[row+1])
    bot[row+1] = np.minimum(left,right)
  
  print(f"Minimum Path Sum = {pyr[len(pyr)-1][0]}")
  
pyr = to_pyramid(matrix)
print(pyr)
min_path_sum(pyr)
    

    
