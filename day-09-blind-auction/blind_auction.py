# from replit import clear

print("Welcome to the secret auction!")

bids = {}

more_bidders = True

while more_bidders:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower() == "yes"
    bids[name] = bid
    # clear()

highest_bid = 0
highest_bidder = ""

for key in bids:
    bid = bids[key]
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
