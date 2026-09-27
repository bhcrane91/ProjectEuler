import numpy as np

"""
side = 5
grid = np.zeros((side,side),dtype=int)
row_start = 0
row_finis = side-1
col_start = side-1
col_finis = 0
i = side**2
while i > 0:
    
    top = np.arange(col_finis,col_start+1)[::-1]
    print(top)
    for col in top:
        grid[row_start][col] = i
        i -= 1
    row_start += 1 
    
    left = np.arange(row_start,row_finis+1)
    print(left)
    for row in left:
        print(row)
        grid[row][col_finis] = i
        i -= 1 
    col_start += 1
    
    bottom = np.arange(col_finis,col_start)
    print(bottom)
    for col in bottom:
        print(col)
        grid[row_finis][col] = i 
        i -= 1
    row_finis -= 1
    
    right = np.arange(row_start,row_finis)[::-1]
    for row in right:
        print(row)
        grid[row][col_finis] = i
        i -= 1
    col_finis -= 1
    
print(grid)
"""

side = 1001
top = side**2
corners = 2*side-1
sum = top
print(top)
while top != 1:
    for i in range(4):
        top -= (side-1)
        sum += top 
        print(top)
    side -= 2
print(sum)
        
    
    
    
    
