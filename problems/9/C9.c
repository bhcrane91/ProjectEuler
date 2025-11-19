#include <stdio.h>

int main() {
    for (int a = 100; a < 1000; a++) {
		for (int b = a; b < 1000-a; b++) {
			int c = 1000 - a - b;
			if (a*a+b*b == c*c) {
				printf("Triple: (%d,%d,%d) | Product: %d",a,b,c,(a*b*c));
				return 0;
			}
		}
	}
    return 0;
}