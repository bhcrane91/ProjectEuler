#include <iostream> 

int main() {
    int k = 1000;
    int l = 200;
    for (int a = l; a < k; a++) {
        for (int b = a+1; b < k-a; b++) {
            int c = 1000 - a - b;
            if (a*a+b*b == c*c) {
                std::cout << "Triple: (" << a << "," << b << "," << c << ") | Product: " << a*b*c << std::endl;
                return 1;
            }
        }
    }
    return 0;
}