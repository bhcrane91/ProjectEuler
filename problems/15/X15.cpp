#include <iostream>
#include <algorithm>

std::vector<long> pascal(int n) {
    std::vector<long> pascalRow(2*n);
    pascalRow[0] = 1L;
    for (int row = 0; row < 2*n; row++) {
        for (int i = 0; i < 2*n; i++) {
            pascalRow[i] += pascalRow[(i+1)%(2*n)];
        }
    }
    return pascalRow;
}

int main() {
    int target = 20;
    std::vector<long> triangle = pascal(target);
    std::cout << "Paths in " << target << "x" << target << " square: " << *std::max_element(triangle.begin(), triangle.end()) << std::endl;
}