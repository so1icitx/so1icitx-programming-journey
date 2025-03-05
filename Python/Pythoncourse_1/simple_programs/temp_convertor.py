unit = input("Celsius or Fahrenheit (c/f): ")
temp = float(input("Enter the temperature: "))

if unit == "c".lower():
    temp = round(temp * 9 / 5 + 32, 1)
    print(f"{temp} F")
elif unit == "f".lower():
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"{temp} C")
else:
    print(f"{unit} is not a valid input")
