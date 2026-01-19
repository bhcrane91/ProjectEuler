#include <stdio.h>
#include <math.h>

int main() {
    int target = 500;
    int tri = 1;
    int itr = 1;
    int div = 1;
    while (div < target) {
        itr++;
        tri += itr;
        div = 0;
        for (int i = 1; i < ((int)sqrt(tri)) + 1; i++) {
            if (tri % i == 0) {
                if (tri / i == i) {
                    div++;
                } else {
                    div += 2;
                }
            }
        }
    }
    printf("Triangle Number (%d): %d | Divisors: %d\n",itr,tri,div);
    return 0;
}