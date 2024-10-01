import numpy as np
import sys 

"""
https://www.cs.ubc.ca/~liorma/cpsc320/files/closest-points.pdf
"""

def s(n):
    n *= 2
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
    return min
    
def broad(P):
    # Calculate pairwise distances using NumPy broadcasting
    differences = P[:, np.newaxis, :] - P
    # print(differences)
    pairwise_distances = np.sqrt(np.sum(differences**2, axis=2))
    # print(pairwise_distances)

    # Set the diagonal elements (i.e., distances between the same points) to zero
    np.fill_diagonal(pairwise_distances, np.iinfo(np.int64).max)
    # print(pairwise_distances)
    # print(np.min(pairwise_distances))
    return np.min(pairwise_distances), np.sort(P)

"""
Algorithm MinDist(P):
  if |P| ≤ 3 then
    try all pairs to find MinDist
    sort P
    return MinDist and sorted P
  else
    find x median of the points
    split P into L and R of about the same size using x
    
    δleft, pointsLeft = MinDist(L)
    δright, pointsRight = MinDist(R)
    
    P = pointsLeft + pointsRight
    δ = min {δleft, δright}

    BL = points in L within δ of x median
    BR = points in R within δ of x median

    for p ∈ BL do
       binary search for highest q ∈ BR in a δ × 2δ box of p
       compare at most 6 points starting with q to p
    
    return δ and P
"""
n = 14
P = s(n)
print(broad(P))


def min_dist(P):
    if len(P) <= 10:
        return broad(P)
    else:
        x_median = np.median(P[:, 0])
        L = P[P[:, 0] < x_median]
        R = P[P[:, 0] >= x_median]
        dL, pL = min_dist(L)
        dR, pR = min_dist(R)

        P = np.concatenate((pL, pR), axis=0)
        d = min(dL, dR)

        BL = L[np.abs(x_median - L[:, 0]) <= d]
        BR = R[np.abs(x_median - R[:, 0]) <= d]

        for p in BL:
            


# min_dist(14)

"""
method = int(sys.argv[1])
points = int(sys.argv[2])
if method == 1:
    d(points)
elif method == 2:
    broad(points)
"""
