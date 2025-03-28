#include <stdio.h>
#include <inttypes.h>

int main() {
    uint32_t n = 100;
    uint32_t sumOfSquares = (n * (n+1) * (2*n + 1)) / 6;
	uint32_t squareOfSums = (n * (n+1)) / 2;
	squareOfSums *= squareOfSums;
    printf("C -> : %"PRIu32,squareOfSums - sumOfSquares);
}