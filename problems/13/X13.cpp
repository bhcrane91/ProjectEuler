#include <iostream>
#include <string>
#include <fstream>

int main() {
    std::ifstream file("digits.txt"); 
    std::string line;
    long num = 0L;

    if (file.is_open()) { 
        while (std::getline(file, line)) {
            num += std::stol(line.substr(0,10));
        }
        file.close();
    } else {
        std::cerr << "Unable to open file" << std::endl;
    }

    
    std::cout << num << std::endl;

    return 0;
}
