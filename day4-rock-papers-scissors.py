import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


options = [rock, paper,scissors]
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
pc_input = random.randint(0,2)

#print player choice
print(options[player_input])

#print computer choice
print(f"Computer chose:\n{options[pc_input]}")

if(player_input == pc_input + 1 or (player_input == 0 and pc_input == 2)):
    print("You win")
elif(player_input == pc_input):
    print("Tie")
else:
    print("You lose")