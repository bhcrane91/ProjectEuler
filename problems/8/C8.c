#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define MAX_LINE_LENGTH 1024

int main() {
    FILE *file = fopen("num.txt","r");
    if (file == NULL) {
        perror("Error operning file.");
        return 1;
    }

    char line[MAX_LINE_LENGTH];
    
    return 0;
}