# FIXED: Replaced the mutable default argument with None.
# This ensures a fresh list is created inside the function on every call
# that doesn't explicitly provide an inventory list.

def add_item_to_inventory(item, inventory=None):
    """
    Adds a new item to the player's inventory.
    Returns the updated inventory.
    """
    if inventory is None:
        inventory = []
        
    print(f"Adding {item} to inventory...")
    
    inventory.append(item)
    
    print(f"Current inventory size: {len(inventory)}")
    return inventory
