

number = input("Enter a number: ")
total = 0
for i in range(1, len(number) + 1):
    i = number[i - 1]
    total += pow(int(i), 3)

if int(total) == int(number):
    print(True)
else:
    print(False)
