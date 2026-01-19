#include <stdio.h>
#include <math.h>

int main() {
    int max = 0;
    int nmx = 0;
    int comparator[9] = {1,1,1,1,1,1,1,1,1};
    for (int n = 1; n < 6; n++) {
        int f = pow(10,n-1);
        int lb = (int) (9*f + (pow(10,n-1)-1)/9);
        int ub = (int) f*10;
        for (int i = lb; i < ub; i += 2) {
            int curr[9];
            int j = 0;
            
        }
    }
}