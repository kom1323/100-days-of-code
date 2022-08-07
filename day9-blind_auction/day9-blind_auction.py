import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


from art import logo
print (logo)

print("Welcome to the secret auction program.")

curr_item_bids = {"max_bid": ["", 0]}
ask_for_name = "yes"

while ask_for_name == "yes":

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    curr_item_bids[name] = bid
    if bid > curr_item_bids["max_bid"][1]:
        curr_item_bids["max_bid"][0] = name
        curr_item_bids["max_bid"][1] = bid

    ask_for_name = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clearConsole()
    



print(f"The winner is {curr_item_bids['max_bid'][0]} with a bid of {curr_item_bids['max_bid'][1]}$")