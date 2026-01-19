import numpy as np

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_val = {}
for i, l in enumerate(letters):
    letter_val[l] = i+1
    
file = "words.txt"
with open(file,"r") as f:
    words = f.read()
    
words = [w[1:-1] for w in words.split(",")]

# t[n] = (n * (n + 1)) / 2
n = np.arange(1,27)
triangle_nums = (n*(n+1))//2

triangle_words = 0
for word in words:
    score = 0
    for letter in word:
        score += letter_val[letter]
    if score in triangle_nums:
        # print(word,score)
        triangle_words += 1
    
print(triangle_words)


