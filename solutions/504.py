"""
Let ABCD be a quadrilateral whose vertices are lattice points lying on the 
coordinate axes as follows:
A -> (a,0)
B -> (0,b)
C -> (-c,0)
D -> (0,-d)

where 1 <= a,b,c,d <= m and a,b,c,d,m are integers.

It can be shown that for m=4 there are exactly 256 valid ways to construct ABCD.
Of these 256 quadrilaterals, 42 of them STRICTLY contain a square number of 
lattice points.

How many quadrilaterals ABCD strictly contain a square number of lattice points for m = 100?
"""
from itertools import permutations
import math 

def generate_pairs(m):
    pairs = []
    for a in range(m):
        for b in range(m):
            for c in range(m):
                for d in range(m):
                    pairs.append([a+1,b+1,c+1,d+1])
    return pairs 

def triangle(a,b):
    pts = 0
    i = 1
    f = int(b/a*i)
    print(f)
    while f != 1 and i < a:
        pts += b-f-1
        print(i,b-int(b/a*i),pts)
        i += 1
    return int(pts)

def num_points(pts):
    # pts = [a,b,c,d]
    return (
        triangle(pts[0],pts[1]) + # BA
        triangle(pts[0],pts[3]) + # DA
        triangle(pts[2],pts[1]) + # BC
        triangle(pts[2],pts[3]) + # DC
        sum([pt-1 for pt in pts]) + 
        1
    )

def quad_is_square(pts):
    n = math.sqrt(num_points(pts))
    return n == int(n)

def find_squares(pairs):
    total = 0
    for pair in pairs:
        total += quad_is_square(pair)
    return total 

"""
n = 4
pairs = generate_pairs(n)
squrs = find_squares(pairs)
print(n,len(pairs),squrs)
"""
from tqdm import tqdm
top = 100
print(triangle(4,7))
print("---")
print(triangle(7,4))
"""
for i in range(1,top):
    for j in range(1,top):
        a = triangle(i,j)
        b = triangle(j,i)
        if a != b:
            print(i,j,a,b)
"""
# build dict of keys "a b" = triangle(a,b)
# only need to calculte each triangle once
# for quadrilateral 