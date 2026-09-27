#include <stdio.h>

int main() {
    int bouncy = 0;
    int total = 99;
    while (bouncy*100 < total*99) {
        total++;
        int n = total;
        int a = n % 10;
        int b = ((n % 100) - a) / 10;
        int k = b - a;
        /// printf("%d %d %d %d\n",n,a,b,k);
        while (n > 10) {
            a = n % 10;
            b = ((n % 100) - a) / 10;
            // printf("\t %d %d %d %d\n",n,a,b,k);
            if ((b-a) * k < 0) {
                bouncy++;
                break;
            }
            n = (n - a) / 10;
            k = b - a;
        }
        if (total == 1587000) printf("%f %d %d\n",((double)bouncy/total), total, bouncy);
    }
    printf("%f %d %d\n",((double)bouncy/total), total, bouncy);
}

