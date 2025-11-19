t = 3 
b = 7
d = 20
D = (float('inf'),0,0)

for i in range(1,d+1):
    x = (3 * i) // 7
    for j in range(1,x+1):
        # print(j,i)
        s = (t/b) - (j/i)
        if s < D[0] and s != 0:
            D = (s,j,i)
            print(D)

print(D)

## only search between the last found and 3/7

"""
check ipad notes
# 71 
# pivot = 3/7

pivot_n = 3
pivot_d = 7
d_cap = 1000000 
diff = float('inf')

curr_max_n = 1 # a
curr_max_d = 2 # b

n = 1 
d = 2

a / b < n / d < p_n / p_d

while d < d_cap:
    # find max fraction with curr d < pivot
    # a / b < n / d
    # a * d < n * b
    if curr_max_n * pivot_d < pivot_n * curr_max_d:
        n = (curr_max_d * pivot_n) // pivot_d
        for poss_n in range()

    d += 1


"""