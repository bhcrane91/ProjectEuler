#include <iostream>
using namespace std;

int main() {
    int side = 1001; 
    int top = side*side; 
    int sum = top; 
    while (top != 1) {
        for (int i = 0; i < 4; i++) {
            top -= (side-1); 
            sum += top; 
        }
        side -= 2;
    }	
    cout << sum << endl;
}