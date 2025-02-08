import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computers_hand = []
ai_cards_total = 0
player_hand = []
player_cards_total = 0


def play():
    global ai_cards_total, player_hand, player_cards_total
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    computers_hand.append(random.choice(cards))
    player_cards_total = player_hand[0] + player_hand[1]
    print(
        f"Your hand {player_hand}, with a total of {player_cards_total}. The computer's first card is {computers_hand}")
    pick_another_card = input("Do you want to pick another card? (y/n/exit)").lower()
    if pick_another_card == "y":
        player_hand.append(random.choice(cards))
    elif pick_another_card == "n":
        pass
    elif pick_another_card == "exit":
        print("Game exited")
        return
    else:
        print("Invalid input, try again")
    computers_hand.append(random.choice(cards))
    ai_cards_total = computers_hand[0] + computers_hand[1]
    if ai_cards_total < 15:
        computers_hand.append(random.choice(cards))
    if len(computers_hand) > 2:
        ai_cards_total += computers_hand[2]
    if len(player_hand) > 2:
        player_cards_total += player_hand[2]


    if player_cards_total== ai_cards_total:
        print(f"Its a draw {player_cards_total}")
    elif player_cards_total > 21:
        print(f"You lose your total is {player_cards_total}, computer's total is {ai_cards_total}")
    elif ai_cards_total > 21:
        print(f"You win the computer total is higher than 21 ({ai_cards_total}), your total is {player_cards_total}")
    elif player_cards_total > ai_cards_total:
        print(f"You win your total is {player_cards_total}, computer's hand {ai_cards_total}")

    elif player_cards_total < ai_cards_total:
        print(f"You lose your total is {player_cards_total}, computer's total is {ai_cards_total}")

while True:
    play()
    again = input("Do you want to play again? y/n").lower()
    if again == "y":
        print(f"\n" * 100)
        computers_hand = []
        ai_cards_total = 0
        player_hand = []
        player_cards_total = 0
        continue
    elif again == "n":
        break
    else:
        print("Invalid input")
