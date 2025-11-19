#include <stdio.h> 

int gcd(int a, int b) {
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int coprime(int a, int b) {
    return gcd(a,b) == 1 ? 1 : 0;
}

int main() {
    int target = 1000;
    int triangles[1000];
    int max = 0;
    int nmx = 0;
    for (int m = 2; m < 100; m++) {
        for (int n = 1; n < m; n++) {
            for (int k = 1; k < 100; k++) {
                if (((m + n) % 2 != 0) && (coprime(m,n) == 1)) {
                    int a = k * (m*m - n*n);
                    int b = k * (2*m*n);
                    int c = k * (m*m + n*n);
                    int triangle = a + b + c;
                    if (triangle < target) {
                        triangles[triangle]++;
                        if (triangles[triangle] > max) {
                            max = triangles[triangle];
                            nmx = triangle;
                        }
                    }
                }
            }
        }
    }
    printf("%d %d\n",max,nmx);
}