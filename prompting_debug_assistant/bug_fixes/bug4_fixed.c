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
    for (i = 0; i < src_len && i < (dest_size - 1); i++) {
        dest[i] = src[i];
    }
    dest[i] = '\0';
}

int main() {
    char target_buffer[20];
    safe_string_copy(target_buffer, sizeof(target_buffer), "fixed");
    return 0;
}
