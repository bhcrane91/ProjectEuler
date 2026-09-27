#include <iostream>
#include <unordered_set>

std::unordered_set<long> divisors(long n) {
    std::unordered_set<long> divs;
    for (long i = 2L; i < ((long)sqrt(n))+1L; i++) {
        if (n % i == 0) {
            divs.insert(i);
            divs.insert(n/i);
        }
    }
    return divs;
}

int main() {
    long tri = 1L;
    long itr = 1L;

    std::unordered_set<long> divs = divisors(tri);
    int target = 500; 
    while (divs.size()+2 <= target) {
        itr++;
        tri += itr;
        divs = divisors(tri);
    }
    std::cout << "Triangle Number (" << itr << "): " << tri << " | Divisors: " << (divs.size()+2) << std::endl;
    return 0;
}