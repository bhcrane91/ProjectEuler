#include <vector>
#include <iostream>
#include <unordered_set>
using namespace std;

unordered_set<int> divisors(int n) {
    unordered_set<int> divs;
    divs.insert(1);
    for (int i = 2; i < (int)sqrt(n) + 1; i++) {
        if (n % i == 0) {
            divs.insert(i);
            divs.insert((int)(n/i));
        }
    }
    return divs;
}

int main() {
    int cutoff = 28124;
    vector<int> abundants;
    unordered_set<int> doubles;
    for (int i = 12; i < cutoff; i++) {
        int divSum = 0; 
        for (int j: divisors(i)) divSum += j;
        if (divSum > i) {
            abundants.push_back(i);
            for (int k: abundants) {
                doubles.insert(k+i);
            }
        }
    }
    int nonAbundant = 0; 
    for (int i = 0; i < cutoff; i++) {
        if (doubles.find(i) == doubles.end()) nonAbundant += i;
    }
    cout << nonAbundant << endl;
}