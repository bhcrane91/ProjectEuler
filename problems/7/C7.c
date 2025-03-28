#include <stdio.h>
#include <math.h>

int checkPrime(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    for (int i = 3; i < sqrt(n)+1; i+=2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main(){
    int prime = 1;
    int n = 0; 
    while (n < 10001) {
        if (checkPrime(prime++) == 1) n+=1;
    }
    printf("C -> %dst prime = %d\n",n,prime);
    return 0;
}