T = lambda n: (n * (n + 1)) // 2 
S = lambda n: n**2 
P = lambda n: (n * (3*n - 1)) // 2
X = lambda n: n * (2*n - 1)
H = lambda n: (n * (5*n - 3)) // 2
O = lambda n: n * (3*n - 2)
btw = lambda n, b: n >= b[0] and n < b[1]
N = 3
bounds = [10**N,10**(N+1)]
polygons = [T,S,P,X,H,O]
d = {}
for i, polygon in enumerate(polygons):
    d[i+3] = {"nums":[],"f":{},"b":{}}
    d[i+3]["nums"] = [polygon(j) for j in range(150) if btw(polygon(j),bounds)]
    fbd = {str(i):set() for i in range(10,100)}
    fbd.update({str(f"0{j}"):set() for j in range(10)})
    d[i+3]["f"] = fbd
    d[i+3]["b"] = fbd
    for num in d[i+3]["nums"]:
        s = str(num)
        d[i+3]["f"][s[:2]].add(num)
        d[i+3]["b"][s[2:]].add(num)