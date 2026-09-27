#include <iostream>
#include <set>
using namespace std;

int checkPrime(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0)  return 0;
    for (int i = 3; i < ((int)sqrt(n))+1; i+=2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

set<int> primesBelow(int n) {
    set<int> primes;
    for (int i = 2; i < n; i++) {
        if (checkPrime(i) == 1) primes.insert(i);
    }
    return primes;
}

int quadratic(int a, int b, int c) {
    return c*c + a*c + b;
}

int main() {
    set<int> pb = primesBelow(1000);
    int streak[3] = {};
    for (int a = -999; a < 1000; a++) {
        for (int b: pb) {
            int curr = quadratic(a,b,1);
            int run = 1;
            while (pb.find(curr) != pb.end()) {
                run++;
                curr = quadratic(a,b,run);
            }
            if (run > streak[0]) {
                streak[0] = run;
                streak[1] = a;
                streak[2] = b;
            }
        }
    }
    cout << "Streak: " << streak[0] << + " | a = " << streak[1] << ", b = " << streak[2] << " | a*b = " << (streak[1]*streak[2]) << endl;
}