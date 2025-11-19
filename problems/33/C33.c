#include <stdio.h>

int gcd(int a, int b) {
    int temp = b;
    while (b != 0) {
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int a = 1;
    int b = 1; 

    for (int i = 1; i < 10; i++) {
        for (int j = 1; j < 10; j++) {
            int n = (i * 10) + j;
            for (int k = 9; k > i; k--) {
                int m = (j * 10) + k;
                if ((k * n) == (m * i)) {
                    a *= i;
                    b *= k;
                    // printf("%d %d\n",n,m);
                }
            }
        }
    }

    int g = gcd(a,b);
    while (g != 1) {
        a /= g;
        b /= g;
        g = gcd(a,b);
    }
    printf("%d\n",b);
}