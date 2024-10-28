def product(digits):
    bot = 10**(digits-1)
    top = 10**digits
    max = (0,0,0)
    for i in range(top,bot-1,-1):
        for j in range(top,bot-1,-1):
            p = i*j
            if p > max[0] and str(p) == str(p)[::-1]:
                max = (p,i,j)
    return max

ans = product(3)
print(f"Python | Max: {ans[0]} | Factors: ({ans[1]},{ans[2]})")
