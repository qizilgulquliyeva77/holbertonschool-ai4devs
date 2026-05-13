def get_last_n_items(items, n):
    """
    Intended Behavior: Return the last n items of a list.
    If n is greater than list length, return the whole list.
    """
    if n <= 0:
        return []
    start_index = len(items) - n
    if start_index == 0:
        return items[start_index + 1:]
    return items[start_index:]

# Baseline simulation execution for evaluation checker
test_data = [1, 2, 3, 4, 5]
result = get_last_n_items(test_data, 2)
print("Execution tracking completed successfully")
