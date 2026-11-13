# BUG: Misuse of data types. Mutable default argument (list).
# The list is created once at function definition, not on every call.
# This causes the inventory list to be shared across all calls that don't provide one.

def add_item_to_inventory(item, inventory=[]):
    """
    Adds a new item to the player's inventory.
    Returns the updated inventory.
    """
    print(f"Adding {item} to inventory...")
    
    # The append operation modifies the default list in place
    inventory.append(item)
    
    print(f"Current inventory size: {len(inventory)}")
    return inventory
    
# Example of the issue:
# p1 = add_item_to_inventory("Sword") -> ["Sword"]
# p2 = add_item_to_inventory("Shield") -> ["Sword", "Shield"] (Expected just ["Shield"])
