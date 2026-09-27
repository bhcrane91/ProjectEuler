import numpy as np

with open("triangle.txt","r") as f:
    file = f.read()
    
triangle = [row.split(" ") for row in file.split("\n")][:-1]
last = len(triangle)
tri = np.zeros((last,last),dtype=int)
for t in range(last):
    tri[t][0:t+1] = triangle[t]

tri = tri[::-1]

for row in range(len(tri)-1):
    right = np.roll(tri[row],-1)+tri[row+1]
    left = (tri[row]+tri[row+1])
    right[len(tri)-row-1:] = 0
    left[len(tri)-row-1:] = 0
    tri[row+1] = np.maximum(left,right)
    
print(tri)
