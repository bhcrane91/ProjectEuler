#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define MAX_LINE_LENGTH 1024

int main() {
    FILE *file = fopen("base_exp.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    char line[MAX_LINE_LENGTH];
    double maxVal = 0;
    int maxIdx = 0;
    int linNum = 1;
    int* curr = malloc(2*sizeof(int));

    while (fgets(line, sizeof(line), file)) {
        // Remove newline character if it exists
        line[strcspn(line, "\n")] = '\0';

        // Split the line by commas
        char *token = strtok(line, ",");
        int i = 0; 
        while (token != NULL) {
            // printf("%s ", token); // Process each token as needed
            curr[i++] = atoi(token);
            token = strtok(NULL, ",");
        }

        double n = curr[1] * log(curr[0]);
        if (n > maxVal) {
            maxVal = n;
            maxIdx = linNum;
        }
        linNum++;
    }

    free(curr);
    fclose(file);
	printf("C: Answer -> Max Value: %f | Line Number: %d\n",maxVal,maxIdx);
    return 0;
}
