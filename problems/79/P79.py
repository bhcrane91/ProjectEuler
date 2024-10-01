import numpy as np
import pylong as pl
from collections import Counter
import sys

with open("txtF/keylog.txt","r") as f:
    keys = list(set(f.read().split("\n")))

keys.sort()
print(keys)
"""
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
"""

"""
Ans:
sort unique attempts
=> [
    '129', '160', '162', '168', '180', 
    '289', '290', '316', '318', '319', 
    '362', '368', '380', '389', '620', 
    '629', '680', '689', '690', '710', 
    '716', '718', '719', '720', '728', 
    '729', '731', '736', '760', '762', 
    '769', '790', '890'
]

start 

pw = '129'
'129' + '289' => 1289

=> [
    '160', '162', '168', '180', 
    '290', '316', '318', '319', 
    '362', '368', '380', '389', '620', 
    '629', '680', '689', '690', '710', 
    '716', '718', '719', '720', '728', 
    '729', '731', '736', '760', '762', 
    '769', '790', '890'
]

1289 + 890 => 12890

=> [
    '160', '162', '168', '180', 
    '290', '316', '318', '319', 
    '362', '368', '380', '389', '620', 
    '629', '680', '689', '690', '710', 
    '716', '718', '719', '720', '728', 
    '729', '731', '736', '760', '762', 
    '769', '790'
]

=> 12890 + 162 => 162890

=> [
    '160', '168', '180', 
    '290', '316', '318', '319', 
    '362', '368', '380', '389', '620', 
    '629', '680', '689', '690', '710', 
    '716', '718', '719', '720', '728', 
    '729', '731', '736', '760', '762', 
    '769', '790'
]

=> 162890 + 731 => 73162890

all others confirm this order and can be removed


"""
# 73162890
    
    

