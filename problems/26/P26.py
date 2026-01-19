import math 

def long_divide(a,b):
    remainders = set()
    rem = a % b
    digits = ""
    
    while rem != 0 and rem not in remainders:
        remainders.add(rem)
        
        rem *= 10
        digits += str(rem // b)
        rem = rem % b
        # print(rem,digits)
    # print(rem,digits,remainders)
    return rem, digits

# long_divide(1,50)

rem = ""
lmx = 0 
for i in range(1,1000):
    crm, cyc = long_divide(1,i)
    if len(cyc) > lmx:
        lmx = len(cyc)
        rem = crm 
        print(i,len(cyc))