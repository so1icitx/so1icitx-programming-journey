weight = float(input("Enter your weight: "))
unit = input("In Kgs or Pounds? (k or l)")

if unit =="k".lower():
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
    
elif unit == "l".lower():
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"Sorry, {unit} is not valid")

