#include <stdio.h>

int main() {
    int target = 1000000;
    long max = 0L;
    int num = 0;
    for (int i = 1; i < target; i++) {
        int itr = 1;
        long x = (long) i;
        while (x != 1) {
            if (x % 2 == 0) {
                x /= 2;
            } else {
                x = 3*x + 1;
            }
            itr += 1;
        }
        if (itr > max) {
            max = itr;
            num = i;
        }
    }
    printf("Maximum Collatz Sequence for c[0] < %d: c[0] = %d | Length: %li",target,num,max);
    return 0;
}
