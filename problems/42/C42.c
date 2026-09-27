#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LINE_LENGTH 20000
#define DELIMITERS ",\"" // Example delimiters: space, comma, hyphen, newline

int main() {
    FILE *file;
    char line[MAX_LINE_LENGTH];

    // Open the file in read mode
    file = fopen("words.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    int triSum = 0; 
    // Read lines one by one until the end of the file
    while (fgets(line, sizeof(line), file) != NULL) {
        // Use strtok to split the line into tokens
        char *token = strtok(line, DELIMITERS);

        // Process each token in the line
        while (token != NULL) {
            // Do something with the token (e.g., print it)
            
            int nSum = 0;
            for (int i = 0; i < strlen(token); i++) {
                nSum += (int) token[i];
            }
            printf("Token: %s -> %d\n", token, nSum);

            // Get the next token (pass NULL to continue from the same string)
            token = strtok(NULL, DELIMITERS);

            

            
        }
        printf("-- End of line --\n"); // Optional: separator for each line's tokens
    }

    // Close the file
    fclose(file);

    return 0;
}