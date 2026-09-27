#include <iostream>
#include <string>
#include <vector>
#include <cmath>

int main() {
    std::vector<long> list;
    long n = 600851475143L;
    long num = n;

    while (n % 2 == 0) {
        list.push_back(2L);
        n /= 2;
    }

    for (long i = 3; i < ((long) sqrt(n))+1; i += 2) {
        while (n % i == 0) {
            n /= i; 
            list.push_back(i);
        }
    }
    if (n > 1) list.push_back(n);

    std::cout << "Prime Factors of " << num << ": " << std::endl;
    for (int i = 0; i < list.size(); i++) std::cout << list[i] << " " << std::endl;
    std::cout << "| Largest -> " << list[list.size() - 1] << std::endl;
}