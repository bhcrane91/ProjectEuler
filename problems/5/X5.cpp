#include <iostream>

int lcm(int a, int b);
int gcd(int a, int b);

int main() {
    int ans = 1;
    int n = 20;
    for (int i = 1; i < n; i++) ans = lcm(i,ans);
    std::cout << "LCM of numbers 1 to " << n << ": " << ans << std::endl;
}

int gcd(int a, int b) {
    int t = b;
    while (b != 0) {
        t = b; 
        b = a % b;
        a = t;
    }
    return a;
}

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}