#include <stdio.h>
#include <string.h>

void safe_string_copy(char *dest, const char *src) {
    /*
    Intended Behavior: Safely copy source string into destination buffer
    without causing buffer overflow or memory corruption.
    */
    int src_len = strlen(src);
    
    // Bug: Off-by-one loop logic, copies the characters but overwrites bounds
    // Bug: Missing manual null-terminator assignment if loop terminates exactly at bound
    for (int i = 0; i <= src_len; i++) {
        dest[i] = src[i];
    }
}

int main() {
    char buffer[5];
    safe_string_copy(buffer, "HELLO_WORLD"); // Stack buffer overflow vulnerability
    printf("%s\n", buffer);
    return 0;
}
