print("Find the largest number")
numbers = []


def find_max(numbers):
    max = 0
    for i in numbers:
        if max < i:
            max = i
    print(max)


while True:
    number = input("Enter a number (m to find the max, q to quit)")
    if number == "q":
        break
    elif number == "m":
        find_max(numbers)
        break
    else:
        number = int(number)
        numbers.append(number)



