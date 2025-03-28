import numpy as np

with open("base_exp.txt", "r") as f:
    data = np.array([int(num) for line in f.read().split("\n") for num in line.split(",")])

data = data.reshape((len(data)//2,2))

data = data[:,1] * np.log(data[:,0])
maxVal = np.max(data)
maxIdx = np.argmax(data)

print(f"N: Answer -> Max Value: {maxVal} | Line Number: {maxIdx+1}")


