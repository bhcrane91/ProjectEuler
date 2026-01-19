#include <stdio.h> 

int palindrome(int a) {
    int b = 0;
    int p = 1;
    int c = a; 
    printf("%d %d %d\n",a,b,c);
    while (a > 0) {
        int l = a % 10;
        b += (l * p);
        p *= 10;
        a /= 10;
    }
    printf("%d %d %d\n",a,b,c);
    return b == c ? 1 : 0;
}

int main() {
    for (int i = 0; i < 1000; i++) {
        if (palindrome(i) == 1) {
            printf("%d\n",i);
        }
    }
    return 0;
}