def get_last_n_items(items, n):
    """
    Returns the last n items of a list.
    If n is greater than the list length, returns the whole list.
    If n is less than or equal to 0, returns an empty list.
    """
    if n <= 0:
        return []
    
    if n >= len(items):
        return items
        
    result = []
    
    # BUG: Off-by-one error in the range start index
    # It should be len(items) - n, but the +1 makes it start one index too late.
    for i in range(len(items) - n + 1, len(items)):
        result.append(items[i])
        
    return result
