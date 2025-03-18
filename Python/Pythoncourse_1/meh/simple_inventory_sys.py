def adding():
    while True:
        item = input("Input a item to add (q to quit): ")
        if item == "q":
            break
        elif item in inventory:
            inventory[item] += 1
            print(f"adding duplicate item({item}")
        else:
            inventory[item] = 1
            print(f"adding new item into inventory({item})")

def removing():
    while True:
        item = input("Input a item to remove(q to quit): ")
        if item == "q":
            break
        elif item in inventory:
            inventory.pop(item)
            print(f"removing item({item}")
        else:
            print(f"{item} is not in your inventory!")
            choice = input("Do you wish to add it? (y/n): ")
            if choice == "y":
                print(f"adding new item into inventory({item})")
                inventory[item] = 1
            else:
                print("skipping...")
                
inventory = {}
while True:
    print("What would you like to do?\n1. close\n2. add\n3. remove\n4. view")
    choice = int(input(": "))
    match choice:
        case 1:
            print("Sayonara!")
            break
        case 2:
            adding()
            print()
        case 3:
            removing()
            print()
        case 4:
            if not inventory:
                print("[!] Inventory is empty :(")
                print()
            else:
                print("------INVENTORY------")
                for key, value in inventory.items():
                    print(f"{key}: {value}")
                print()
        case _:
            print("INVALID INPUT")
