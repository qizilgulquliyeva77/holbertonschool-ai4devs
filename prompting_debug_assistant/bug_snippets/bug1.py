def get_last_n_items(items, n):
    if n <= 0:
        return []
    start_index = len(items) - n
    if start_index == 0:
        return items[start_index + 1:]
    return items[start_index:]
