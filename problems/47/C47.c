#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int numDistinctPrimeFactors(int n) {
    int f = 0;
    if (n % 2 == 0) {
        f++;
        while (n % 2 == 0) n /= 2;
    }
    for (int i = 3; i < ((int)sqrt(n)) + 1; i+=2) {
        if (n % i == 0) {
            f++;
            while (n % i == 0) n /= i;
        }
    }
    if (n > 1) f++;
    return f;
}

int main() {
    int streak = 0;
    int distinct = 4;
    int n = 646;

    while (streak < distinct) {
        n++;
        int currPrimeFactors = numDistinctPrimeFactors(n);
        streak = (currPrimeFactors == distinct) ? (streak+1) : 0;
    }
    
    printf("Streak: %d -> %d\n",(n-distinct+1),n);
}