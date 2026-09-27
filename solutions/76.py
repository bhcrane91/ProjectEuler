import numpy as np

# dumb way of generating
def summations(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    sums = [np.ones(n,dtype=int)]
    total = 1
    print(f"Sum {total} : {sums[0]}")
    for i in range(2,n):
        for j in range(1,i+1):
            if n-i-j+1 == 1:
                break
            num = np.ones(n-i-j+1,dtype=int)
            num[0] = i
            num[1] = j
            nlist = num.tolist()
            if nlist not in sums:
                total += 1
                sums.append(num.tolist())
                print(f"Sum {total} : {num}")
            curr = np.argmax(num == 1)
            while np.sum(num == 1) > 1:
                num[curr] += num[curr+1]
                num[curr+1] = 0
                num = num[num != 0]
                nlist = num.tolist()
                if nlist not in sums:
                    sums.append(nlist)
                    total += 1
                    print(f"Sum {total} : {num}")
                curr += 1
        else:
            continue
    return sums
        
# Partition Numbers - 1
# Enlightened way if you know what partition function is 
def dumb(n):
    ns = np.arange(1,n,dtype=np.int64)
    ways = np.zeros(n+1,dtype=np.int64)
    ways[0] = 1
    for num in ns:
        for i in range(num,n+1):
            ways[i] += ways[i-num]
            # print(ways)
    return ways[n]
   
 
# for i in range(101):
#     print(i,len(summations(i+1)),dumb(i))

summations(10)
    
