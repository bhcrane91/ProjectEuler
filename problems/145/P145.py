from tqdm import tqdm 

L = 10**9 

def reverse(n):
    s = 0 
    while n > 0:
        s *= 10
        s += (n%10)
        n //= 10 
    return s

# l = 1
# m = 2 
# p = 2 
R = 0
for p in tqdm(range(1,4)):
    for m in range(2,9,2):
        for l in range(1,10**p,2):
            num = m*10**p + l
            
            if not set(str(q)) - set("13579"):
                R += 2
            else:
                print(num,reverse(num),q)

 
print(R)

            
