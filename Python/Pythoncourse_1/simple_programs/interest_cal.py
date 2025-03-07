principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less or equal to 0")
        print("Try again")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("The interest rate can't be less or equal to 0")
        print("Try again")

while time <= 0:
    time = int(input("Enter the time: "))
    if time <= 0:
        print("The time can't be less or equal to 0")
        print("Try again")

total = principle * pow((1 + rate / 100), time)
print(f"The new balance after {time} years is ${total:.2f}")
