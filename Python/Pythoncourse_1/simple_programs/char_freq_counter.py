word = input("Enter a word: ")
check = {}

for char in word:
    if char in check:
        check[char] += 1
    else:
        check[char] = 1

for key, value in check.items():
    print(f"{key}: {value}")
