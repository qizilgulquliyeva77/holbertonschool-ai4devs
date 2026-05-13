#include <stdio.h>
#include <string.h>
void safe_string_copy(char *dest, const char *src) {
    int src_len = strlen(src);
    for (int i = 0; i <= src_len; i++) {
        dest[i] = src[i];
    }
}
