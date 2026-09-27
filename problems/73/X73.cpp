#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

int gcd(int a, int b) {
    int t;
    while (b != 0) {
        t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main() {
    int T = 12000;
    int S = 0;
    unordered_set<string> fractions;
    fractions.insert("1/3");
    fractions.insert("1/2");
    
    for (int d = 4; d <= T; d++) {

        int b = d / 3 + 1;
        int t = d / 2;

        for (int f = b; f <= t; f++) {

            int frac_n = f;
            int frac_d = d;
            int g = gcd(frac_n, frac_d);

            while (g != 1) {

                frac_n /= g;
                frac_d /= g;
                g = gcd(frac_n, frac_d);
            }

            string fraction = atoi
            if (fractions.find(fraction) != fractions.end()) {
                S++;
                fractions.insert(fraction);
            }
        }
    }
    cout << S << endl;
}