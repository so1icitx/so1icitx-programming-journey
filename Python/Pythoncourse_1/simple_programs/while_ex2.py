age = int(input("Enter your age: "))

while age < 0:
    print("Sorry, you can't enter a negative number.")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")
