int* distinctPrimeFactors(int n, int* c) {
    int f = 10;
    int* factors = (int*) calloc(f,sizeof(int));
    if (n % 2 == 0) {
        factors[(*c)++] = 2;
        while (n % 2 == 0) n /= 2;
    }
    for (int i = 3; i < ((int)sqrt(n)) + 1; i++) {
        if (n % i == 0) {
            factors[(*c)++] = i;
            n /= i;
        }
        if ((*c) == f) {
            f *= 2;
            factors = realloc(factors, f);
        }
    }
    if (n > 0) factors[(*c)++] = n;
    return factors;
}