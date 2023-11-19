import numpy as np
import sys 

def s(n):
    sn = np.zeros(n,dtype=int)
    sn[0] = 290797
    for i in range(1,n):
        sn[i] = (sn[i-1]**2) % 50515093
    return sn.reshape(len(sn)//2,2)  

def d(k):
    sn = s(k*2)
    min = np.iinfo(np.int64).max
    for i in range(len(sn)-1):
        for j in range(i+1,len(sn)):
            dist = np.sqrt(np.sum((sn[i] - sn[j])**2))
            if dist < min:
                min = dist
    print(min)
    
def broad(k):
    sn = s(k*2)
    # Calculate pairwise distances using NumPy broadcasting
    differences = sn[:, np.newaxis, :] - sn
    # print(differences)
    pairwise_distances = np.sqrt(np.sum(differences**2, axis=2))
    # print(pairwise_distances)

    # Set the diagonal elements (i.e., distances between the same points) to zero
    np.fill_diagonal(pairwise_distances, np.iinfo(np.int64).max)
    # print(pairwise_distances)
    print(np.min(pairwise_distances))


method = int(sys.argv[1])
points = int(sys.argv[2])
if method == 1:
    d(points)
elif method == 2:
    broad(points)