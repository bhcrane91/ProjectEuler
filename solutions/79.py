import numpy as np
import pylong as pl
from collections import Counter
import sys

with open("keylog.txt","r") as f:
    keys = f.read()
    
nums = {key: {"before": set(), "after": set()} for key, val in Counter(keys.replace("\n","")).items()}
nums2 = {key: set() for key, val in Counter(keys.replace("\n","")).items()}
keys = np.array(keys.split("\n"))
keys = np.unique(np.sort(keys)).tolist()
for key in keys:
    nums[key[0]]["after"].add(key[1])
    nums[key[0]]["after"].add(key[2])
    nums[key[1]]["before"].add(key[0])
    nums[key[1]]["after"].add(key[2])
    nums[key[2]]["before"].add(key[0])
    nums[key[2]]["before"].add(key[1])
    
passcode = ""
while nums != None:
    for key, val in nums.items():
        before = key["before"]
        after = key["after"]
    
    
    

