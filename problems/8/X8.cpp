#include <iostream>
#include <string>
#include <fstream>

int main() {
    std::ifstream file("num.txt"); 
    std::string line;
    std::string num;

    if (file.is_open()) { 
        while (std::getline(file, line)) {
            num.append(line);
        }
        file.close();
    } else {
        std::cerr << "Unable to open file" << std::endl;
    }

    long m = 0L;
    int k = 13;
    std::string submax = "";
    std::vector<int> places;
    places.reserve(2);
    for (int i = 0; i < num.size()-k; i++) {
        long curr = 1L;
        for (int j = 0; j < k; j++) {
            curr *= ((int)num[i+j]) - 48;
        }
        if (curr > m) {
            m = curr;
            submax = num.substr(i,k);
            places[0] = i;
            places[1] = i + k;
        }
    }
    std::cout << m << " | " << submax << " (" << places[0] << ", " << places[1] << ")" << std::endl;

    return 0;
}
