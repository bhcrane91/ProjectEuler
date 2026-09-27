import subprocess as sp 
from tabulate import tabulate as tb
import pandas as pd
import argparse as ap
import os

p = ap.ArgumentParser(prog="Project Euler Driver")

p.add_argument(
    "-l",
    type=str,
    default="npjrlcg",
    help="Run solution for each language key: j (Java), n (NumPy), p (Python), r (Rust), l (Julia), c (C), g (Go)"
)

p.add_argument(
    "-n",
    type=int,
    required=True,
    help="Problem number to run. Ex: Problem 1: '-n 1'"
)

available_keys = "npjrlcg"
keydict = {
    "p": "Python",
    "j":"Java",
    "n":"NumPy",
    "r":"Rust",
    "c":"C",
    "g":"Go",
    "l":"Julia"
}

argx = p.parse_args()
codepath = "/Users/bhc/vscode/ProjectEuler/problems/" + str(argx.n)
data = {
    lang: {
        "name": keydict[lang],
        "out": "",
        "time": "",
        "total": "",
        "cpu": "",
        "system": "",
        "user": "",
        "available": "",
        "error": ""        
    }
    for lang in argx.l if lang in available_keys
}

print(data)
