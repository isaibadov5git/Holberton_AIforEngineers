# BUG: Misuse of data types. Mutable default argument (list).
# The list is created once at function definition, not on every call.
def add_item_to_inventory(item, inventory=[]):
    inventory.append(item)
    return inventory
