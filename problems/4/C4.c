#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int checkPalindrome(int num) {
    int reversed = 0, original = num, remainder;
    while (num > 0) {
        remainder = num % 10;
        reversed = reversed * 10 + remainder;
        num /= 10;
    }
    return original == reversed;
}

int main(){
    int digits = 3;
    int bot = pow(10, digits-1);
    int top = pow(10,digits);
    int* max = malloc(3*sizeof(int));
    for (int i = bot; i <= top; i++) {
        for (int j = i; j >= bot; j--) {
            int p = i*j;
            if (p > max[0] && checkPalindrome(p)==1) {
                max[0] = p;
                max[1] = i;
                max[2] = j;
            }
        }
    }
    printf("C -> Max: %d | Factors: (%d,%d)\n",max[0],max[1],max[2]);
    free(max);
    return 0;
}