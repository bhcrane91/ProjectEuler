#include <stdio.h>

int main() {
    int ans = 0;
    int arg = 1000;
    for (int i = 0; i < arg; i++) {
        ans += (i % 5 == 0 || i % 3 == 0) ? i : 0;
    }
    printf("Sum of multiples of 3 or 5 below %d: %d\n", arg, ans);
    return 0;
}
