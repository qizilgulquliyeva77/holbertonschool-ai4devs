#include <iostream>
#include <string>

void reverseString(std::string& s) {
    int n = s.length();
    // Bug: i <= n causes out-of-bounds access (s[n] is null terminator)
    // Bug: Swapping until n means it reverses back to original
    for (int i = 0; i <= n; i++) {
        char temp = s[i];
        s[i] = s[n - i];
        s[n - i] = temp;
    }
}

int main() {
    std::string str = "Hello";
    reverseString(str);
    std::cout << str << std::endl;
    return 0;
}
