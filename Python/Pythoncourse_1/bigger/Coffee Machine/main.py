MENU = {"espresso": {"ingredients": {"water": 50,"milk" : 0, "coffee": 18}, "cost": 1.5},
        "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
        "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}}
resources = { "water" : 300, "milk" : 200, "coffee" : 100, "money" : 0}



def resource_check(total_cost, choice):
    if resources["water"] < MENU[choice]["ingredients"].get("water"):
        print("Sorry, there is not enough water.")
        return
    elif resources["milk"] < MENU[choice]["ingredients"].get("milk"):
        print("Sorry, there is not enough milk.")
        return
    elif resources["coffee"] < MENU[choice]["ingredients"].get("coffee"):
        print("Sorry, there is not enough coffee.")
        return
    else:
        money(total_cost, choice)
        return

def money(total_cost, choice):
    try:
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickels = float(input("How many nickels?: "))
        pennies = float(input("How many pennies?: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    total_given = (float(quarters) * 0.25) + (float(dimes) * 0.10) + (float(nickels) * 0.05) + (float(pennies) * 0.01)
    if total_given > total_cost:
        change = total_given - total_cost
        print(f"Here is your change: ${change:.2f}")
        resources["money"] += total_cost
        return calc(choice)
    elif total_given < total_cost:
        print(" [!] Insufficient money")
        return
    else:
        resources["money"] += total_cost
        return calc(choice)

def calc(choice):
        resources["water"] -= MENU[choice]["ingredients"].get("water")
        resources["milk"] -= MENU[choice]["ingredients"].get("milk")
        resources["coffee"] -= MENU[choice]["ingredients"].get("coffee")
        print(f"Here is your {choice}, enjoy!!!")
        return
def main():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            break
        elif choice == "report":
            print(resources)
        elif choice == "espresso":
            resource_check(1.5, choice)
        elif choice == "latte":
            resource_check(2.5, choice)
        elif choice == "cappuccino":
            resource_check(3.0, choice)
        else:
            print("[!] Invalid choice")
if __name__ == "__main__":
    main()
