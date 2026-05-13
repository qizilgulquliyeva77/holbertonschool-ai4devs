#include <stdio.h>
#include <string.h>
void safe_string_copy(char *dest, size_t dest_size, const char *src) {
    if (dest_size == 0) return;
    size_t src_len = strlen(src);
    size_t i;
    for (i = 0; i < src_len && i < (dest_size - 1); i++) {
        dest[i] = src[i];
    }
    dest[i] = '\0';
}
