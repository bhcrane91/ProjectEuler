#include <stdio.h>
#include <math.h>

int checkPrime(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    for (int i = 3; i < sqrt(n)+1; i+=2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int s = 4; 
    int n = 9;
    int corners = 5;
    int primes = 3;
    while (((double)primes/corners) > 0.1) {
        for (int i = 0; i < 4; i++) {
            n += s;
            if (checkPrime(n)) primes++;
            corners++;
        }
        s += 2;
    }
    printf("%d %d %d %f",(s-1),primes,corners,((float)primes/corners));
}