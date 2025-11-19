#include <iostream>
#include <string>

int main() {
    int ans = 0;
    int arg = 1000;
    for (int i = 0; i < arg; i++) {
       ans += (i % 3 == 0 || i % 5 == 0) ? i : 0;
    }
    std::cout << "Sum of multiples of 3 or 5 below " << arg << ": " << ans << std::endl;
    return 0;
}