import os
# os.system('clear')

from art import logo
print(logo)

bids = {}

bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name? : ")
    price = int(input("What's your bid? : $"))
    bids[name] = price  # Changed from "bids['name']" to "bids[name]"
    should_continue = input("Are there any other bidders? Type 'YES' or 'NO': ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)  # Call the function after bidding is finished
    else:
        os.system('cls')  # This will clear the console
