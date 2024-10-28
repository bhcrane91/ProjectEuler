with open("num.txt","r") as f:
    num = "".join([c for c in f.read() if c.isdigit()])

adj = 13 
max_prod = 0
max_strg = ""

places = (0,0)
for i in range(0,len(num)-adj):
    s = num[i:i+adj]
    p = 1 
    for j in s:
        p *= int(j)
    if p > max_prod:
        max_prod = p 
        max_strg = s 
        places = (i,i+adj)

print(max_prod,max_strg,places)

# split by 0?
# second approach remove all nums within 12 spaces of 0's then brute force