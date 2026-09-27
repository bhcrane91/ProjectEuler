#include <iostream>

std::vector<long> collatz(int n) {
    long iters = 1L;
    long num = (long) n;
    while (num != 1) {
        num = (num % 2 == 0) ? (num / 2) : (3*num + 1);
        iters++;
    }
    std::vector<long> res;
    res.push_back(n);
    res.push_back(iters);
    return res;
}

int main() {
    int target = 1000000;
    std::vector<long> c = collatz(113383);
    long m = 0;
    long num = 0;
    for (int i = 1; i < target; i++) {
        std::vector<long> seq = collatz(i);
        if (seq[1] > m) {
            m = seq[1];
            num = seq[0];
        }
    }
    std::cout << "Maximum Collatz Sequence for c[0] < " << target << ": c[0] = " << num << " | Length: " << m << std::endl;
    return 0;
}