def is_palindrome(s):
    """
    Checks if a string is a palindrome.
    Fixes applied: Lowercase normalization and proper slicing step.
    """
    if not s:
        return False
        
    # Fixed: Added case normalization and removed whitespace
    clean_s = str(s).lower().replace(" ", "")
    
    # Fixed: Corrected slicing from [::-2] to [::-1]
    is_equal = (clean_s == clean_s[::-1])
    
    print(f"Checking word: '{s}' | Is palindrome: {is_equal}")
    return is_equal

is_palindrome("Racecar")
