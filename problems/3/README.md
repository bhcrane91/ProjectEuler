### Problem Statement:
What is the largest prime factor of $600851475143$?

### Explanation:
The [Fundamental Theorm of Arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic) states that any integer $n\gt 1$ can be represented as a product of prime numbers
$$
n=2^{n_1}3^{n_2}5^{n_3}7^{n_4}\dots=\prod_{i=1}^{k}p_i^{n_i}
$$
where $p_i$ is the $i^{th}$ prime factor of $n$, and $p_1 \lt p_2 \lt \dots \lt p_k$.

We will use the above theorem to find the largest prime factors of $n$ via prime factorization. 

We will need to find the factors via trial division. While this is generally inefficient, we can improve our division sieve with a few considerations. 

1) All primes, $p \gt 2$, are odd.
2) The largest factor of any integer $n$ is $\sqrt{n}$.

From here, we can use the above Theorem to find the prime factors of $n$ from the ground up. 

#### Algorithm 

1) Start with $n$ as our number to factor, and $p$ as an empty list or array to store prime factors.
2) If $n \le 1$, $n$ is not prime and we can return an empty list or array. 
3) While $n$ is even or $(n\mod{2}) =0$.
    1) Add 2 to $p$.
    2) $n = n / 2$
4) $n$ is now odd. The largest possible factor left is $\sqrt{n}$. 
    1) For $i$ in $3\dots\sqrt{n}$. If $(n\mod{i})=0$:
        1) Add $i$ to $p$.
        2) $n=n/i$
        3) $i=i+2$. (We only care about odd numbers as factors/we know that even numbers wont be prime factors.)
5) If $n \gt 1$, add $n$ to $p$.
6) Return the last item in $p$.

Note: Alternatively you can just keep track of the only last found prime factor in $p$ because it will be the greatest by definition.

### Process Stats / Program Output

------------------------------------------------
| lang   |   total | cpu   | system   | user   |
|--------|---------|-------|----------|--------|
| java   |   0.132 | 117%  | 0.03s    | 0.12s  |
| rust   |   0.28  | 3%    | 0.00s    | 0.01s  |
| python |   0.038 | 96%   | 0.01s    | 0.03s  |
| numpy  |   0.265 | 452%  | 0.31s    | 0.89s  |
| julia  |   0.515 | 57%   | 0.07s    | 0.22s  |
------------------------------------------------

```Prime Factors of 600851475143: [71 839 1471 6857] | Largest -> 6857```