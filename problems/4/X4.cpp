#include <iostream>
#include <string>
#include <cmath>

int checkPalindrome(std::string str);

int main() {
    int digits = 3;
    int bot = (int) pow(10,digits-1);
    int top = (int) pow(10,digits);
    int max[3]; 
    for (int i = top; i >= bot; i--) {
        for (int j = i; j >= bot; j--) {
            int p = i*j;
            std::string str = std::to_string(p);
            if (p > max[0] && checkPalindrome(str)) {
                max[0] = p;
                max[1] = i;
                max[2] = j;
            }
        }
    }
    std::cout << "Max: " << max[0] << " | Factors: (" << max[1] << "," << max[2] << ")" << std::endl;
}

int checkPalindrome(std::string str) {
    for (int i = 0; i < str.length()/2; i++) {
        if (str.at(i) != str.at(str.length()-i-1)) return 0;
    }
    return 1;
}