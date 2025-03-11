import random

random_number = random.randint(1, 100)
count = 0



print("Welcome to the number guessing game!!\n\nPick a number between 1/100")
while True:
    count += 1
    guess = int(input("Enter your guess: "))
    if guess == random_number:
        print(f"Well done you won, you guessed the right number {random_number}, in {count} guesses")
        break
    elif random_number > guess:
        print("[!] Higher")
    elif random_number < guess:
        print("[!] Lower")
    else:
        print("[ERROR] invalid input")
