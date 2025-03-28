### Problem Statement:
The sum of the squares of the first ten natural numbers is,
$$1^2 + 2^2 + ... + 10^2 = 385.$$
The square of the sum of the first ten natural numbers is,
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

### Explanation:
There are summation formulas for the sum of a series of integers. 
$$
\sum_{i=1}^{n}n=\frac{n(n+1)}{2} = K(n)
$$
$$
\sum_{i=1}^{n}n^2=\frac{n(n+1)(2n+1)}{6} = Q(n)
$$

We want to find the difference, $D(n)$, between the sum of the squares and the sqaure of the sum of the integers of $1 \dots n$. 

$$
D(n) = Q - K^2 \\
= \sum_{i=1}^{n}n^2 - (\sum_{i=1}^{n}n)^2 \\
= \frac{n(n+1)(2n+1)}{6} - (\frac{n(n+1)}{2})^2 \\
$$

We just need to plug in $n$ and we have the answer.
$$
D(100)=25164150
$$

### Process Stats / Program Output

--------------------------------------------------------
| lang   | key   | total   | cpu   | system   | user   |
|--------|-------|---------|-------|----------|--------|
| java   | J     | 0.457s  | 233%  | 0.11s    | 0.96s  |
| julia  | L     | 0.510s  | 54%   | 0.07s    | 0.21s  |
| rust   | R     | 0.248s  | 0%    | 0.00s    | 0.00s  |
| python | P     | 0.029s  | 93%   | 0.01s    | 0.02s  |
| numpy  | N     | 0.132s  | 585%  | 0.22s    | 0.56s  |
| c      | C     | 0.226s  | 0%    | 0.00s    | 0.00s  |
--------------------------------------------------------

Program Output:

Ans -> 25164150
