#include <iostream>
#include <vector>
#include <set>
using namespace std;

set<int> divisors(int n) {
    set<int> divs;
    divs.insert(1);
    for (int i = 2; i < (int)sqrt(n); i++) {
        if (n % i == 0) {
            divs.insert(i);
            divs.insert(n/i);
        }
    }
    return divs;
}

int setSum(const set<int>& s) {
    int S = 0;
    for (int i: s) S += i;
    return S;
}

int main() {
    set<int> amicable;
    for (int i = 1; i < 10000; i++) {
        if (amicable.find(i) == amicable.end()) {
            int a = setSum(divisors(i));
            int b = setSum(divisors(a));
            if (b == i && a != b) {
                amicable.insert(a);
                amicable.insert(b);
            }
        }
    }
    cout << setSum(amicable) << endl;
    return 0;
}