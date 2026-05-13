#include <stdio.h>
#include <string.h>

void safe_string_copy(char *dest, const char *src) {
    /*
    Intended Behavior: Safely copy source string into destination buffer
    without causing buffer overflow or memory corruption.
    */
    int src_len = strlen(src);
    for (int i = 0; i <= src_len; i++) {
        dest[i] = src[i];
    }
}

int main() {
    char target_buffer[20];
    safe_string_copy(target_buffer, "test");
    return 0;
}
