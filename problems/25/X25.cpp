#include <iostream>
using namespace std;

int main() {
    double a = 1;
    double b = 1;
    int i = 1;
    double x = a + b;
    int j = 2; 
    int n = 1000; 
    while (i < n) {
        j += 1; 
        x = a + b;
        int e = ((int) log10(x)) - ((int) log10(b));
        i += e;
        a = b;
        b = x;
        if (e > 0) {
            a /= 10;
            b /= 10;
        }
    }
    cout << "First Fibonacci term with " << n << " digits: F_n -> n = " << j << endl;
}