more = "yes"
placeholder = 0
bids = {}
winner = ""
differnce_bid = 0
second_placeholder = 0

while more == "yes":
    name = str(input("What is your name?"))
    bids[name] = int(input("What is your bid?"))
    more = input("Is there others who wish to bid? (yes/no)")
    print("\n" * 100)

for bid in bids:
    if bids[bid] > placeholder:
        second_placeholder = placeholder
        placeholder = bids[bid]
        winner = bid
    elif bids[bid] > second_placeholder:
        second_placeholder = bids[bid]

differnce_bid = placeholder - second_placeholder
print(f"\nThe winner is {winner} with a bid of ${placeholder} and with a leading bid of ${differnce_bid}.")
