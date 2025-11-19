#include <stdio.h>
#include <stdlib.h>

int* factorials() {
    int* f = calloc(10,sizeof(int));
    f[0] = 1;
    for (int i = 1; i < 10; i++) {
        f[i] = f[i-1] * i;
    }
    return f;
}

int main() {
    int* facts = factorials();
    int df = 0;
    int l = 10;
    int S = 0;
    int* digFactorials = calloc(l,sizeof(int));
    printf("Digit Factorial Sum Numbers: ");
    for (int i = 3; i < 1000000; i++) {
        int n = i;
        int s = 0;
        while (n > 0) {
            int l = n % 10;
            s += facts[l];
            n = (n - l) / 10;
        }
        // printf("%d %d\n",i,s);
        if (s == i) {
            if (df+1 == l) {
                l += 10;
                digFactorials = realloc(digFactorials, l*sizeof(int));
            }
            digFactorials[df] = i;
            df++;
            S += i;
            printf("%d ",i);
        }
    }
    printf("-> Sum: %d\n",S);
}