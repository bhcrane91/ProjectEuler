#include <stdio.h>

// Function to find the Greatest Common Divisor (GCD) using Euclidean algorithm
int gcd(int a, int b) {
    int temp = b;
    while (b != 0) {
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Function to find the Least Common Multiple (LCM) of two numbers
int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    int ans = 1;
    for (int i = 1; i < 20; i++) {
        ans = lcm(i,ans);
    }
    printf("%d\n", ans);
    return 0;
}
