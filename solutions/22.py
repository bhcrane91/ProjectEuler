import numpy as np

with open("names.txt","r") as f:
    names = f.read()
    names = names.split(",")
    names = [name[1:-1] for name in names]

print(names)

lets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dctsrt = {}
scores = {}
for i in range(len(lets)):
    dctsrt[lets[i]] = []
    scores[lets[i]] = i+1
    
for name in names:
    dctsrt[name[0]].append(name)
    
names = []
for key, val in dctsrt.items():
    print(val)
    names += sorted(val)
    
total = 0
for idx, name in enumerate(names):
    name_score = 0
    for char in name:
        name_score += scores[char]
    name_score *= (idx + 1)
    if name == 'COLIN':
        print(name, name_score)
    total += name_score

print(total)
    
        
    
    


    

    
    

