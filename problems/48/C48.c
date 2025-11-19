#include <stdio.h>

int modExp(int a, int b, long d) {
    if (b == 0) return 1;
    long s = 1;
    for(int i = 0; i < b; i++) {
        s = (s * a) % d;
    }
    return s;
}

int main() {
    long sum = 0;
    long d = 100000000000;
    for (int i = 1; i < 1001; i++) {
        sum += modExp(i,i,d);
    }
    printf("%lu\n",(sum%d));
}