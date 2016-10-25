import collections

# ========== Global variables ==========

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

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

def print_table(order):
    global inv
    inventory = inv
    total = 0
    
    # If there is no argument
    if order == None:
        print("Inventory:")
        print(" "*2 + "count" + " "*4 + "item name")
        print("-"*20)
        for key, value in inv.items():
            num_of_front_space = 7 - len(str(value))
            num_of_mid_space = 20 - num_of_front_space - len(str(value)) - len(key)
            print(" "*num_of_front_space + str(value) + " "*num_of_mid_space + str(key))
            total += value
        print("-"*20)
        print("Total number of items:", total)
    # If the argument is "count,desc"
    if order == "count,desc":
        inv_list = list(inv.items())
        i = 0
        while i in range(len(inv_list)-1):
            if inv_list[i][1] < inv_list[i+1][1]:
                temp = inv_list[i]
                inv_list[i] = inv_list[i+1]
                inv_list[i+1] = temp
                if i > 0:
                    i -= 1
                else:
                    i = 0
            else:
                i += 1
                continue
        print("Inventory:")
        print(" "*2 + "count" + " "*4 + "item name")
        print("-"*20)
        for i in range(len(inv_list)):
            num_of_front_space = 7 - len(str(inv_list[i][1]))
            num_of_mid_space = 20 - num_of_front_space - len(str(inv_list[i][1])) - len(inv_list[i][0])
            print(" "*num_of_front_space + str(inv_list[i][1]) + " "*num_of_mid_space + str(inv_list[i][0]))
            total += inv_list[i][1]
        print("-"*20)
        print("Total number of items:", total)
    # If the argument is "count,asc"
    if order == "count,asc":
        inv_list = list(inv.items())
        inv_list = list(inv.items())
        i = 0
        while i in range(len(inv_list)-1):
            if inv_list[i][1] > inv_list[i+1][1]:
                temp = inv_list[i]
                inv_list[i] = inv_list[i+1]
                inv_list[i+1] = temp
                if i > 0:
                    i -= 1
                else:
                    i = 0
            else:
                i += 1
                continue
        print("Inventory:")
        print(" "*2 + "count" + " "*4 + "item name")
        print("-"*20)
        for i in range(len(inv_list)):
            num_of_front_space = 7 - len(str(inv_list[i][1]))
            num_of_mid_space = 20 - num_of_front_space - len(str(inv_list[i][1])) - len(inv_list[i][0])
            print(" "*num_of_front_space + str(inv_list[i][1]) + " "*num_of_mid_space + str(inv_list[i][0]))
            total += inv_list[i][1]
        print("-"*20)
        print("Total number of items:", total)


# def import_inventory(filename):


# def export_inventory(filename):



# ========== Main ==========

inv = add_to_inventory(inv, dragon_loot)
# display_inventory(inv)
# order = None
# order = "count,desc"
order = "count,asc"

print_table(order)
