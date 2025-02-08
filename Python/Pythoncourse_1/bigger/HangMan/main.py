import random
from sigma import stages
from sigma import logo
from words import word_list

end_of_game = False
duplicates = []
lives = 6

signal = random.randint(0, len(word_list) - 1)
chosen_word = word_list[signal]
display = ["_" for _ in chosen_word]

print(logo)
while not end_of_game:
    guess = ""
    while True:
        guess = input("Enter a letter: ").lower()
        if guess in duplicates:
            print("You already entered this letter. Try again.")
        else:
            break

    duplicates.append(guess)

    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
    else:
        print("Incorrect letter, you lost a life")
        lives -= 1
        print(stages[lives])

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True
        print(f"You ran out of lives. The correct word was {chosen_word}.")
