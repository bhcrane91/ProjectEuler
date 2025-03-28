#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    uint64_t num = 600851475143;
    uint64_t n = num;
    uint8_t l = 4;
    uint32_t* factors = malloc(l*sizeof(uint32_t));
    uint8_t f = 0;
    while (n % 2 == 0) {
        factors[f] = 2;
        n /= 2;
        f++;
        if (f==l) {
            l *= 2;
            factors = realloc(factors, l*sizeof(uint32_t));
        }
    }
    for (uint32_t i = 3; i < sqrt(n)+1; i += 2) {
        while (n % i == 0) { 
            factors[f] = i;
            n /= i;
            f++;
            if (f==l) {
                l *= 2;
                factors = realloc(factors, l*sizeof(uint32_t));
            }
        }
    }
    if (n > 1) {
        factors[f] = n;
        f++;
    }
    printf("C -> Prime Factors of %"PRIu64": [",num);
    for (int i = 0; i < f-1; i++) {
        printf("%" PRIu32 ", ",factors[i]);
    }
    printf("%"PRIu32"] | Largest -> %"PRIu32"\n",factors[f-1],factors[f-1]);
    free(factors);
    return 0;
}