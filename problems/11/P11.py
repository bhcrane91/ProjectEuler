def diagonals(matrix):
    if not matrix:
        return [], []
    
    rows, cols = len(matrix), len(matrix[0])
    main_diagonals = {}
    anti_diagonals = {}
    
    # Main diagonals (i - j is constant)
    for i in range(rows):
        for j in range(cols):
            key = i - j
            if key not in main_diagonals:
                main_diagonals[key] = []
            main_diagonals[key].append(matrix[i][j])
    
    # Anti-diagonals (i + j is constant)
    for i in range(rows):
        for j in range(cols):
            key = i + j
            if key not in anti_diagonals:
                anti_diagonals[key] = []
            anti_diagonals[key].append(matrix[i][j])
    
    # Convert to list of lists
    # main_diagonal_list = [main_diagonals[key] for key in sorted(main_diagonals.keys())]
    # anti_diagonal_list = [anti_diagonals[key] for key in sorted(anti_diagonals.keys())]
    # return main_diagonal_list, anti_diagonal_list

    return [main_diagonals[key] for key in sorted(main_diagonals.keys())] + [anti_diagonals[key] for key in sorted(anti_diagonals.keys())]

def straights(matrix): 
    rows = [row for row in matrix]
    cols = [matrix[j][i] for i in range(len(matrix[0])) for j in range(len(matrix))]
    cols = [cols[i*len(matrix):(i+1)*len(matrix)] for i in range(len(matrix[0]))]
    return rows + cols


def subarr(arrs, l):
    sub = []
    for arr in arrs:
        curr_len = len(arr)
        if curr_len > l:
            for i in range(curr_len-l+1):
                sub.append(arr[i:l+i])
        else:
            sub.append(arr)
    return sub


# ---- Answer ----

L = 4

with open("nums.txt","r") as f:
    nums = [l.split(" ") for l in f.read().split("\n")]

directions = diagonals(nums) + straights(nums) 
sequences = subarr(directions, l=L)
maxProd = -1 
arr = []

for s in sequences:
    p = 1
    for n in s:
        p *= int(n)
    if p > maxProd:
        maxProd = p
        arr = s 

print(maxProd, arr)