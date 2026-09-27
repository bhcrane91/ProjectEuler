#include <iostream>

int checkPrime(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    for (int i = 3; i < ((int)sqrt(n))+1; i += 2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int limit = 2000000;
    long ans = 2L;
    int numP = 1;
    for (int i = 1; i < limit; i += 2) {
        if (checkPrime(i)) {
            ans += i;
            numP++;
        }
    }
    std::cout << "Number of Primes below " << limit << ": " << numP << " | Sum: " << ans << std::endl;
    return 0;
}