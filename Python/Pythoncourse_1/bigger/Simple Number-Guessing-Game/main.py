from art import logo
import random
lives = 0
play_again = True

def start():
    print(logo)
    print("Welcome to the game!!")
    print("Im thinking of a number between 1 and 100")

    def play():
        global lives
        difficulty = input("Choose a difficulty (easy or hard):")
        number = random.randint(1,100)
        if difficulty == "easy":
            lives = 10
        elif difficulty == "hard":
            lives = 5
        else:
            print("Invalid input, try again")
            play()
        print(f"You have {lives} guesses remaining")
        guess = input("Make a guess:")
        print(f"Pssssst the number is {number}")
        while int(guess) != number:
            if lives == 0:
                print("You lost!")
                break
            elif int(guess) == number:
                print(f"You got it! The number was {number}.")
                break
            elif int(guess) > number:
                lives -= 1
                print("Too high")
                print("Guess again")
                print(f"You have {lives} guesses remaining")
                guess = input("Make a guess:")
            elif int(guess) < number:
                lives -= 1
                print("Too low")
                print("Guess again")
                print(f"You have {lives} guesses remaining")
                guess = input("Make a guess:")

    play()
start()

while play_again:
    print("Thanks for playing!")
    again = input("Do you want to play again? (yes or no)")
    if again == "yes":
        print("\n" * 100)
        start()
    elif again == "no":
        play_again = False
    else:
        print("Invalid input, try again")
        again = input("Do you want to play again? (yes or no)")
