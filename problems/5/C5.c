#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int* removeElement(int* array, int size, int index_to_remove) {
    if (index_to_remove < 0 || index_to_remove >= size) {
        printf("Index out of bounds.\n");
        return array;
    }

    for (int i = index_to_remove; i < size - 1; i++) {
        array[i] = array[i + 1];
    }

    int* new_array = realloc(array, (size - 1) * sizeof(int));
    if (new_array == NULL && size > 1) {
        printf("Memory reallocation failed.\n");
        return array;
    }

    return new_array;
}

int* prime_factors(int n, int* j) {
    if (n <= 1) return NULL;
    int f = 4;
    int* factors = malloc(f*sizeof(int));
    while (n % 2 == 0) { 
        factors[*j++] = 2;
        n /= 2;
        if (*j == &f) {
            f += 4;
            factors = realloc(factors, f*sizeof(int));
        }
        printf("%d ",factors[*j-1]);
    }

    for (int i = 3; i < sqrt(n)+1; i+=2) {
        while (n % i == 0) {
            factors[*j++] = i;
            if (*j == f) {
                f += 4;
                factors = realloc(factors, f*sizeof(int));
            }
            n /= i;
            printf("%d ",factors[*j-1]);
        }
    }
    if (n > 1) factors[*j++] = n;
    factors = realloc(factors, (*j)*sizeof(int));
    printf("%d ",n);
    return factors; 
}
/*
int gcd(int a, int b) {
    printf("gcd a=%d b=%d\n",a,b);
    int* factors_a = prime_factors(a);
    int* factors_b = prime_factors(b);
    int div = 1;
    for (int i = 0; i < (sizeof(&factors_a)/sizeof(&factors_a[0])); i++) {
        for (int j = 0; j < (sizeof(&factors_b)/sizeof(&factors_b[0])); j++) {
            if (factors_a[i] == factors_b[j]) {
                div *= factors_a[i];
                factors_b = removeElement(factors_b, (sizeof(&factors_b)/sizeof(&factors_b[0])), j); 
            }
        }
    }
    free(factors_a);
    free(factors_b);
    return div;
}

int lcm(int a, int b) {
    printf("lcm a=%d b=%d\n",a,b);
    return a*b/gcd(a,b);
}
*/
int main() {
    int ans = 1;
    int nf = 0; 
    for (int i = 2; i <= 20; i++) {
        printf("i: %d -> ",i);
        //ans = lcm(ans, i);
        int* factors = prime_factors(i,&nf);
        // printf("\n");
        printf("| j < %lu\n", (sizeof(&factors)/sizeof(factors[0])));
        for (int j = 0; j < nf; j++) {
            printf("%d ",factors[j]);
        }
        printf("\n");
    }
    return 0;
}