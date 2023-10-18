from replit import clear
#HINT: You can call clear() to clear the output in the console.

# import art file
from art import logo 

# print logo
print(logo)

bid_finished = False 
bid_list = {}

# function that determines highest bidder, receives bid_list as an input 
def highest_bid(bid_list):
  max_bid = 0
  highest_bidder = ""
  for bidder in bid_list:
    bid = bid_list[bidder]
    if bid > max_bid:
      max_bid = bid
      highest_bidder = bidder
  print(f'The winner is {highest_bidder} with a bid of ${max_bid}.')
  
while not bid_finished:
  # ask for name
  name = input("What is your name?: ")
  # ask for bid
  bid = int(input(f"Hello {name}, how much would you like to bid?: $"))
  # add name and bid to bid list
  bid_list[name] = bid
  # Ask if there are more bidders
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  # if yes, ask for name and bid
  if more_bidders == "yes":
    clear()
  else:
    bid_finished = True
    highest_bid(bid_list)
  