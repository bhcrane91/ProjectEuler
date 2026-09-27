#include <iostream>

int checkPrime(int n) {
    if (n <= 1) return 0;
    if (n == 1) return 1;
    if (n % 2 == 0) return 0;
    for (int i = 3; i < ((int)sqrt(n))+1; i += 2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int prime = 3;
    int n = 2;
    while (n < 10001) {
        prime += 2; 
        if (checkPrime(prime)) n++;
    }
    std::cout << n << "st prime = " << prime << std::endl;
}