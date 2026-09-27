#include <stdio.h>
#include <math.h>

int checkPrime(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    for (int i = 3; i < ((int)sqrt(n))+1; i+=2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int N = 7; 
    int S = 0; 
    int n = 10;
    for (int i = 1; i < N; i++) {
        for (int j = n/10; j < n; j++) {
            int tmp = j;
            int ts = 0;
            for (int k = 0; k < i; k++) {
                ts += checkPrime(tmp);
                tmp = ((n/10) * (tmp % 10)) + ((tmp - (tmp % 10)) / 10);
            }
            
            if (ts == i) {
                S++;
            }
        }
        n *= 10;
    }
    printf("Number of Circular Primes below %d: %d",(n/10),S);
}