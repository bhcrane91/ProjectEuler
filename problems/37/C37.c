#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int checkPrime(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    for (int i = 3; i < sqrt(n)+1; i+=2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int nextPrime(int n) {
    n++;
    while (checkPrime(n) == 0) n++;
    return n;
}

int main() {
    int truncatable = 11;
    int prime = nextPrime(10);
    int sum = 0;
    while (truncatable > 0) {
        int l = log10(prime);
        int trunc = 1;
        for (int i = 0; i < l; i++) {
            int buff = pow(10,l-i);
            int right = prime % buff;
            int left = (prime - right) / buff;
            if (checkPrime(left) == 0 || checkPrime(right) == 0) {
                trunc = 0;
            }
        }
        if (trunc == 1) {
            truncatable -= 1;
            sum += prime;
        }
        prime = nextPrime(prime);
    }
    printf("Sum of truncatable primes: %d\n",sum);
}