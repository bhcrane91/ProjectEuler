import numpy as np 
import pylong.pylong as pl

file = "txtF/sudoku.txt"

with open(file,"r") as f:
    games = f.read()

games = games.split("\n")
games = [g for g in games if "Grid" not in g]
print(len(games),9*50)
print(games[:9])