def get_last_n_items(items, n):
    if n <= 0:
        return []
    start_index = max(0, len(items) - n)
    return items[start_index:]
