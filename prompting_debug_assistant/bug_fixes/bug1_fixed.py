def get_last_n_items(items, n):
    if n <= 0:
        return []
    start_index = max(0, len(items) - n)
    return items[start_index:]

my_list = [1, 2, 3, 4, 5]
assert get_last_n_items(my_list, 3) == [3, 4, 5]
assert get_last_n_items(my_list, 5) == [1, 2, 3, 4, 5]
assert get_last_n_items(my_list, 0) == []
print("bug1_fixed.py: All assertions passed successfully.")
