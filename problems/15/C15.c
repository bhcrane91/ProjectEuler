#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

long* pascal(int n) {
    long* pascalRow = malloc(2*n*sizeof(long));
    pascalRow[0] = 1L;
    for (int row = 0; row < 2*n; row++) {
        for (int i = 0; i < 2*n; i++) {
            pascalRow[i] += pascalRow[(i+1)%(2*n)];
        }
    }
    return pascalRow;
}

int main() {
    int target = 20;
    long* triangle = pascal(target);
    long max = 0;
    for (int i = 0; i < 2*target; i++) {
        if (triangle[i] > max) {
            max = triangle[i];
        }
    }
    printf("Paths in %dx%d square: %li\n",target,target,max);
}