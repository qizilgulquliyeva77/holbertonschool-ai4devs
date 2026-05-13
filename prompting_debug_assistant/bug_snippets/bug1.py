def get_last_n_items(items, n):
    """
    Intended Behavior: Return the last n items of a list.
    If n is greater than list length, return the whole list.
    """
    if n <= 0:
        return []
    
    start_index = len(items) - n
    # Bug: Off-by-one error when n == len(items), slice returns empty list instead of full list
    if start_index == 0:
        return items[start_index + 1:]
        
    return items[start_index:]

# Test case that fails
my_list = [10, 20, 30, 40, 50]
print(f"Expected [10, 20, 30, 40, 50], Got: {get_last_n_items(my_list, 5)}")
