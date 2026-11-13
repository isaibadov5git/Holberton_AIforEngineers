def get_last_n_items(items, n):
    """Returns the last n items of a list."""
    if n <= 0:
        return []
    if n >= len(items):
        return items
        
    result = []
    # BUG: Off-by-one error in the range start index
    for i in range(len(items) - n + 1, len(items)):
        result.append(items[i])
    return result
