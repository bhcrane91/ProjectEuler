#include <iostream>
#include <unordered_set>
#include <tuple>
#include <string>
using namespace std;

tuple<int,string> longDivide(int a, int b) {
    unordered_set<int> remainders;
    int rem = a % b;
    string digits;

    while (rem != 0 && remainders.find(rem) == remainders.end()) {
        remainders.insert(rem);
        rem *= 10;
        digits.append(to_string((int)(rem / b)));
        rem %= b;
    }
    return {rem,digits};

}

int main() {
    int lmx = 0;
    int k = 0;
    for (int i = 1; i < 1000; i++) {
        tuple<int,string> ans = longDivide(1,i);
        if (get<1>(ans).length() > lmx) {
            lmx = get<1>(ans).length();
            k = i;
        }
    }
    cout << k << ": " << lmx << endl;
}