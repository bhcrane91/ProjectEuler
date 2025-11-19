#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int numProdDigits(int n) {
    int digits = 0;
    for (int i = 1; i <= n; i++) {
        digits += (int) log10(i) + 1;
    }
    return digits;
}

int* factorial(int num, int num_digits) {
    int* arr = calloc(num_digits,sizeof(int));
    arr[0] = 1;
    for (int f = 2; f <= num; f++) {
        int rollover = 0;
        int curr = 0;
        for (int i = 0; i < num_digits; i++) {
            curr = arr[i] * f + rollover;
            arr[i] = curr % 10;
            rollover = curr / 10;
        }
    } 
    return arr;
}

int main() {
    int num = 100;
    int num_digits = numProdDigits(num);
    int* fact = factorial(num, num_digits);

    int s = 0;
    char* strnum = calloc(num_digits,sizeof(char));
    for (int i = 0; i < num_digits; i++) {
        s += fact[i];
    }
    printf("Sum of digits of %d! = %d\n",num,s);
}