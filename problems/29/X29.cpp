#include <unordered_set>
#include <iostream>
using namespace std;

int main() {
    unordered_set<double> s;
    int n = 100;
    for (int i = 2; i <= n; i++) {
        for (int j = 2; j <= n; j++) {
            s.insert(pow(i,j));
        }
    }
    cout << s.size() << endl;
}