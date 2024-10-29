import subprocess as sp 
from tabulate import tabulate as tb
import pandas as pd
import argparse as ap 

p = ap.ArgumentParser(prog="Project Euler Driver")

p.add_argument(
    "-l",
    type=str,
    default="npjrl",
    help="Run solution for each language key: j (Java), n (NumPy), p (Python), r (Rust), l (Julia)"
)

p.add_argument(
    "-n",
    type=int
)

a = p.parse_args()
langs = [c for c in a.l]
prob = a.n

print()
d = {c:{"out":"","time":""} for c in langs}

codepath = "/Users/bhc/vscode/ProjectEuler/problems/"
for lang in langs:
    if lang == "p":
        call = f"python3.11 {codepath}{prob}/P{prob}.py"
        d[lang]["lang"] = "python"
    elif lang == "j":
        # sp.run(f"javac {codepath}{prob}/J{prob}.java", shell=True)
        call = f"java {codepath}{prob}/J{prob}.java"
        d[lang]["lang"] = "java"
    elif lang == "r":
        sp.run(f"rustc {codepath}{prob}/R{prob}.rs", shell=True)
        sp.run(f"mv R{prob} {codepath}{prob}/", shell=True)
        call = f"{codepath}{prob}/R{prob} "
        d[lang]["lang"] = "rust"
    elif lang == "l":
        call = f"julia {codepath}{prob}/L{prob}.jl"
        d[lang]["lang"] = "julia"
    elif lang == "n": 
        call = f"python3.11 {codepath}{prob}/NP{prob}.py"
        d[lang]["lang"] = "numpy"

    print("CALL: ",call)
    s = sp.run(f"time {call}", shell=True, executable="/bin/zsh" , capture_output=True, cwd=f"{codepath}{prob}")
    d[lang]["out"] = s.stdout.decode("utf-8").replace("\n","")
    d[lang]["time"] = s.stderr.decode("utf-8").replace("\n","")

data = {
    "lang": [],
    "total": [],
    "cpu": [],
    "system": [],
    "user": []
}

for k,t in d.items():
    col = t["time"].split(" ")[:2:-2]
    row = t["time"].split(" ")[:1:-1][1::2]
    for i in range(len(col)):
        data[col[i]].append(row[i])
    data["lang"].append(t["lang"])
 
df = pd.DataFrame(data)
print()
print("Process Stats: ")
print()
print(tb(df, headers='keys', tablefmt='psql', showindex=False))
print()
print("Program Output:")
print()
for k,t in d.items():
    print(t['out'])
print()