#include <stdio.h>
#include <stdlib.h>

#define L 20

int main() {
    FILE *fp;
    int grid[L][L];
    int r, c;

    fp = fopen("nums.txt", "r");

    if (fp == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    for (r = 0; r < L; r++) {
        for (c = 0; c < L; c++) {
            if (fscanf(fp, "%d", &grid[r][c]) != 1) {
                fprintf(stderr, "Error reading number from file at row %d, col %d\n", r, c);
                fclose(fp);
                exit(EXIT_FAILURE);
            }
        }
    }
    fclose(fp);
    
    /*
    printf("Content of the 2D array:\n");
    for (r = 0; r < L; r++) {
        for (c = 0; c < L; c++) {
            printf("%d ", grid[r][c]);
        }
        printf("\n");
    }
    */
    return 0;
}