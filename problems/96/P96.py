import random 
from tqdm import tqdm 
from pprint import pprint

file = open("sudoku.txt","r").read().split("\n")
boards = []
grid = []
for line in file:
    if line.startswith("Grid"):
        if grid:
            boards.append(grid)
        grid = []
    else:
        grid.append([int(c) for c in line])
boards.append(grid)

for board in boards:
    r = len(board)
    c = set([len(board[c]) for c in range(r)])
    if (r,c) != (9,set([9])):
        print(r,c)
        pprint(board)

# print("all valid boards!")

# print(boards[0])
# print(boards[-1])

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    return None

def is_valid_move(board,row,col,num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False 
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col + j] == num:
                return False 
    return True

def solve(board):
    empty = find_empty(board)
    if empty is None:
        return True 
    row, col = empty
    nums = [i for i in range(1,10)]
    random.shuffle(nums)
    for n in nums:
        if is_valid_move(board,row,col,n):
            board[row][col] = n 
            if solve(board):
                return True
            board[row][col] = 0 
    return False        

# solved = []
s = 0
for board in boards: # tqdm(boards):
    grid = board 
    solve(grid)
    # solved.append(grid)
    for i in range(3):
        s += ((10**(2-i)) * grid[0][i])
print(s)