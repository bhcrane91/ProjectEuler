import subprocess as sp 
import sys
from tabulate import tabulate as tb
import pandas as pd


s = sp.run(f"zsh run_prob.sh {sys.argv[1]}", shell=True, capture_output=True)
q = str(s.stderr).split("\\n")

data = {
    "lang": ["java","rust","python","numpy","julia"],
    "total": [],
    "cpu": [],
    "system": [],
    "user": []
}

for k in q:
    col = k.split(" ")[:2:-2]
    row = k.split(" ")[:1:-1][1::2]
    for i in range(len(col)):
        data[col[i]].append(row[i])

df = pd.DataFrame(data)
print()
print("Process Stats: ")
print()
print(tb(df, headers='keys', tablefmt='psql', showindex=False))
print()
print("Program Output:")
print()
for line in str(s.stdout).split("\\n")[4:-1]:
    print(line)
print()