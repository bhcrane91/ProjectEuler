with open("triangle.txt","r") as f:
    triangle = [[int(k) for k in row.split(" ")]  for row in f.read().split("\n")][::-1]

rowlen = len(triangle[0])
trilen = len(triangle)
for t in range(trilen):
    triangle[t] = triangle[t] + [0]*(rowlen-len(triangle[t]))

for row in triangle:
    print("{",",".join([str(s) for s in row]),"},")

def roll(arr,step):
    sign = 1 if step > 0 else -1
    l = len(arr)
    step %= (l*sign)
    if step == 0:
        return arr
    return arr[-step:] + arr[:((l*sign)-step)]

def arrmax(a,b):
    if len(a) != len(b):
        print("Needs to be the same length")
        return 
    return [max(a[i],b[i]) for i in range(len(a))]

def idxsum(a,b):
    if len(a) != len(b):
        print("Needs to be the same length")
        return 
    return [a[i]+b[i] for i in range(len(a))]

for row in range(trilen-1):
    right = idxsum(roll(triangle[row],-1),triangle[row+1])
    left = idxsum(triangle[row],triangle[row+1])
    right[trilen-row-1:] = [0]*len(right[trilen-row-1:])
    left[trilen-row-1:] = [0]*len(left[trilen-row-1:]) 
    triangle[row+1] = arrmax(left,right)

print(triangle[trilen-1][0])
    