#include <stdio.h>
#include <string.h>

void safe_string_copy(char *dest, size_t dest_size, const char *src) {
    /*
    Fixed Behavior: Boundary validated loops with explicit manual null-termination
    to eliminate buffer overflow hazards.
    */
    if (dest_size == 0) return;
    
    size_t src_len = strlen(src);
    size_t i;
    
    // AI Fix Applied: Bounded iteration constraint (i < dest_size - 1)
    for (i = 0; i < src_len && i < (dest_size - 1); i++) {
        dest[i] = src[i];
    }
    dest[i] = '\0'; // Guarantee strict null-termination boundary
}

int main() {
    char buffer[12]; // Allocated enough space for string + null-terminator
    safe_string_copy(buffer, sizeof(buffer), "HELLO_WORLD");
    printf("Result: %s\n", buffer);
    return 0;
}
