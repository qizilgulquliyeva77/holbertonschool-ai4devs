def get_last_n_items(items, n):
    """
    Fixed Behavior: Returns the last n items of a list safely.
    If n is greater than list length, returns the whole list.
    """
    if n <= 0:
        return []
    
    # AI Fix Applied: Removed the broken conditional check and simplified slicing.
    start_index = max(0, len(items) - n)
    return items[start_index:]

# Validation Tests
my_list = [1, 2, 3, 4, 5]
assert get_last_n_items(my_list, 3) == [3, 4, 5]
assert get_last_n_items(my_list, 5) == [1, 2, 3, 4, 5]
assert get_last_n_items(my_list, 0) == []
print("bug1_fixed.py: All assertions passed successfully.")
