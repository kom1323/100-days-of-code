from art import logo
import os
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)




## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 10]

while new_game == 'y':

    clearConsole()
    print(logo)
    player_cards = []
    comp_cards = []
    another_card = 'y'


    comp_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))
    comp_sum = sum(comp_cards)
    player_cards.append(random.choice(cards))
    player_sum = player_cards[0]

    while another_card == 'y':
        player_cards.append(random.choice(cards))
        player_sum += player_cards[-1]
        
        player_sum_print = player_sum

        if 11 in player_cards:
            if player_sum > 21:
                player_cards[player_cards.index(11)] = 1
                player_sum -= 10
                player_sum_print = player_sum
            else: 
                player_sum_print = f"{player_sum_print}/{player_sum_print - 10}"
   
        print(f"\tYour cards {player_cards}, current score: {player_sum_print}")
        print(f"\tComputer's first card: {comp_cards[0]}")
        if player_sum < 21:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            another_card = 'n'


    if player_sum <= 21:
        another_card = 'y'
    
    while another_card == 'y':
        if comp_sum <= player_sum and comp_sum != 21:
            comp_cards.append(random.choice(cards))
            comp_sum += comp_cards[-1]
        else: 
            another_card = 'n'
    

    print(f"Your final hand: {player_cards}, final score: {player_sum}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_sum}")
    if player_sum > 21:
        print("You went over. You lose.")
    elif comp_sum <= 21 and comp_sum > player_sum:
        print("Computer scored higher. You lose")
    elif comp_sum > 21:
        print("Computer went over. You win")
    elif comp_sum == player_sum:
        print("It's a tie.") 
    else:
        print("You scored higher. You win.")

    new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")