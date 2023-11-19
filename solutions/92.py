import numpy as np
import pylong as pl
import threading
import os

def squareChain(num):
    while num != 89 and num != 1:
        digits = pl.digits_from_scalar(num)
        num = np.sum(digits**2)
    if num == 89:
        return 1
    return 0

def threadSC(start,end,result):
    sum = 0
    for i in range(start,end):
        sum += squareChain(i)
    result.append(sum)
    
def main(n):
    numbers = 10000000
    step = numbers // n 
    threads = []
    results = []
    
    for i in range(n):
        start = i * step 
        end = start + step 
        if i == (n-1):
            end = numbers
        thread = threading.Thread(target=threadSC, args=(start,end,results))
        threads.append(thread)
        thread.start()
        
    for t in threads:
        t.join()
        
    return sum(results)
            
if __name__ == "__main__":
    num = os.cpu_count()-1
    print(main(num))
