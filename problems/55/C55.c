#include <stdio.h>

long rev(long n) {
    long r = 0;
    while (n > 0) {
        r = r * 10 + n % 10;
        n /= 10;
    }
    return r;
}

int main() {
    int lychrel = 0;
    long N = 10000;
    for (long i = 1; i < N; i++) {
        long n = i;
        int l = 1;
        for (int j = 0; j < 50; j++) {
            n += rev(n);
            if (n == rev(n)) {
                l = 0;
                break;
            }
        }
        lychrel += l;
    }
    printf("Lychrel Numbers below %lu: %d\n",N,lychrel);
}