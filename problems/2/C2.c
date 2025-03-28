#include <stdio.h>

int main() {
    int a = 1; 
    int b = 2;
    int tmp = 0;
    int sum = 0; 
    int target = 4000000;
    while (b < target) {
        if (b % 2 == 0) sum += b;
        tmp = b; 
        b += a;
        a = tmp;
    }
    printf("C: Sum of even-valued Fibonacci terms < %d: %d\n", target, sum);
    return 0;
}