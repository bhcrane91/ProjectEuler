### Problem Statement:

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

### Explanation:

All we have to do is loop over the numbers below n = 1000 and add
them to our sum if they are divisible by d = {3,5}. 

#### In math notation:

Let $d$ be a set of divisors, and
$$
f(n) =
\begin{cases} 
n & \text{if } (n\mod m)=0, \forall m \in d
 \\
0 & otherwise
\end{cases}
$$
Then our sum, $S(N)$ is simply
$$
S(N) = \sum_{n=1}^{N} f(n)
$$


### Answer / Output:

#### Process Stats: 

| lang   |   total  | cpu   | system   | user   |
|--------|----------|-------|----------|--------|
| java   |   0.106s | 105%  | 0.02s    | 0.09s  |
| rust   |   0.264s | 3%    | 0.00s    | 0.01s  |
| python |   0.042s | 94%   | 0.01s    | 0.03s  |
| numpy  |   0.284s | 429%  | 0.31s    | 0.91s  |
| julia  |   0.503s | 57%   | 0.07s    | 0.22s  |

#### Programs Output:

```Prime Factors of 600851475143: [71 839 1471 6857] | Largest -> 6857```