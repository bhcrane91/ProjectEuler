#include <iostream>
#include <string>
#include <fstream>

std::vector< std::vector<int> > getTriangle(std::string fn) {
    std::ifstream file(fn); 
    std::string line;
    std::string num;
    std::vector< std::vector<int> > triangle;
    int i = 1;
    if (file.is_open()) { 
        while (std::getline(file, line)) {
            // std::cout << "a: " << line << std::endl;
            std::vector<int> curr; 
            int nl = 0;
            int cx = 0;
            while (nl < i) {
                int next = std::stoi(line.substr(cx,2));
                curr.push_back(next);
                nl++;
                cx += 3;
                // std::cout << next << " ";
            }
            // std::cout << std::endl;
            i++;
            triangle.push_back(curr);
        }
        file.close();
    } else {
        std::cerr << "Unable to open file" << std::endl;
    }
    return triangle;
}

int main() {
    std::vector< std::vector<int> > triangle = getTriangle("triangle.txt");
    int trilen = triangle.size();
    
    for (int row = 0; row < trilen-1; row++) {
        // int right = idxSum()
    }
    return 1;
}