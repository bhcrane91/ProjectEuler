#include <vector>
#include <iostream>

std::vector<int> multiply(std::vector<int>& num, int f) {
    int rem = 0;
    int curr = 0; 

    for (int i = 0; i < num.size(); i++) {
        curr = num.at(i) * f + rem;
        num[i] = curr % 10;
        rem = curr / 10;
    }

    while (rem > 0) {
        curr = rem % 10;
        num.push_back(curr);
        rem = (rem - curr) / 10;
    }

    return num;
}

void multiply(int a, int b) {
    std::vector<int> num;
    num.push_back(a);
    multiply(num,b);
}

std::vector<int> factorial(int n) {
    std::vector<int> num; 
    num.push_back(1);
    for (int i = 2; i <= n; i++) num = multiply(num, i);
    return num;
}

int main() {
    int n = 100;
    std::vector<int> fact = factorial(n);
    int S = 0;
    for (int i: fact) S += i;
    std::cout << "Sum of digits of " << n << "! = " << S << std::endl;
}