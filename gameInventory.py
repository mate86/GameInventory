

# ========== Functions ==========

def display_inventory(inventory):
    total = 0
    print("Inventory:")
    for key, value in inventory.items():
        total += value
        print(value, key)
    print("Total number of items:", total)

def add_to_inventory(inventory, added_items):            
    for i in range(len(added_items)):
        if added_items[i] not in inventory.keys():          # If the item is not in the inventory...
                    inventory[added_items[i]] = 1           # ...then add it
                    continue
        for inv_key, inv_value in inventory.items():            
            if added_items[i] ==  inv_key:                  # If the list's element is equal to the inventory element...
                inventory[inv_key] += 1                     # ...then increase its value with 1
                continue
            if added_items[i] != inv_key:
                continue
    return inventory

# def print_table(order):


# def import_inventory(filename):


# def export_inventory(filename):



# ========== Global variables ==========

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# ========== Main ==========

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)