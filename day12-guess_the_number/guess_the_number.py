import random
from art import logo





print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")

number = random.randint(1, 100)

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

for i in range(attempts):
    print(f"You have {attempts - i} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it. The answer was {number}")
        break
    elif guess > number:
        print("Too high.\nGuess again.")
    else:
        print("Too low.\nGuess again.")

if guess != number:
    print("You have run out of guesses, You lose")