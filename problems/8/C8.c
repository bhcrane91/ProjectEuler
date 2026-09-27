#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* read_file_into_string(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file");
        return NULL;
    }

    // Determine file size
    fseek(file, 0, SEEK_END);
    long length = ftell(file);
    fseek(file, 0, SEEK_SET);

    // Allocate memory for the file content (+1 for the null terminator)
    char* buffer = (char*)malloc(length + 1);
    if (buffer == NULL) {
        perror("Error allocating memory");
        fclose(file);
        return NULL;
    }

    // Read the entire file into the buffer
    size_t read_bytes = fread(buffer, 1, length, file);
    fclose(file);

    if (read_bytes != length) {
        fprintf(stderr, "Error reading file: read %zu bytes, expected %ld\n", read_bytes, length);
        free(buffer);
        return NULL;
    }

    // Null-terminate the string
    buffer[length] = '\0';

    return buffer;
}

int main() {
    const char* filename = "num.txt"; // Replace with your file name
    char* file_content = read_file_into_string(filename);

    if (file_content != NULL) {
        printf("File Content:\n%s\n", file_content);

        // Free the dynamically allocated memory after use
        free(file_content);
    }

    return 0;
}
