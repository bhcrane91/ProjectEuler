#include <stdio.h>
#include <math.h>

int main() {
    double a = 1;
    double b = 1;
    int i = 1;
    double x = a+b;
    int j = 2;
    int n = 1000;
    while (i < n) {
        j += 1;
        x = a + b;
        int e = ((int) log10(x)) - ((int) log10(b));
        i += e;
        a = b;
        b = x;
        if (e > 0) {
            a /= 10;
            b /= 10;
        }
        // printf("%d %d %.2f %.2f %.2f %d\n",i,j,a,b,x,e);
    }
    printf("First Fibonacci term with %d digits: F_n -> n = %d\n",n,j);
    //printf("%.f %.f %.f",a,b,x);
}
