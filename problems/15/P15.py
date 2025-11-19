def pascal(s):
    pascal_row = [0]*(2*s)
    pascal_row[0] = 1
    for row in range(0,2*s):
        for i in range(0,2*s):
            pascal_row[i] += pascal_row[(i+1)%(2*s)]
    return pascal_row

t = 20
tri = pascal(t)
print(f"Paths in {t}x{t} square: {max(tri)}")
        
