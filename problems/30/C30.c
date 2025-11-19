#include <stdio.h> 
#include <math.h>

int main() {
    int ans = 0;
    for (int s = 2; s < 6; s++) {
        for (int i = ((int) pow(10,s)); i < ((int) pow(10,s+1)); i++) {
            int j = i;
            int sj = 0;
            while (j > 0) {
                int l = j % 10;
                sj += ((int) pow(l,5));
                j = (j - l) / 10;
            }
            if (sj == i) {
                ans += sj;
                // printf("%d\n",sj);
            }
        }
    }
    printf("%d\n",ans);
}