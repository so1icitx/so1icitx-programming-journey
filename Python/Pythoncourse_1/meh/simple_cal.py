def main_calc(num1, symbol, num2):
    if symbol == '+':
        return num1 + num2
    elif symbol == '-':
        return num1 - num2
    elif symbol == '*':
        return num1 * num2
    elif symbol == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"


first_cal = main_calc(num1=int(input("Enter the first number: ")),symbol=input("Enter a symbol (+, -, *, /): "),num2=int(input("Enter the second number: ")))

while True:
    print(f"Current result: {first_cal}")
    continue_cal = input("Do you want to continue with this result? (y/n/exit): ").lower()

    if continue_cal == 'y':
        symbol = input("Enter a symbol (+, -, *, /): ")
        num2 = int(input("Enter the next number: "))
        first_cal = main_calc(num1=first_cal, symbol=symbol, num2=num2)
    elif continue_cal == 'n':
        first_cal = main_calc(num1=int(input("Enter a new first number: ")),symbol=input("Enter a symbol (+, -, *, /): "),num2=int(input("Enter the second number: ")))
    elif continue_cal == 'exit':
        print("Calculator closed.")
        break
    else:
        print("Invalid input. Please enter 'y', 'n', or 'exit'.")
