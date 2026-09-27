#include <iostream>

std::vector<short> exponentiate(short base, short exp) {
    /*if (base == 0) return 0;
    if (exp == 0) return 1;
    if (exp == 1) return base;*/

    std::vector<short> num; 
    num.push_back(base);
    for (short i = 1; i < exp; i++) {
        short rem = 0; 
        for (short j = 0; j < num.size(); j++) {
            short curr = (num[j] * base) + rem;
            if (curr < 10) {
                num[j] = curr;
                rem = 0;
            } else {
                num[j] = curr % 10;
                rem = curr / 10;
            }
        }
        if (rem > 0) num.push_back(rem);
    }
    return num;
} 

int main() {
    short b = 2;
    short e = 1000;
    std::vector<short> res = exponentiate(b,e);
    short S = 0;
    for (short n = 0; n < res.size(); n++) S += res[n];
    std::cout << "Sum of digits of " << b << "^" << e << ": " << S << std::endl;
    return 0;
}