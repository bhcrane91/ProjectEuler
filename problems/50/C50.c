#include <stdio.h>
#include <math.h>

int checkPrime(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    for (int i = 3; i < ((int) sqrt(i)) + 1; i += 2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {

}