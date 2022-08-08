from turtle import clear
from game_data import data
import art
import random
import os 


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def compare_dictionaries_followers(comparies, answer):
    """Returns True of the answer was correct and removes the wrong lower followers item"""
    if comparies[0]['follower_count'] > comparies[1]['follower_count']:
        if answer == 'A':
            comparies.pop(1)
            return True
    else:
        if answer == 'B':
            comparies.pop(0)
            return True
    return False


def get_compare_data(comparies):
    if len(comparies) == 0:
        comparies.append(data.pop(data.index(random.choice(data))))

    comparies.append(data.pop(data.index(random.choice(data))))

    return comparies
    

def draw_compare(comparies):
    a = comparies[0]
    b = comparies[1]
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(art.vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")




score = 0
comparies = []
game_state = True


while game_state:

    clearConsole()
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}")

    comparies = get_compare_data(comparies)
    draw_compare(comparies)
    player_answer = input("Who has more followers? Type 'A' or 'B': ")
    if compare_dictionaries_followers(comparies, player_answer):
        score += 1
    else:
        clearConsole()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_state = False
    
    