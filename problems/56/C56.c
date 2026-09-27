#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int* digits(int n) {
    int* num = calloc(4, sizeof(int));
    int l = 0;
    for (int j = 0; j < d; j++) {
        l = n % 10;
        num[j] = l;
        n = (n - l) / 10;
    }
    return num;
}

int arrSum(int* arr, int d) {
    int S = 0;
    for (int k = 0; k < d; k++) {
        S += arr[d];
    }
    return S;
}

/*int* exponential(int a, int b) {

    //int* numA = digits();
}*/

int main() {
    int A = 1;
    int B = 1;
    int p10 = 2;
    
}