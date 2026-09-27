#include <stdio.h>
#include <string.h>

int main() {
    FILE *fptr;

    // Open a file in read mode
    fptr = fopen("num.txt", "r");

    // Store the content of the file
    
    int n = 50;
    char myString[n];

    // Read the content and print it
    while(fgets(myString, n, fptr)) {
        printf("%s", myString);
    }

    // Close the file
    fclose(fptr);
}