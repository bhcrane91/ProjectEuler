import numpy as np

with open("num.txt","r") as f:
    number = f.read()

num = [int(c) for c in number if c != "\n" and c != " "]
num = np.array(num,dtype=np.int64)
adj = 13
scores = []
for i in range(len(num)-adj+1):
    sub = num[i:i+adj]
    # print(len(sub))
    scores.append(np.prod(sub))
    

print(np.max(np.array(scores)))