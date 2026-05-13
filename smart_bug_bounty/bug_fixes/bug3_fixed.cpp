#include <iostream>
#include <string>
#include <algorithm>

/**
 * Reverses a given string in-place.
 * Fixes applied: Loop boundary and correct index swapping.
 */
void reverseString(std::string& s) {
    int n = s.length();
    if (n <= 1) return;

    for (int i = 0; i < n / 2; i++) {
        char temp = s[i];
        s[i] = s[n - 1 - i];
        s[n - 1 - i] = temp;
    }
}

int main() {
    std::string testStr = "Holberton";
    reverseString(testStr);
    std::cout << "The reversed output is: " << testStr << std::endl;
    return 0;
}
