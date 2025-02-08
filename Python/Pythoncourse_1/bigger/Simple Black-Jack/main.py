import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ai_cards = []
player_cards = []
player_total = 0
ai_total = 0
while True:
    ai_cards.append(random.choice(cards))

    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    print(f"Your cards: {player_cards} Overall {player_cards[0] + player_cards[1]}")
    print(f"The computers first hand {ai_cards}")
    print(f"Do you want to draw another card? y/n")
    another = input().lower()
    if another == "y":
        player_cards.append(random.choice(cards))
        ai_cards.append(random.choice(cards))
        player_total = player_cards[0] + player_cards[1] + player_cards[2]
        ai_total = ai_cards[0] + ai_cards[1]
        if player_total > 21:
            print(f"You lose your total is {player_total}, computer's total is {ai_total}")
        elif player_total > ai_total:
            print(f"You win your total is {player_total}, computer's hand {ai_total}")
        elif player_total == ai_total:
            print(f"Its a draw {player_total}")
        elif player_total < ai_total:
            print(f"You lose your total is {player_total} computers hand {ai_total}")
    elif another == "n":
        ai_cards.append(random.choice(cards))
        player_total = player_cards[0] + player_cards[1]
        ai_total = ai_cards[0] + ai_cards[1]
        if player_total > 21:
            print(f"You lose your total is {player_total}, computer's total is {ai_total}")
        elif player_total > ai_total:
            print(f"You win your total is {player_total}, computer's hand {ai_total}")
        elif player_total == ai_total:
            print(f"Its a draw {player_total}")
        elif player_total < ai_total:
            print(f"You lose your total is {player_total}, computer's total is {ai_total}")

    again = input(f"Do you want to play again? y/n").lower()
    if again == "y":
        ai_cards = []
        player_cards = []
        continue
    elif again == "n":
        break
