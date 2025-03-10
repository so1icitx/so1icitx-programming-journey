foods = []
prices = []
total = 0

while True:
    food = input("What food do you want to buy? (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART ------")

for food in foods:
    print(f"{foods.index(food) + 1}: {food}")

for price in prices:
    total += price

print(f"\nYour total is: ${total}")
