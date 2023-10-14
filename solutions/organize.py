import os
import sys 
import subprocess

files = [f for f in os.listdir(".") if ".py" in f and "organize" not in f]
print(files)

for f in files:
    os.mkdir(f[:-3])
    subprocess.run(f"mv {f} {f[:-3]}")
    subprocess.run(f"touch {f[:-3]}/readme.md")
    subprocess.run(f"echo 'projecteuler.net/problem=' >> {f[:-3]}/readme.md")

pyl = "pyl"
output = [o.replace(f".py:import {pyl}ong as pl","") for o in subprocess.check_output(f"grep -r {pyl}ong",shell=True,text=True).split("\n")][:-1]
for o in output:
    subprocess.run(f"cp {pyl}ong.py {o}")
    
print(output)
    


