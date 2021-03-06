# Mate Balazs, 2016, Codecool
import random

# ========== Global variables ==========

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# ========== Functions ==========

def display_inventory(inventory):
    total = 0                                                   # Total number of items
    print("Inventory:")
    for key, value in inventory.items():
        total += value
        print(value, key)
    print("Total number of items:", total)

def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        if added_items[i] in inventory:                         # If the item is in the inventory...
            inventory[added_items[i]] += 1                      # ...then increase its value
        else:                                                   # If the item is not in the inventory...
            inventory[added_items[i]] = 1                       # ...then add it
    return inventory

def print_table(order = None):
    global inv
    inventory = inv
    total = 0                                                   # Total number of items
    
    # If there is no argument
    if order == None:
        print("Inventory:")
        print(" "*2 + "count" + " "*4 + "item name")
        print("-"*20)
        for key, value in inv.items():
            front_space = 7 - len(str(value))                                       # Calculates the space before the value
            mid_space = 20 - front_space - len(str(value)) - len(key)               # Calculates the space between the value and the item
            print(" "*front_space + str(value) + " "*mid_space + str(key))
            total += value
        print("-"*20)
        print("Total number of items:", total)
    # If the argument is "count,desc"
    if order == "count,desc":
        inv_list = list(inv.items())
        i = 0
        while i in range(len(inv_list)-1):                      # Sorts the items
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
            front_space = 7 - len(str(inv_list[i][1]))
            mid_space = 20 - front_space - len(str(inv_list[i][1])) - len(inv_list[i][0])
            print(" "*front_space + str(inv_list[i][1]) + " "*mid_space + str(inv_list[i][0]))
            total += inv_list[i][1]
        print("-"*20)
        print("Total number of items:", total)
    # If the argument is "count,asc"
    if order == "count,asc":
        inv_list = list(inv.items())
        inv_list = list(inv.items())
        i = 0
        while i in range(len(inv_list)-1):                      # Sorts the items
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
            front_space = 7 - len(str(inv_list[i][1]))
            mid_space = 20 - front_space - len(str(inv_list[i][1])) - len(inv_list[i][0])
            print(" "*front_space + str(inv_list[i][1]) + " "*mid_space + str(inv_list[i][0]))
            total += inv_list[i][1]
        print("-"*20)
        print("Total number of items:", total)

def import_inventory(filename = "import_inventory.csv"):
    global inv
    try:                                                        # Try to open the file
        file = open(filename, "r")
        file_list = file.read().splitlines()                    # Creates a list from the file lines without newline character
        file.close()
    except:                                                     # If file does not exist, throws an exception, then quits
        print("Error! File ('" + str(filename) + "') does not exist!")
        quit()

    file_element = []

    for i in range(1,len(file_list)):                           # Puts te lines into a two dimensional list without the first line
        file_element.append(file_list[i].split(","))            # Splits the lines at the comma

    del file_list

    for i in range(len(file_element)):                          # Converts the value from 'str' to 'int'
        file_element[i][1] = int(file_element[i][1])
    
    for i in range(len(file_element)):
        if file_element[i][0] not in inv:                       # If the element is not in the inventory...
            inv[file_element[i][0]] = file_element[i][1]        # ...let add it
        else:
            inv[file_element[i][0]] += file_element[i][1]

def export_inventory(filename = "export_inventory.csv"):
    global inv
    file = open(filename, "w")
    file.write("item_name,count")
    for key, value in inv.items():
        file.write("\n" + str(key) + "," + str(value))          # Writes the items to the file, separated with comma
    file.close()

def attack(enemy):
    global inv
    result = random.randint(1,10)
    if result > 3:
        try:                                                        # Try to open the file
            file = open(enemy, "r")
            file_list = file.read().splitlines()                    # Creates a list from the file lines without newline character
            file.close()
        except:                                                     # If file does not exist, throws an exception, then quits
            print("Error! File ('" + str(filename) + "') does not exist!")
            quit()
        
        file_element = []

        for i in range(1,len(file_list)):                           # Puts te lines into a two dimensional list without the first line
            file_element.append(file_list[i].split(","))            # Splits the lines at the comma

        del file_list

        for i in range(len(file_element)):                          # Converts the value from 'str' to 'int'
            file_element[i][1] = int(file_element[i][1])
        
        for i in range(len(file_element)):
            if file_element[i][0] not in inv:                       # If the element is not in the inventory...
                inv[file_element[i][0]] = file_element[i][1]        # ...let add it
            else:
                inv[file_element[i][0]] += file_element[i][1]

        print("You won the battle!")
        print("-"*20)
        print("Your reward is:")
        for i in range(len(file_element)):
            front_space = 7 - len(str(file_element[i][1]))
            mid_space = 20 - front_space - len(str(file_element[i][1])) - len(file_element[i][0])
            print(" "*front_space + str(file_element[i][1]) + " "*mid_space + str(file_element[i][0]))
        print("-"*20)
        display_inventory(inv)
        print("-"*20)
        export_inventory()
    else:
        print("You are died!")
        print_table("count,desc")
        export_inventory()
        quit()

def main():
    global inv
    inv = add_to_inventory(inv, dragon_loot)                    # Calls the mandatory functions :)
    import_inventory()
    command = "f"
    while True:
        if command == "f":
            print("You are in the forest. Where do you want to go?")
            command = input("To the cave ('c'), to the lake ('l'), to the mountains ('m') or quit ('q'): ")
            continue
        if command == "c":
            print("You are in the cave. A barbarian attacks you!")
            attack("barbarian.csv")
            print("Where do you want to go?")
            command = input("To the forest ('f'), to the lake ('l'), to the mountains ('m') or quit ('q'): ")
            continue
        if command == "l":
            print("You are at the lake. An ork attacks you!")
            attack("ork.csv")
            print("Where do you want to go?")
            command = input("To the cave ('c'), to the forest ('f'), to the mountains ('m') or quit ('q'): ")
            continue
        if command == "m":
            print("You are in the mountains. A wolf attacks you!")
            attack("wolf.csv")
            print("Where do you want to go?")
            command = input("To the cave ('c'), to the lake ('l'), to the forest ('f') or quit ('q'): ")
            continue
        if command == "q":
            export_inventory()
            quit()
        else:
            print("Invalid command!")
            print("Where do you want to go?")
            command = input("To the forest ('f'), to the cave ('c'), to the lake ('l'), to the forest ('f') or quit ('q'): ")
    
    export_inventory()

# ========== Main ==========

main()
