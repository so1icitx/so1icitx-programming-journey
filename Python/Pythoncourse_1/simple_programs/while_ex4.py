num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not a valid number")
    num = int(input("Enter a number between 1 - 10: "))


print(f"Your number is {num}")
