#include <iostream>

int main() {
    long n = 100L;
    long sumOfSquares = (n * (n+1) * (2*n + 1)) / 6;
    long squareOfSums = (n * (n+1)) / 2;
    squareOfSums *= squareOfSums;
    std::cout << (squareOfSums - sumOfSquares) << std::endl;
}