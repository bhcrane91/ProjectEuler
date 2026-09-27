#include <iostream>
using namespace std;

int main() {
    int t = 3;
    int b = 7;
    int l = 1000000;
    double c = (double) t / b;
    double D = 1e200;
    int n = 0;
    int d = 0;
    for (int i = l - 1; i > 0; i--) {
        int q = (t * i) / b;
        double s = c - ((double)q/i);
        if (s < D && s != 0) {
            D = s;
            n = q;
            d = i;
        }
    }
    cout << n << " " << d << endl;
}