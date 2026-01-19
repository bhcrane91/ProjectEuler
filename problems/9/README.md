### Problem Statement 

A Pythagorean triplet is a set of three natural numbers for which ,
$$
a\lt b \lt c,\quad a^2 + b^2 = c^2
$$
For example, 
$$
3^2 + 4^2 = 9 + 16 = 25 = 5^2
$$.
There exists exactly one Pythagorean triplet for which 
$$
a + b + c = 1000
$$.
Find the product abc.

### Explanation:
We can use the sum of terms to limit our search space for this problem. To satisfy both the sum of terms and the Pythagorean Theorem, we know all three terms need to have the same order of magnitude, here they will all be ~$10^2$. Therefore we will search through these terms and generate triples using our expression for the sum of terms. Since we need at least three terms of magnitude ~$10^2$ and we need there sum to be $1000$, we can choose
$$
a = 100 \\
b = a+1 = 101 \\
c = 1000-a-b = 1000-100-101 = 799
$$.
From here we just slowly increment $a,b$, calculate $c$ and check if it will satisfy the Pythagorean triple. As soon as we find one that works we stop since we are given the fact there will only be one for this situation. 

### Process Stats: 


| lang   | key   | total   | cpu   | system   | user   |
|--------|-------|---------|-------|----------|--------|
| numpy  | N     | 0.137s  | 612%  | 0.23s    | 0.60s  |
| python | P     | 0.086s  | 98%   | 0.01s    | 0.08s  |
| java   | J     | 0.465s  | 249%  | 0.13s    | 1.03s  |
| rust   | R     | 0.273s  | 1%    | 0.00s    | 0.00s  |
| julia  | L     | 0.495s  | 54%   | 0.06s    | 0.21s  |
| c      | C     | 0.232s  | 0%    | 0.00s    | 0.00s  |


### Program Output:

```
N -> Triple: (200,375,425) | Product: 31875000
P -> Triple: (200,375,425) | Product: 31875000
J -> Triple: (200,375,425) | Product: 31875000
R -> Triple: (200,375,425) | Product: 31875000
L -> Triple: (200,375,425) | Product: 31875000
C -> Triple: (200,375,425) | Product: 31875000
```