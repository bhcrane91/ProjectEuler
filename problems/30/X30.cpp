#include <iostream>
using namespace std;

int main() {
    int s = 2; 
    int ans = 0;
    int n = 5; 
    while (s < n+1) {
        for (int i = ((int) pow(10,s)); i < ((int) pow(10,s+1)); i++) {
            int j = i;
            int sj = 0;
            while (j > 0) {
                int l = j % 10;
                sj += ((int) pow(l,5));
                j = (j - l) / 10;
            }
            if (sj == i) {
                ans += sj;
            }
        }
        s++;
    }
    cout << ans << endl;
}