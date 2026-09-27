#include <iostream>
#include <set>
using namespace std;

int pentagon(int n) {
    return (3*(n*n)-n) / 2;
}

int main() {
    set<int> pnums;
    for (int i = 1; i < 5000; i++) pnums.insert(pentagon(i));
    int D[3] = {INT32_MAX,0,0};
    for (auto end = pnums.begin(); end != pnums.end(); end++) {
        for (auto start = pnums.begin(); start != end; start++) {
            int j = *end;
            int k = *start;
            int s = j + k;
            int d = j - k;
            if (d < D[0] && (pnums.find(s) != pnums.end()) && (pnums.find(d) != pnums.end())) {
                cout << d << " " << j << " " << k << " " << s << endl;
            }
        }
    }
}