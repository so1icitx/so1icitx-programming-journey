word = input("Enter a word: ")
character = input("Enter a char: ")
new_word = ""

for i in word:
    if i in "aeuio":
        new_word += character
    else:
        new_word += i

print(new_word)
