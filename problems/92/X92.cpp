#include <iostream>
using namespace std;

int main() {
    int q = 0;
    int S = 0;
    int l = 0;
    int s = 0;
    for (int i = 1; i < 10000000; i++) {
        s = i;
        while (s != 1 && s != 89) { 
            while (s > 0) {
                l = s % 10;
                q += l * l;
                s = (s - l) / 10;
            }
            s = q;
            q = 0;
        }
        S += (s == 89) ? 1 : 0;
    }
    cout << S << endl;
}