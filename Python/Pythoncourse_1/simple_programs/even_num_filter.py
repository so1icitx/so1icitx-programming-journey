numbers = []
even_numbers = []


def even_num_finder():
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print(even_numbers)

while True:
    con = input("Enter a number (c to continue): ")
    if con == "c":
        even_num_finder()
        break
    else:
        numbers.append(int(con))
